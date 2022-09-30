import cv2 as cv
import numpy as np


circles = []
def mouse(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        circles.append([x,y])
    if event == cv.EVENT_RBUTTONDOWN:
        circles.pop()


while 1:
    img = np.zeros((480,720,3), np.uint8)
    for i in circles:
        cv.circle(img,i,50,(0,255,0),1)
    cv.imshow("Done", img)
    cv.setMouseCallback("Done", mouse)
    if cv.waitKey(1) == ord('q'):
        break
