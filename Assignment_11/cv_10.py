import cv2

img = cv2.imread("./highway.jpg")

resize = cv2.resize(img, (640, 640))

kernal = 3


blur = cv2.medianBlur(resize, kernal)

cv2.imshow("Input", resize)
cv2.imshow("Output", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()