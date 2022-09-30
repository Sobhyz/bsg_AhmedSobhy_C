from cmath import sin
import cv2 as cv
import numpy as np
import math

img = np.zeros((480,720,3), np.uint8)
width= 720
height = 480

i =60
speed = eval(input("insert speed in m/s "))
time = eval(input("insert time in hours "))
angle = eval(input("insert angle in degrees "))
time = time*60*60
speed = speed*time
speed/=1000



x = speed*math.sin(math.radians(angle))
y = speed * math.cos(math.radians(angle))
cv.rectangle(img, (40,40),(680,440),(255,255,255),2)
y*=-1
print(x)
print(y)
x*=2
y*=2
while i <680:
    cv.line(img,(i,40),(i,440),(255, 255, 255), 2)
    if i<440:
        cv.line(img, (40,i), (680,i), (255, 255, 255), 2)
    i+=20

x+=(width/2)
y+=(height/2)
cv.putText(img, "N", (int(width/2),30), cv.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255),2)
cv.putText(img, "S", (int(width/2),470), cv.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255),2)
cv.putText(img, "W", (10,int(height/2)), cv.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255),2)
cv.putText(img, "E", (695,int(height/2)), cv.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255),2)
cv.circle(img, (int(width/2), int(height/2)), 10, (0, 255, 0), cv.FILLED)
cv.circle(img, (int(x),int(y)),10, (0,0,255), cv.FILLED)
cv.line(img,(int(width/2), int(height/2)), (int(x),int(y)), (255, 0, 0), 5)
cv.imshow("answer", img)
cv.waitKey(0)