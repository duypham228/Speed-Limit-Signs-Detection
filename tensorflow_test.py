import tensorflow as tf
import tensorflow_datasets as tfds

import pathlib
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PIL
import PIL.Image
from __future__ import absolute_import, division, print_function, unicode_literals

def get_images():
    data_dir = pathlib.Path('crop_images') #folder the images are from
    image_count = len(list(data_dir.glob('/*.jpg'))) #printing out the number of images to ensure you have all of them

    numbers = list(data_dir.glob('*')) #save all images as a vector
    PIL.Image.open(str(numbers[0])) #open up an image to test
    return numbers, data_dir

def test_train():
    numbers, data_dir = get_images()

    batch_size = 32 #default parameter; will adjust later if needed
    img_height = 150 #from separator.py
    img_width = 299 #from separator.py

    #train_df.class_names will give you the names of the classes
    #in this case: digits 0-9. is there a way to manipulate this though?

    train_df = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=0.2, subset="training", seed=123,
        image_size=(img_height, img_width), batch_size=batch_size)

    test_df = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=0.2, subset="validation", seed=123,
        image_size=(img_height, img_width), batch_size=batch_size)