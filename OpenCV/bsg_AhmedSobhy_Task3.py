from cmath import sin
import cv2 as cv
import numpy as np
import math

img = np.zeros((200,200,3), np.uint8)
width= 200
height = 200

i =20
speed = eval(input("insert speed in m/s "))
time = eval(input("insert time in hours "))
angle = eval(input("insert angle in degrees "))
time = time*60*60
speed = speed*time
speed/=1000

x = abs(speed*math.sin(math.radians(angle)))
y = abs(speed * math.cos(math.radians(angle)))
print(x)
print(y)
while i <720:
    cv.line(img,(i,0),(i,480),(255, 255, 255), 2)
    cv.line(img, (0,i), (720,i), (255, 255, 255), 2)
    i+=20

x+=(width/2)
y+=(height/2)

cv.circle(img, (int(width/2), int(height/2)), 10, (0, 255, 0), cv.FILLED)
cv.circle(img, (int(x),int(y)),10, (0,0,255), cv.FILLED)
cv.line(img,(int(width/2), int(height/2)), (int(x),int(y)), (0, 0, 0), 5)
cv.imshow("answer", img)
cv.waitKey(0)