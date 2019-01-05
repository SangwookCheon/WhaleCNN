import cv2
import numpy as np
import pandas as pd
import pickle

print('running')
infile = open('/Users/45622/Downloads/fullimages.pickle', 'rb')
train_images = pickle.load(infile)
train_2 = pickle.load(infile)
infile.close()

print(train_images)
print(train_2)