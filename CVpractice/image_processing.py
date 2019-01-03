import numpy as np
import argparse
import cv2
import imutils
import os
#imutils is from Pyimagsearcher.com

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image", image)

# Translation -------------
M = np.float32([[1, 0, 25], [0, 1, 50]])
#[1, 0, k] --> Right/Left, [0, 1, k] --> up/down
#negative: up/left, positive: down/right
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("shifted right, down", shifted)
cv2.waitKey(0)

#using imutils
shifted = imutils.translate(image, 25, 50)
cv2.imshow("shifted right, down", shifted)
cv2.waitKey(0)

# Translation -------------
(height, width) = image.shape[:2]
center = (width // 2, height //2)

M = cv2.getRotationMatrix2D(center, -45, 1.0)
#1.0 --> resizes the image if other numbers are put.
rotated = cv2.warpAffine(image, M, (width, height))
cv2.imshow("rotated by 45 degrees", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, -45)
cv2.imshow("rotated by 45 degrees", rotated)
cv2.waitKey(0)

# Resizing ------------------
r = 100 / image.shape[1]
dim = (100, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
#dim --> (width, height)
cv2.imshow("width: 100 resize", resized)
cv2.waitKey(0)

resized = imutils.resize(image, width = 100)
cv2.imshow("width: 100 resize", resized)
cv2.waitKey(0)

# Flipping ------------------

flipped = cv2.flip(resized, 1)
#Horizontal
cv2.imshow("Horizontal", flipped)
cv2.waitKey(0)

flipped = cv2.flip(resized, 0)
#Vertical
cv2.imshow("Vertical", flipped)
cv2.waitKey(0)

flipped = cv2.flip(resized, -1)
#Both horizontal and vertical
cv2.imshow("horizontal and vertical", flipped)
cv2.waitKey(0)

#Cropping ------------------
cropped = image[0:100, 0:400]
#[y, x] above.
cv2.imshow("cropped", cropped)
cv2.waitKey(0)

#To save a file to a specific path, simply write the full path name
# + image name with the extension.
# path = '/Users/45622/DevResources/'
# cv2.imwrite(os.path.join(path, 'resized_img_1.jpg'), resized)

print(image[:50, :50])
#As each image gets transformed into a 3d array, can save each image in a giant dictionary.

dict_images = {'image_1': image}
print(dict_images['image_1'].shape[0])