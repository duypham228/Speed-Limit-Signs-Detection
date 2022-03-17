import os
import cv2
import numpy

# Images Folder Path
dirname = os.getcwd()
curpath = os.path.join(dirname, 'crop-images')
# croppath = os.path.join(dirname, 'crop-images')

# os.chdir(croppath)
# Getting Each Image Path
# for image in os.listdir(curpath):
impath = os.path.join(curpath, "crop-1.jpeg")
img = cv2.imread(impath)
# print("Before: ", img.shape)

# current size img[300h, 250w]

# Convert image into gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("test.jpeg",gray)