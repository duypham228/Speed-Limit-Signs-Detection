import os
import cv2
import numpy
from dev_ws.model import import_model


# Mapping function to reset 8 bits to 2 bits scale
# Blackwhite threshold = 175
def setBit(value):
    return 255 if value < 50 else 0
def mapping_helper(arr):
    return list(map(setBit, arr))

# Images Folder Path
dirname = os.getcwd()
# curpath = os.path.join(dirname, 'crop-images')
curpath = os.path.join(dirname, 'dev_ws/images')
# croppath = os.path.join(dirname, 'crop-images')
testpath = os.path.join(dirname, 'dev_ws/testdump')


# Getting Each Image Path
for image in os.listdir(curpath):
    impath = os.path.join(curpath, image)
    img = cv2.imread(impath)

    new_width = 250
    new_height = 300
    dsize = (new_width, new_height)
    resize_img = cv2.resize(img, dsize)
    bottom_half = resize_img[150:300, :]
    # print("after: ", resize_img.shape)

    # print(len(resize_img[:,10]))
    # print("Before: ", img.shape)

    # current size img[150h, 250w]
    # os.chdir(testpath)
    # Convert image into gray scale
    leftBound = 15
    rightBound = 235
    bottomBound = 135
    crop = bottom_half[:bottomBound,leftBound:rightBound]
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    # print(len(gray[0]))

    blackWhite = numpy.array(list(map(mapping_helper, gray)), dtype="uint8")
    # print(list(blackWhite))
    # cv2.imwrite("Test.jpeg",blackWhite)

    # print(gray[:, 20])
    # Dense Threshold: 10%
    # denseThreshold = 20

    # calculate condensation of black and white
    portion = 20
    partDict = {}
    for i in range(0, len(blackWhite[0]), portion):
        part = blackWhite[:,i:i+portion]
        blackRatio = (len(part) - (numpy.count_nonzero(part == 0)) / (len(part)*len(part[0]))) * 100
        print(i, blackRatio)
        if i > portion * 2 and i < portion * 10:
            partDict[i] = blackRatio
        # name = "test" + str(i) + ".jpeg"
        # cv2.imwrite(name ,part)

    #split the digits
    speed_limit_file = image.split("-") #number, speed_limit.jpeg
    speed_limit_value = speed_limit_file[1].split(".") #speed_limit, .jpeg
    speed_limit = speed_limit_value[0] #you only want the number from the split list!

    #switch to the directory for the cropped digits
    split_images_path = os.path.join(dirname, "dev_ws/crop-images")
    os.chdir(split_images_path)

    #split the images
    index = min(partDict, key=partDict.get)
    firstDigit = blackWhite[:,0:index+10]
    secondDigit = blackWhite[:, index+10:]

    #save each of the split images
    first_file = speed_limit_file[0] + "-" + speed_limit[0] + ".jpeg"
    second_file = speed_limit_file[0] + "-" + speed_limit[1] + ".jpeg"
    cv2.imwrite(first_file, firstDigit)
    cv2.imwrite(second_file, secondDigit)

# model = import_model()

# # os.chdir(testpath)

# firstDigit = cv2.resize(firstDigit, (28, 28), interpolation=cv2.INTER_CUBIC)
# # cv2.imwrite("first_resize.jpeg", firstDigit)
# firstDigit = firstDigit.reshape(1, 28, 28)

# secondDigit = cv2.resize(secondDigit, (28, 28), interpolation=cv2.INTER_CUBIC)
# # cv2.imwrite("second_resize.jpeg", secondDigit)
# secondDigit = secondDigit.reshape(1, 28, 28)

# first_result = numpy.argmax(model.predict(firstDigit)[0])
# second_result = numpy.argmax(model.predict(firstDigit)[0])

# print(first_result, second_result)