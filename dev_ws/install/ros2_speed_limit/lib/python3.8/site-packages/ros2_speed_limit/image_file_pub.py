import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import cv2
import pytesseract
import os
import numpy


class Image_File_Pub(Node):

    def __init__(self):
        super().__init__('image_file_pub')
        self.publisher_ = self.create_publisher(String, 'file_path', 10)
        timer_period = 5 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def path(self):
        #images folder path
        dirname = os.getcwd()
        curpath = os.path.join(dirname, 'images')
        dir_list = os.listdir(curpath)
       
        image = dir_list[self.i]
        impath = ""
       
        try:
            impath = os.path.join(curpath, image)
        except:
            print("image does not exist")

        return impath

    
    
    def timer_callback(self):
        msg = String()
        file_path = self.path()
        
        if file_path == "":
            return
        msg.data = file_path
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
    



def main(args=None):
    rclpy.init(args=args)

    image_file_pub = Image_File_Pub()

    rclpy.spin(image_file_pub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_file_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()