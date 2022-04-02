from PIL import Image, ImageEnhance
import os


# adjust contrast from 0.25 to 0.9 at intervals of 0.05
def applyContrast(directory, saveDirectory, image, pilImage):
    img = pilImage.convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    for i in range(25, 90, 5):
        adjustVal = i / 100
        enhancer.enhance(adjustVal).save(os.path.join(saveDirectory, str(i) + 'contrast' + image))


# adjust color balance from 0.2 to 0.9 at intervals of 0.05
def applyColor(directory, saveDirectory, image, pilImage):
    img = pilImage.convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    for i in range(20, 90, 5):
        adjustVal = i / 100
        enhancer.enhance(adjustVal).save(os.path.join(saveDirectory, str(i) + 'color' + image))


# adjust brightness from 0.5 to 0.9 at intervals of 0.05
def applyBrightness(directory, saveDirectory, image, pilImage):
    img = pilImage.convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    for i in range(50, 90, 5):
        adjustVal = i / 100
        enhancer.enhance(adjustVal).save(os.path.join(saveDirectory, str(i) + 'brightness' + image))


# adjust sharpness from 0.25 to 0.9 at intervals of 0.05
def applySharpness(directory, saveDirectory, image, pilImage):
    img = pilImage.convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    for i in range(25, 90, 5):
        adjustVal = i / 100
        enhancer.enhance(adjustVal).save(os.path.join(saveDirectory, str(i) + 'sharpness' + image))


def createSyntheticDataset(directory, saveDirectory):
    count = 0
    for image in os.listdir(directory):
        img = Image.open(os.path.join(directory, image))
        applyContrast(directory, saveDirectory, image, img)
        applyColor(directory, saveDirectory, image, img)
        applyBrightness(directory, saveDirectory, image, img)
        applySharpness(directory, saveDirectory, image, img)
        count += 1
        print(count)
        img.close()


imageDir = os.path.join(os.getcwd(), 'images')
saveDir = os.path.join(os.getcwd(), 'all-images')
createSyntheticDataset(imageDir, saveDir)
