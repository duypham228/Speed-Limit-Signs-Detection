import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image

def setBit(value):
    return 255 if value < 50 else 0

def mapping_helper(arr):
    return list(map(setBit, arr))

img = "dev_ws/images/25-25.jpeg"

# Images Folder Path
dirname = os.getcwd()
curpath = os.path.join(dirname, img)
croppath = os.path.join(dirname, 'crop-images')

# Convert the image to gray scale, and cropping
new_width = 250
new_height = 300
dsize = (new_width, new_height)

img = cv2.imread(curpath)
resize_img = cv2.resize(img, dsize)
#cv2.imwrite("resize.jpeg", resize_img)

# Cut the image in half horizontally
top_img = resize_img[0:150, :]
bottom_half = resize_img[150:300, :]

# Convert image into gray scale
leftBound = 15
rightBound = 235
bottomBound = 135
crop = bottom_half[:bottomBound,leftBound:rightBound]
#print("lol surprise: ", crop.shape)
gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("gray.jpeg", gray)

# https://stackoverflow.com/questions/55087860/resize-cpp3787-error-215assertion-failed-func-0-in-function-cvhal
blackWhite = np.array(list(map(mapping_helper, gray)), dtype='uint8')
#cv2.imwrite("Test.jpeg", blackWhite)

# calculate condensation of black and white
portion = 20
partDict = {}
for i in range(0, len(blackWhite[0]), portion):
    part = blackWhite[:, i:i + portion]
    whiteRatio = (len(part) - (np.count_nonzero(part == 0)) / (len(part)*len(part[0]))) * 100
    #print(i, whiteRatio)
    if i > portion * 2 and i < portion * 10:
        partDict[i] = whiteRatio
    # name = "test" + str(i) + ".jpeg"
    # cv2.imwrite(name, part)

index = min(partDict, key=partDict.get)
firstDigit = blackWhite[:, 0:index+10]
secondDigit = blackWhite[:, index+10:]

# retrieve the model for numerical identification
new_model = tf.keras.models.load_model('dev_ws/saved_model/my_model.h5')

#save the images
testpath = os.path.join(dirname, 'dev_ws/test')
first_testpath = os.path.join(testpath, "first.jpeg")
second_testpath = os.path.join(testpath, "second.jpeg")
cv2.imwrite(first_testpath, firstDigit)
cv2.imwrite(second_testpath, secondDigit)

# Apply OCR on the cropped image
#https://wavesofvoqueric.com/software/2020/03/31/19/29/opencv-image-to-tensorflow-tensor/
# firstDigit = cv2.resize(firstDigit, (28, 28), interpolation=cv2.INTER_CUBIC)
# firstDigit = tf.convert_to_tensor(firstDigit, dtype=tf.float32)

#viewing the resized digit of 0.
img_convert = cv2.imread(second_testpath)
secondDigit_reize = cv2.resize(img_convert, (28, 28), interpolation=cv2.INTER_CUBIC)
second_testpath_reize = os.path.join(testpath, "second_resize.jpeg")
cv2.imwrite(second_testpath_reize, secondDigit_reize)
# secondDigit = tf.convert_to_tensor(secondDigit, dtype=tf.float32)

firstDigit = image.load_img(first_testpath, target_size=[28, 28])
secondDigit = image.load_img(second_testpath, target_size=[28, 28])

#image processing changes here - currently firstDigit and secondDigit are numpy.ndarray types
first_arr = image.img_to_array(firstDigit)
first_digit_array = np.expand_dims(first_arr, axis=0)
first_preprocessed = preprocess_input(first_digit_array)

second_arr = image.img_to_array(secondDigit)
second_digit_array = np.expand_dims(second_arr, axis=0)
second_preprocessed = preprocess_input(second_digit_array)

first_result = np.argmax(new_model.predict(first_preprocessed))
second_result = np.argmax(new_model.predict(second_preprocessed))

print(first_result, second_result)