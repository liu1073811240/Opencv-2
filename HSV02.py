import cv2
import numpy as np

img = cv2.imread("image/1.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([0, 50, 100])
upper_blue = np.array([179, 225, 200])

# 函数会将位于两个区域间的值置为255(白色)，位于区间外的值置为0（黑色）。
mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow("frame", img)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()




