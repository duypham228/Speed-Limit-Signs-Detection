import cv2
import pytesseract
import os
import numpy

# images folder path
dirname = os.getcwd()
curpath = os.path.join(dirname, 'images')
# croppath = os.path.join(dirname, 'crop-images')

# os.chdir(croppath)
# Getting Each Image Path
for image in os.listdir(curpath):
    impath = os.path.join(curpath, image)
    img = cv2.imread(impath)
    # print("Before: ", img.shape)

    # # Convert the image to gray scale
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
    resize_img = cv2.resize(img, dsize)


    # Cut the image in half horizontally
    top_img = resize_img[0:150, :]
    bottom_img = resize_img[150:299, :]
    gray_bottom = gray = cv2.cvtColor(bottom_img, cv2.COLOR_BGR2GRAY)
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
        
    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(gray_bottom)
    
    # Appending the text into file
    print(image, ": ", text)

    # Convert image into gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("test.jpeg",gray)