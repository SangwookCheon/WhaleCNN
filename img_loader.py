import numpy as np
import argparse
import cv2
import tensorflow as tf
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import os
import pickle
import pandas as pd

train_id = pd.read_csv('/Users/45622/DevResources/WhaleCNN/train.csv')


def load_photos(directory):
    images = dict()
    index = 0
    length = len(os.listdir(directory))
    print("{} images need to be loaded".format(str(length)))
    for name in os.listdir(directory):
        filename = directory + '/' + str(name)
        image = load_img(filename)
        image = img_to_array(image)
        image_id = name.split('.')[0]
        images[image_id] = image
        index = index + 1
        if index % 1000 == 0:
            print('1000 images loaded. Loading...')
        elif index == length // 100:
            print('{} images successfully loaded.'.format(str(length // 100)))
            return images
        elif (index % 500 == 0) and (index % 1000 != 0):
             print('500 images loaded.')


directory = '/Users/45622/DevResources/WhaleCNN/train'
images = load_photos(directory)

import bz2

full_images = open('fullimages.pickle', 'wb')
pickle.dump(images, full_images)
full_images.close()

