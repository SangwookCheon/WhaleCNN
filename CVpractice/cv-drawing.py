import numpy as np
import cv2

canvas1 = np.zeros((300, 300, 3), dtype = 'uint8')
# 8 bits integers, as range is from 0 to 255

# Drawing Lines and Rectangles ------------------
cv2.line(canvas1, (0, 0), (300, 300), (255, 0, 0), 1)
#starting point, ending point, color (BGR), thickness (-1: fill)
cv2.line(canvas1, (0, 300), (300, 0), (0, 255, 0), 3)
cv2.imshow("Canvas", canvas1)
cv2.waitKey(0)

cv2.rectangle(canvas1, (10, 10), (60, 60), (60, 60, 60), 5)
cv2.rectangle(canvas1, (100, 125), (200, 20), (0, 0, 255), -1)
cv2.imshow("Canvas1", canvas1)
cv2.waitKey(0)

# Drawing Circles -----------------

canvas2 = np.zeros((300, 300, 3), dtype='uint8')
(centerX, centerY) = (canvas2.shape[0] // 2, canvas2.shape[1] // 2)

for r in range(0, 175, 25):
    cv2.circle(canvas2, (centerX, centerY), r, (255, 255, 255), 2)
    # center of the circle, radius, color, thickness

cv2.imshow("Canvas2", canvas2)
cv2.waitKey(0)

# Draw Abstract painting
canvas3 = np.zeros((300, 300, 3), dtype='uint8')
for i in range(0, 25):
    center_pos = np.random.randint(low = 0, high = 300, size = (2,)).tolist()
    radius = np.random.randint(low = 5, high = 150)
    color = np.random.randint(low = 0, high = 255, size = (3,)).tolist()
    cv2.circle(canvas3, tuple(center_pos), radius, tuple(color), thickness=-1)
    cv2.imshow("Canvas3", canvas3)
    cv2.waitKey(0)

cv2.imwrite("canvas1_lines_rectangles.jpg", canvas1)
cv2.imwrite('canvas2_circles.jpg', canvas2)
cv2.imwrite('canvas3_circles_art.jpg', canvas3)

canvas4 = np.zeros((300, 300, 3), dtype='uint8')

for i in range(0, 30):
    for r in range(0, 30):
        if i%2 == 0:
            cv2.rectangle(canvas4, (i * 10, r * 10), (i * 10 + 10, r * 10 + 10), (0, 0, 0))
            cv2.rectangle(canvas4, (i * 10, r * 10), (i * 10 + 10, r * 10 + 10), (0, 0, 255))
        else:
            cv2.rectangle(canvas4, (i * 10, r * 10), (i * 10 + 10, r * 10 + 10), (0, 0, 255))
            cv2.rectangle(canvas4, (i * 10, r * 10), (i * 10 + 10, r * 10 + 10), (0, 0, 0))

cv2.imshow('design_challenge', canvas4)



