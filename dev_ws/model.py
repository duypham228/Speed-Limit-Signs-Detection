from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import ssl
import requests

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import os
from PIL import Image



def import_model():
    new_model = tf.keras.models.load_model('saved_model/my_model')

    # mnist = tf.keras.datasets.mnist

    # (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # x_train, x_test = x_train / 255.0, x_test / 255.0

    # Evaluate the restored model
    # loss, acc = new_model.evaluate(x_test, y_test, verbose=2)

    # print('Restored model, accuracy: {:5.2f}%'.format(100 * acc))
    # print(new_model.predict(x_test).shape)
    
    return new_model