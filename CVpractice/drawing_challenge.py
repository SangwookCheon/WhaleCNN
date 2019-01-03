import numpy as np
import cv2

canvas4 = np.zeros((300, 300, 3), dtype='uint8')

for i in range(0, 30):
    for r in range(0, 30, 2):
        if i % 2 == 0:
            cv2.rectangle(canvas4, (r * 10, i * 10), (r * 10 + 10, i * 10 + 10), (0, 0, 0), -1)
            cv2.rectangle(canvas4, (r * 10 + 10, i * 10), (r * 10 + 20, i * 10 + 10), (0, 0, 255), -1)
        else:
            cv2.rectangle(canvas4, (r * 10, i * 10), (r * 10 + 10, i * 10 + 10), (0, 0, 255), -1)
            cv2.rectangle(canvas4, (r * 10 + 10, i * 10), (r * 10 + 20, i * 10 + 10), (0, 0, 0), -1)

# (width, height) first.

cv2.circle(canvas4, (150, 150), 50, (0, 255, 0), -1)
cv2.imshow('design_challenge', canvas4)
cv2.waitKey(0)

cv2.imwrite('design_challenge.png', canvas4)