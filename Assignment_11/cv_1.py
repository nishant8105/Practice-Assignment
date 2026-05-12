import cv2
import numpy as np
img = cv2.imread("D:/Coding/Practice-Assignment/Assignment_11/highway.jpg")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading image
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

cv2.imshow("window", img)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Writing image
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

cv2.imshow("window", img) 
cv2.imwrite('car.jpg', img)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Resizing image
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("Dimensions of the image : ", img.shape)
width = 400
height = 400
dim = (width, height)
resized = cv2.resize(img, dim)

cv2 .imshow("window", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()