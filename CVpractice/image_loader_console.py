import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')

#parse inputs and store them in a dictionary
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Piano concert image", image)
cv2.waitKey(0)
cv2.imwrite('example_image.jpg', image)

## OpenCV stores images as Blue, Green, Red (BGR)
#To index values, go with (y, x), as row starts first.

(b, g, r) = image[219, 90]
print('Pixel at [219, 90]: Red: {}, Green: {}, Blue: {}'.format(r, g, b))

#change the pixel value
# image[0,0] = (220, 220, 220)
#change chunk of the image
image[0:200, 0:100] = (200, 150, 178) # --> 200 y, 100 x
cv2.imshow("Updated img", image)
cv2.waitKey(0)