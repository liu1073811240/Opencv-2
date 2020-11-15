import cv2
import numpy as np
import matplotlib.pyplot as plt

# 简单阈值
# img = cv2.imread("image/1.jpg", 0)
img = np.uint8(np.arange(400*400*3).reshape([400, 400, 3]) / (400*400*3)*255)

# 阈值二值化
# 小于等于阈值的像素点置0， 大于阈值的像素点置255
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 阈值反二值化
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# 截断阈值化（truncate）
# 小于等于阈值的像素点保持原色，大于阈值的像素点置为灰色（与阈值threshold一致）
ret3, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# 阈值取零（threshold to zero）
# 小于等于阈值的像素点置0， 大于阈值的像素点保持原色
ret4, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# 阈值反取零（threshold to zero inverted）
# 小于等于阈值的像素点保持原色，大于阈值的像素点置为0
ret5, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    # plt.xticks([]),  # 将x轴标尺去掉
    # plt.yticks([])
plt.show()
