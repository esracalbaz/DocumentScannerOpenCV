import cv2
import numpy as np

img = cv2.imread("Resources/cards.webp")

width,height = 250,350

points1 = np.float32([[390,110],[571,161],[268,306],[508,407]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points1,points2)
outputImage = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Output Image", outputImage)

cv2.waitKey(0)