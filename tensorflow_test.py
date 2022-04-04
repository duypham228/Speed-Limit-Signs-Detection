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

    return train_df, test_df

def model_building():
    train_df, test_df = test_train()

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(150, 299)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ]) #build model by stacking layers
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        #selectop optimizer and loss function used for training

    model.fit(train_df, epochs=5) #train
    model.evaluate(test_df) #evaluate