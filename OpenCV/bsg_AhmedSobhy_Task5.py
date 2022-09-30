from ctypes import pointer
import cv2 as cv
import numpy as np
myPoints =[]
global c
c=0
def mouse(event,x,y,flag,params):
    global c
    if event == cv.EVENT_LBUTTONDOWN:
        myPoints.append([x,y])
        c+=1



img = cv.imread("/Users/hany/Downloads/tasks_images_/task_5/jhonsmith.jpg")
width = img.shape[0]
height = img.shape[1]

while c<4:
    print(c)
    cv.imshow("original",img)
    cv.setMouseCallback("original", mouse)
    cv.waitKey(1)

pts1 = np.float32(myPoints)
pts2 = np.float32([[0, 0],[width, 0], [0, height],[width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
warp = cv.warpPerspective(img, matrix, (width, height))
cv.imshow("warp", warp)
cv.waitKey(0)