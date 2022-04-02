import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

import cv2
import pytesseract
import os
import numpy


class Image_Input_Publisher(Node):

    def __init__(self):
        super().__init__('image_input_pub')
        self.publisher_ = self.create_publisher(Int8, 'speed_limit_value', 10)
        timer_period = 0.5 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0

    # Mapping function to reset 8 bits to 2 bits scale
    # Black-white threshold = 175
    def setBit(value):
        return 0 if value < 50 else 255

    def mapping_helper(arr):
        return list(map(setBit, arr))

    def cropper(self):
        #images folder path
        dirname = os.getcwd()
        curpath = os.path.join(dirname, 'images')

        #for image in os.listdir(curpath):
        image = "1.jpeg"
        impath = os.path.join(curpath, image)
        img = cv2.imread(impath)
    
        # Convert the image to gray scale, and cropping
        leftBound = 15
        rightBound = 235
        bottomBound = 135
        crop = img[:bottomBound, leftBound:rightBound]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        blackWhite = numpy.array(list(map(mapping_helper, gray)))
        # cv2.imwrite("Test.jpeg", blackWhite)

        # Dense Threshold: 10%
        # denseThreshold = 20

        # calculate condensation of black and white
        portion = 20
        partDict = {}
        for i in range(0, len(blackWhite[0]), portion):
            part = blackWhite[:, i:i + portion]
            blackRatio = (numpy.count_nonzero(part == 0) / (len(part) * len(part[0]))) * 100
            # print(i, blackRatio)
            if i > portion * 2 and i < portion * 10:
                partDict[i] = blackRatio
            # name = "test" + str(i) + ".jpeg"
            # cv2.imwrite(name, part)

        index = min(partDict, key=partDict.get)
        firstDigit = blackWhite[:, 0:index+10]
        secondDigit = blackWhite[:, index+10:]
        # cv2.imwrite("first.jpeg", firstDigit)
        # cv2.imwrite("second.jpeg", secondDigit)

        # Apply OCR on the cropped image
        text_left = pytesseract.image_to_string(firstDigit)
        text_right = pytesseract.image_to_string(secondDigit)
        
        # Appending the text into file
        text_numerical = None #will return None value if the digit conversion cannot be completed
        if text_left.isdigit() & text_right.isdigit():
            text_left = int(text_left)
            text_right = int(text_right)
            text_numerical = (text_left * 10) + text_right
        return text_numerical

    
    
    def timer_callback(self):
        msg = Int8()
        number = self.cropper()
        msg.data = number
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)
        #self.i += 1
    



def main(args=None):
    rclpy.init(args=args)

    image_input_publisher = Image_Input_Publisher()

    rclpy.spin(image_input_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_input_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()