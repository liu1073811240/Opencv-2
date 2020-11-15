import cv2
import numpy as np

# 多边形
img = np.zeros((400, 400, 3))

#定义n个顶点做点
pts = np.array([[100, 100], [200, 150], [300, 150], [300, 300], [100, 150]])

# pts - 多边形的顶点   isClosed - 是否闭合线段
cv2.polylines(img, [pts], 1, (0, 0, 255), thickness=2)  # 画折线
cv2.fillPoly(img, [pts], color=(0, 255, 0))  # 填充折线

cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




