import cv2 as cv
import numpy as np

img = np.zeros((480,720,3), np.uint8)
width= 720
height = 480

i =20
while i <720:
    cv.line(img,(i,0),(i,480),(255, 255, 255), 2)
    cv.line(img, (0,i), (720,i), (255, 255, 255), 2)
    i+=20
cv.circle(img, (int(width/2), int(height/2)), 10, (0, 0, 255), cv.FILLED)
cv.imshow("try", img)
cv.waitKey(0)