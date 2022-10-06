import cv2 as cv
import numpy as np
import random

r = 0
g = 0
b = 0

dx= [(0,50),(50,100), (0,50), (50,100)]
dy = [(0,50),(0,50),(50,100),(50,100)]

img = np.zeros((100,100,3),np.uint8)

for i in range(4):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    img[dx[i][0]:dx[i][1] , dy[i][0]:dy[i][1]] = r,g,b

img = cv.resize(img,(200,200))
cv.imshow("final", img)
cv.waitKey(60000)