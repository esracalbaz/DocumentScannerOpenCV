import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
#img[100:200, 150:400] = 250,0,0
cv2.line(img,(0,0),(300,400),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(450,100),30,(255,255,0),4)
cv2.putText(img, " HELLO ", (200,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow("Test", img)

cv2.waitKey(0)