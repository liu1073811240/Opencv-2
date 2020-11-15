import cv2


img = cv2.imread("image/3.jpg", 1)  # 1表示以原图形式打开，0表示以灰度图形式打开

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 做二值化之前需要转灰度图
# print(gray.shape)  # (540, 960)

#  阈值二值化（threshold binary）、OSTU二值化
# 小于等于阈值的像素点置为0， 大于阈值的像素点置为255
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print(ret)  # 阈值
print(binary)  # 被处理后的图像
cv2.imshow("gray", gray)
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

