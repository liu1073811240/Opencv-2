import cv2
import numpy as np

# 图像混合
img1 = cv2.imread("image/1.jpg")
print(img1.shape)  # (540, 960, 3)

img2 = np.uint8(np.random.randn(img1.shape[0], img1.shape[1], img1.shape[2]))  # 生成图像噪声
img3 = np.uint8(np.zeros([img1.shape[0], img1.shape[1], img1.shape[2]]))
cv2.imshow("img3", img3)

cv2.putText(img3, "beautiful girl", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 5, lineType=cv2.LINE_AA)  #线形
dst = cv2.addWeighted(img1, 1, img3, 0.1, 0)
# dst = cv2.addWeighted(img1, 1, img2, 0.5, 15)

cv2.imshow("dst", dst)
cv2.imwrite("1.jpg", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()



