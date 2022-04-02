import cv2
import pytesseract
import os
import numpy



# Mapping function to reset 8 bits to 2 bits scale
# Blackwhtie threshold = 175
def setBit(value):
    return 0 if value < 50 else 255
def mapping_helper(arr):
    return list(map(setBit, arr))

# Images Folder Path
dirname = os.getcwd()
curpath = os.path.join(dirname, 'images')
# croppath = os.path.join(dirname, 'crop-images')
testpath = os.path.join(dirname, 'testdump')


# Getting Each Image Path
# for image in os.listdir(curpath):
impath = os.path.join(curpath, "crop-25-2.jpeg")
img = cv2.imread(impath)
# img2 = cv2.imread("images/1.jpeg")
# new_width = 250
# new_height = 300
# dsize = (new_width, new_height)
# resize_img = cv2.resize(img2, dsize)
# # print("after: ", resize_img.shape)

# print(len(resize_img[:,10]))
# print("Before: ", img.shape)

# current size img[150h, 250w]
os.chdir(testpath)
# Convert image into gray scale
leftBound = 15
rightBound = 235
bottomBound = 135
crop = img[:bottomBound,leftBound:rightBound]
gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
# print(len(gray[0]))

blackWhite = numpy.array(list(map(mapping_helper, gray)))
# print(list(blackWhite))
cv2.imwrite("Test.jpeg",blackWhite)

# print(gray[:, 20])
# Dense Threshold: 10%
# denseThreshold = 20

# calculate condensation of black and white
portion = 20
partDict = {}
for i in range(0, len(blackWhite[0]), portion):
    part = blackWhite[:,i:i+portion]
    blackRatio = (numpy.count_nonzero(part == 0) / (len(part)*len(part[0]))) * 100
    print(i, blackRatio)
    if i > portion * 2 and i < portion * 10:
        partDict[i] = blackRatio
    name = "test" + str(i) + ".jpeg"
    cv2.imwrite(name ,part)

index = min(partDict, key=partDict.get)
firstDigit = blackWhite[:,0:index+10]
secondDigit = blackWhite[:, index+10:]
cv2.imwrite("first.jpeg" ,firstDigit)
cv2.imwrite("second.jpeg" ,secondDigit)
