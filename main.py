import cv2
import pytesseract
import os



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
<<<<<<< master
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
=======
for image in os.listdir(curpath):
    impath = os.path.join(curpath, image)
    img = cv2.imread(impath)
    # print("Before: ", img.shape)

    # # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # # Performing OTSU threshold
    # ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))

    # # Applying dilation on the threshold image
    # dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    # # Finding contours
    # contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # current size img[300h, 250w]
    # Creating a copy of image
    # im2 = img.copy()
    new_width = 250
    new_height = 300
    dsize = (new_width, new_height)
    resize_img = cv2.resize(gray, dsize) #using grayscale image here

    # Cut the image in half horizontally
    top_img = resize_img[0:150, :]
    bottom_img = resize_img[150:299, :]
    gray_bottom = cv2.cvtColor(bottom_img, cv2.COLOR_BGR2GRAY)
    filename = "crop-" + image
    # cv2.imwrite(filename, cropped_img)
    # for cnt in contours:
        # x, y, w, h = cv2.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        # rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (255, 255, 255), 2)
        
        # Cropping the text block for giving input to OCR
        # cropped = im2[y:y + h, x:x + w]
        
        # Open the file in append mode
        # file = open("recognized.txt", "a")
        
    # Apply OCR on the cropped image (optical character recognition)
    text = pytesseract.image_to_string(gray_bottom)
    
    # Appending the text into file
    print(image, ": ", text)
>>>>>>> ros_package_demo
