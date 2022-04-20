import rclpy
from rclpy.node import Node
from std_msgs.msg import Image

import cv2
import os
import numpy as np

class Image_File_Pub(Node):

    def __init__(self):
        super().__init__('image_file_pub')
        self.publisher_ = self.create_publisher(Image, 'file', 10)
        timer_period = 5 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def path(self):
        #images folder path
        dirname = os.getcwd()
        curpath = os.path.join(dirname, 'images')
        dir_list = os.listdir(curpath)
       
        image = dir_list[self.i]
        impath = os.path.join(curpath, image)
       
        try:
            #img = np.asarray(img_cv2)
            img = cv2.imread(impath)
        except:
            print("Image does not exist")

        return img

    
    
    def timer_callback(self):
        msg = Image()
        file = self.path()
        
        if file == "":
            return
        msg.data = file
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