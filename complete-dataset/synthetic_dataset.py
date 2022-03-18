from PIL import Image, ImageEnhance
import os

imageDir = os.path.join(os.getcwd(), 'images')


# adjust contrast from 0.25 to 0.9 at intervals of 0.05
def applyContrast(directory):
    for image in os.listdir(directory):
        img = Image.open(image)
        filename = img.filename
        enhancer = ImageEnhance.Contrast(img)
        for i in range(25, 90, 5):
            adjustVal = i / 100
            enhancer.enhance(adjustVal).save(os.path.join(directory, str(i) + 'contrast' + filename))


# adjust color balance from 0.0 to 0.9 at intervals of 0.1
def applyColor(directory):
    for image in os.listdir(directory):
        img = Image.open(image)
        filename = img.filename
        enhancer = ImageEnhance.Color(img)
        for i in range(9, 90, 10):
            adjustVal = i / 100
            enhancer.enhance(adjustVal).save(os.path.join(directory, str(i) + 'color' + filename))


# adjust brightness from 0.3 to 0.9 at intervals of 0.05
def applyBrightness(directory):
    for image in os.listdir(directory):
        img = Image.open(image)
        filename = img.filename
        enhancer = ImageEnhance.Brightness(img)
        for i in range(30, 90, 5):
            adjustVal = i / 100
            enhancer.enhance(adjustVal).save(os.path.join(directory, str(i) + 'brightness' + filename))


# adjust sharpness from 0.25 to 0.9 at intervals of 0.05
def applySharpness(directory):
    for image in os.listdir(directory):
        img = Image.open(image)
        filename = img.filename
        enhancer = ImageEnhance.Contrast(img)
        for i in range(25, 90, 5):
            adjustVal = i / 100
            enhancer.enhance(adjustVal).save(os.path.join(directory, str(i) + 'sharpness' + filename))


def createSyntheticDataset(directory):
    applyBrightness(directory)
    applyColor(directory)
    applyContrast(directory)
    applySharpness(directory)


createSyntheticDataset(imageDir)
