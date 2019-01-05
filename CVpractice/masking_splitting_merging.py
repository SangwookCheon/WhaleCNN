import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

image = cv2.imread('/Users/45622/Desktop/2018-10-19.jpg')

# Masking

mask1 = np.zeros(image.shape[:2], dtype='uint8')
mask2 = np.zeros(image.shape[:2], dtype='uint8')
(cX, cY) = (image.shape[1] // 2, image.shape[0] //2)
cv2.rectangle(mask1, (cX - 50, cY - 50), (cX + 50, cY + 50), (255, 255, 255), -1)
cv2.circle(mask2, (cX, cY), 70, (255, 255, 255), -1)
masked1 = cv2.bitwise_and(image, image, mask = mask1)
masked2 = cv2.bitwise_and(image, image, mask = mask2)

cv2.imshow('rectangle mask', masked1)
cv2.imshow('circle mask', masked2)
cv2.waitKey(0)

# Splitting channels
(B, G, R) = cv2.split(image)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.waitKey(0)

zeros = np.zeros(image.shape[:2], dtype='uint8')
cv2.imshow("B", cv2.merge([zeros, zeros, B]))
cv2.waitKey(0)

#Color spaces
cv2.imshow('GRAY', cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
cv2.imshow('LAB', cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
cv2.imshow('HSV', cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
cv2.waitKey(0)

cv2.imwrite("GRAY.png", cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
cv2.imwrite("LAB.png",cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
cv2.imwrite("HSV.png",cv2.cvtColor(image, cv2.COLOR_BGR2LAB))


