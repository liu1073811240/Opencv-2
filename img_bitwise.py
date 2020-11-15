import cv2

img1 = cv2.imread("image/1.jpg")
img2 = cv2.imread("image/7.jpg")

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 5, 255, cv2.THRESH_BINARY)
# ret, mask = cv2.threshold(img2gray, 5, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("mask", mask)  # 黑底白字

mask_inv = cv2.bitwise_not(mask)  # 取反, 白底黑字
cv2.imshow("mask_inv", mask_inv)

# 利用掩膜（mask）进行“与”操作，即掩膜图像白色区域是对需要处理图像像素的去除，黑色区域是对需要处理图像像素的保留。
img1_bg = cv2.bitwise_and(img1, img1, mask=mask_inv)
cv2.imshow("img1_bg", img1_bg)

dst = cv2.add(img1_bg, img2)
cv2.imshow("res", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



