import os
import cv2

# Images Folder Path
dirname = os.getcwd()
curpath = os.path.join(dirname, 'images')
croppath = os.path.join(dirname, 'crop-images')

os.chdir(croppath)
# Getting Each Image Path
for image in os.listdir(curpath):
    impath = os.path.join(curpath, image)
    img = cv2.imread(impath)
    print("Before: ", img.shape)
    
    # Resize to the same size
    new_width = 250
    new_height = 300
    dsize = (new_width, new_height)
    resize_img = cv2.resize(img, dsize)
    print("after: ", resize_img.shape)
    
    # print(filename)
    

    # Cut the image in half horizontally
    cropped_img = resize_img[150:300, :]
    filename = "crop-" + image
    cv2.imwrite(filename, cropped_img)
    
# cv2.waitKey(0)
# cv2.destroyAllWindows()   
