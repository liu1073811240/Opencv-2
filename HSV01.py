import cv2
import numpy as np

arc = cv2.imread("image/1.jpg")
dst = cv2.cvtColor(arc, cv2.COLOR_BGR2HSV)

cv2.imshow("pic show", arc)
cv2.imshow("arc show", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()







