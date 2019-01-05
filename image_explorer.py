import numpy as np
import argparse
import cv2
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import os
import pickle
import pandas as pd

image = load_img('/Users/45622/DevResources/WhaleCNN/train/0a0c1df99.jpg')
array = img_to_array(image, dtype='uint8')
dict = {'image1': array}

store = open('exampleimage.pickle2', 'wb')
pickle.dump(dict, store, protocol= pickle.HIGHEST_PROTOCOL)
store.close()