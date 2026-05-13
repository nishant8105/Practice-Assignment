import cv2
import numpy as np

img = cv2.imread("./highway.jpg")

column = img.shape[1]
row = img.shape[0]

s = np.float32([(1, 0, 150), (0, 1, 70)])

shifted = cv2.warpAffine(img, s, (column, row))

cv2.imshow("Original Image", img)
cv2.imshow("Shifted Image", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()