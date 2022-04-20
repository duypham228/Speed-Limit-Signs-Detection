import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8, Image

import cv2
import os
import numpy
import sys
dirname = os.getcwd()
print(dirname)
sys.path.append(dirname)
from model import import_model

class Classifier(Node):

    impath = ""
    def __init__(self):
        super().__init__('classifier')
        self.subscription = self.create_subscription(
            Image, 'file', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(Int8, 'speed_limit_value', 10)
        timer_period = 5 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0


    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.impath = msg.data


    # Mapping function to reset 8 bits to 2 bits scale
    # Black-white threshold = 175
    def setBit(self, value):
        return 255 if value < 50 else 0


    def mapping_helper(self, arr):
        return list(map(self.setBit, arr))


    def cropper(self):
        # Convert the image to gray scale, and cropping
        new_width = 250
        new_height = 300
        dsize = (new_width, new_height)
        resize_img = cv2.resize(self.img, dsize)

        # Cut the image in half horizontally
        top_img = resize_img[0:150, :]
        bottom_half = resize_img[150:300, :]

        #os.chdir(testpath)
        # Convert image into gray scale
        leftBound = 15
        rightBound = 235
        bottomBound = 135
        crop = bottom_half[:bottomBound,leftBound:rightBound]
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

        # https://stackoverflow.com/questions/55087860/resize-cpp3787-error-215assertion-failed-func-0-in-function-cvhal
        blackWhite = numpy.array(list(map(self.mapping_helper, gray)), dtype='uint8')
        # cv2.imwrite("Test.jpeg", blackWhite)

        # print(gray[:, 20])
        # Dense Threshold: 10%
        # denseThreshold = 20

        # calculate condensation of black and white
        portion = 20
        partDict = {}
        for i in range(0, len(blackWhite[0]), portion):
            part = blackWhite[:, i:i + portion]
            whiteRatio = (len(part) - (numpy.count_nonzero(part == 0)) / (len(part)*len(part[0]))) * 100
            #print(i, whiteRatio)
            if i > portion * 2 and i < portion * 10:
                partDict[i] = whiteRatio
            # name = "test" + str(i) + ".jpeg"
            # cv2.imwrite(name, part)

        index = min(partDict, key=partDict.get)
        firstDigit = blackWhite[:, 0:index+10]
        secondDigit = blackWhite[:, index+10:]

        # retrieve the model for numerical identification
        new_model = import_model()

        #save the images
        # cv2.imwrite("first.jpeg", firstDigit)
        # cv2.imwrite("second.jpeg", secondDigit)

        #open the images - now pytesseract will recognize as image type
        # first_img = os.path.join(testpath, "first.jpeg")
        # second_img = os.path.join(testpath, "second.jpeg")

        # Apply OCR on the cropped image
        firstDigit = cv2.resize(firstDigit, (28, 28), interpolation=cv2.INTER_CUBIC)
        firstDigit = firstDigit.reshape(1, 28, 28)
        secondDigit = cv2.resize(secondDigit, (28, 28), interpolation=cv2.INTER_CUBIC)
        secondDigit = secondDigit.reshape(1, 28, 28)

        first_result = numpy.argmax(new_model.predict(firstDigit)[0])
        second_result = numpy.argmax(new_model.predict(secondDigit)[0])
        
        # Appending the text into file
        text_numerical = None #will return None value if the digit conversion cannot be completed
        
        try:
            text_numerical = (int(first_result) * 10) + int(second_result)
        except:
            print("image is stupid")

        return text_numerical
    
    
    def timer_callback(self):
        msg = Int8()
        number = self.cropper()
        
        if number is None:
            return
        msg.data = number
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)
        #self.i += 1
    

def main(args=None):
    rclpy.init(args=args)

    classifier = Classifier()

    rclpy.spin(classifier)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    classifier.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()