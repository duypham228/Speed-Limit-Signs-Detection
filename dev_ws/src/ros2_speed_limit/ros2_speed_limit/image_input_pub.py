import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

import cv2
import pytesseract
import os



class Image_Input_Publisher(Node):

    def __init__(self):
        super().__init__('image_input_pub')
        self.publisher_ = self.create_publisher(Int8, 'speed_limit_value', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0

    def cropper(self):
        dirname = os.getcwd()
        curpath = os.path.join(dirname, 'images')
        #for image in os.listdir(curpath):
        image = "1.jpeg"
        impath = os.path.join(curpath, image)
        img = cv2.imread(impath)
    
        # # Convert the image to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #specifying cropped image size
        new_width = 250
        new_height = 300
        dsize = (new_width, new_height)
        resize_img = cv2.resize(img, dsize)

        # Cut the image in half horizontally
        top_img = resize_img[0:150, :]
        bottom_img = resize_img[150:299, :]
        gray_bottom = cv2.cvtColor(bottom_img, cv2.COLOR_BGR2GRAY)
      
            
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(gray_bottom)
        
        # Appending the text into file
        text_numerical = -1000
        try:
            text_numerical = int(text)
        except:
            print("Image can not be read. Thus, returning -1000")
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