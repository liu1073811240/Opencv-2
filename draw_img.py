import cv2
import numpy as np

# 直线、圆、椭圆、矩形
img = cv2.imread("image/1.jpg")
cv2.line(img, (100, 100), (500, 500), (0, 0, 255), thickness=10)
cv2.circle(img, (100, 100), 100, (255, 0, 0), thickness=-1)  # -1表示把里面填满
# cv2.rectangle(img, (100, 30), (210, 180), (0, 255, 0), thickness=1)

cv2.rectangle(img, (200, 200), (100, 50), (0, 255, 0), thickness=1)
cv2.ellipse(img, (200, 200), (100, 50), 0, 90, 360, (0, 0, 255), thickness=-1)  # 0表示旋转角度

cv2.imshow("pic show", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
