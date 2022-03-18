from PIL import Image, ImageEnhance
import os

imageDir = os.path.join(os.getcwd(), 'images')


# adjust contrast from 0.25 to 0.9 at intervals of 0.05
def applyContrast(directory, image, pilImage):
    img = pilImage.convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    for i in range(25, 90, 5):
        adjustVal = i / 100
        enhancer.enhance(adjustVal).save(os.path.join(directory, str(i) + 'contrast' + image))


# adjust color balance from 0.0 to 0.9 at intervals of 0.1
def applyColor(directory, image, pilImage):
    img = pilImage.convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    for i in range(0, 90, 10):
        adjustVal = i / 100
        enhancer.enhance(adjustVal).save(os.path.join(directory, str(i) + 'color' + image))


# adjust brightness from 0.5 to 0.9 at intervals of 0.05
def applyBrightness(directory, image, pilImage):
    img = pilImage.convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    for i in range(50, 90, 5):
        adjustVal = i / 100
        enhancer.enhance(adjustVal).save(os.path.join(directory, str(i) + 'brightness' + image))


# adjust sharpness from 0.25 to 0.9 at intervals of 0.05
def applySharpness(directory, image, pilImage):
    img = pilImage.convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    for i in range(25, 90, 5):
        adjustVal = i / 100
        enhancer.enhance(adjustVal).save(os.path.join(directory, str(i) + 'sharpness' + image))



def createSyntheticDataset(directory):
    for image in os.listdir(directory):
        img = Image.open(os.path.join(directory, image))
        applyContrast(directory, image, img)
        applyColor(directory, image, img)
        applyBrightness(directory, image, img)
        applySharpness(directory, image, img)
        img.close()


createSyntheticDataset(imageDir)
