import os
import cv2
import numpy

# Images Folder Path
dirname = os.getcwd()
orig_imgs_path = os.path.join(dirname, "dev_ws/backup-images")
curpath = os.path.join(dirname, 'dev_ws/dataset/crop-images')

for image in os.listdir(orig_imgs_path):
    impath = os.path.join(orig_imgs_path, image)
    # print(impath)
    if (len(image) <= 1):
        print("Skipping this file because it is", image)
        continue
    elif (image == ".DS_Store"): #because macs are dumb
        continue
    img = cv2.imread(impath)

    #split the digits
    speed_limit_file = image.split("-") #file number, digit.jpeg
    speed_limit_value = speed_limit_file[1].split(".") #speed_limit, .jpeg
    speed_limit = speed_limit_value[0] #you only want the number from the split list!

    #save each of the split images
    first_file = speed_limit + "/" + speed_limit_file[0] + "-" + speed_limit + ".jpeg"
    file_path = os.path.join(curpath, first_file)
    print(file_path)
    cv2.imwrite(file_path, img)