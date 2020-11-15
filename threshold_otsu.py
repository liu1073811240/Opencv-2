import cv2
import matplotlib.pyplot as plt

# 将彩色图转化为灰色图
img = cv2.imread("image/1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 将灰色图转化为二值化图（0， 255）， otsu是自动求取阈值
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(ret)

# 简单阈值的几种类型
ret, binary_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
ret, truncate = cv2.threshold(gray, 0, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
ret, tozero = cv2.threshold(gray, 0, 255, cv2.THRESH_TOZERO | cv2.THRESH_OTSU)
ret, tozero_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_TOZERO_INV | cv2.THRESH_OTSU)

# 结合matplotlib, 展示多张二值化图
titles = ['Gray Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [gray, binary, binary_inv, truncate, tozero, tozero_inv]
for i in range(6):
    # 划分2行3列的区域， 在第（i+1）个区域上画图
    plt.subplot(2, 3, i+1)

    # 将图片显示在画板上
    # cmap颜色映射：当img形状是三维矩阵（N,N,3）或（N,N,4）,值被解释为RGB或RGBA, 此时cmap将被忽略
    # 当img形状是二维矩阵的（M, N），此时cmap用于值到颜色的一个映射
    plt.imshow(images[i], cmap="gray")
    # plt.imshow(images[i])  # 默认把灰色图转为RGB图

    # 添加标题
    plt.title(titles[i])

    # 清空x轴，y轴刻度
    plt.xticks([])
    plt.yticks([])
plt.show()  # 显示画板








