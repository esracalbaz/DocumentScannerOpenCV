import cv2
import numpy as np

img = cv2.imread("Resources/dog.png")
print(img.shape)
imgResize = cv2.resize(img, (1000,1100))
imgCrop = img[0:300,200:600]

cv2.imshow("Image", img)
cv2.imshow("Image resize", imgResize)
cv2.imshow("Image cropped", imgCrop)
cv2.waitKey(0)