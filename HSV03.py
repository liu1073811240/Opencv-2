import cv2
import numpy as np

img = cv2.imread("image/2.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

lower_blue = np.array([0, 110, 0])
# upper_blue = np.array([179, 255, 210])
upper_blue = np.array([50, 255, 210])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow("frame", img)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()





