import cv2
import numpy as np

# 对于渐变色的图片用HSV色彩空间无法处理好
img = cv2.imread("image/9.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([0, 0, 150])
upper_blue = np.array([50, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow("frame", img)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()