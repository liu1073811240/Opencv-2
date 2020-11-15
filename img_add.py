import cv2
import numpy as np

x = np.uint8([[250], [180]])
y = np.uint8([[10], [20]])

print(cv2.add(x, y))  # 最大255
print(cv2.subtract(x, y))

img1 = cv2.imread("image/1.jpg")
img2 = np.uint8(img1 * 0.5)  # 图片像素值变为原来的0.5
img3 = cv2.add(img1, img2)
img4 = cv2.subtract(img1, img2)

cv2.imshow("", img3)
cv2.waitKey(0)

cv2.imshow("", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()



