import cv2

img = cv2.imread("image/1.jpg")

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "beautiful girl 啊", (100, 100), font, 5, (0, 0, 255), 1, lineType=cv2.LINE_AA)  # 抗锯齿线形
cv2.imshow("pic show", img)
cv2.waitKey(0)
cv2.destroyAllWindows()








