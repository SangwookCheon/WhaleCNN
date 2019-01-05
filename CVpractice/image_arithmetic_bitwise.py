import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())
#
# image = cv2.imread(args['image'])
image = cv2.imread('/Users/45622/Desktop/2018-10-19.jpg')

# difference between cv2 operations and Numpy arithmetic
print('max of 255: {}'.format(cv2.add(np.uint8([200]), np.uint8([100]))))
print('min of 255: {}'.format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print('wrap around max: {}'.format(np.uint8([200]) + np.uint8([100])))
print('wrap around min: {}'.format(np.uint8([50]) - np.uint8([100])))

#Produces the results below:
# max of 255: [[255]]
# min of 255: [[0]]
# wrap around max: [44]
# wrap around min: [206]

#Applying operations on an image.

M = np.ones(image.shape, dtype = 'uint8') * 100
subtracted = cv2.subtract(image, M)
cv2.imshow("subtracted", subtracted)
cv2.waitKey(0)

added = cv2.add(image, M)
cv2.imshow("added", added)
cv2.waitKey(0)

#BITWISE Operations --> AND, OR, XOR, NOT

rectangle = np.zeros((300, 300), dtype = 'uint8')
cv2.rectangle(rectangle, (25, 25), (275, 275), (255, 255, 255), -1)

circle = np.zeros((300, 300), dtype = 'uint8')
center = (circle.shape[0] // 2, circle.shape[1] // 2)
cv2.circle(circle, center, 150, (255, 255, 255), -1)

bitwiseAND = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAND)
cv2.waitKey(0)

bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOR)
cv2.waitKey(0)

bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXOR)
cv2.waitKey(0)

bitwiseNOT = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNOT)
cv2.waitKey(0)

cv2.imwrite('bitwiseAND.jpg', bitwiseAND)
cv2.imwrite('bitwiseOR.jpg', bitwiseOR)
cv2.imwrite('bitwiseXOR.jpg', bitwiseXOR)
cv2.imwrite('bitwiseNOT.jpg', bitwiseNOT)