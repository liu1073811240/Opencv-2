import cv2
import numpy as np

img1 = cv2.imread("image/1.jpg")
img2 = cv2.imread("image/8.jpg")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
# print(img1.shape, img2.shape)

img3 = cv2.add(np.uint8(img1*0.5), np.uint8(img2*0.5))
# img3 = cv2.add(img1, np.uint8(img2*0.2))
# img3 = cv2.subtract(img1, np.uint8(img2*0.2))
# img3 = cv2.divide(img1, np.uint8(img2*1.1))
# img3 = cv2.multiply(img1, np.uint8(img2*0.01))

cv2.imshow("", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()


