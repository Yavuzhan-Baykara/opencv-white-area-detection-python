import cv2
import numpy as np

img = cv2.imread("image.jpg")

# Beyaz rengi (255, 255, 255) olarak tanımla
lower = np.array([255, 255, 255])
upper = np.array([255, 255, 255])

mask = cv2.inRange(img, lower, upper)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    cv2.drawContours(img, [contour], 0, (0, 0, 255), 2)

cv2.imshow("Image", img)
cv2.imwrite("output.jpg", img)
cv2.waitKey(0)
