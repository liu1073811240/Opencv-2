import cv2
import numpy as np
import matplotlib.pyplot as plt

# 自适应阈值（局部二值化）
img = cv2.imread('image/10.jpg', 0)
img = cv2.GaussianBlur(img, (5, 5), 0)  # 去除噪声

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 2)

titles = ['Original Image', 'Global Thresholding (v=127)',
          'Adaptive Mean Thresholding', 'Adapting Gaussian Thresholding']

images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()





