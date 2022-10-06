from ctypes import pointer
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
myPoints =[]
global c
c=0
def mouse(event,x,y,flag,params):
    global c
    if event == cv.EVENT_LBUTTONDOWN:
        myPoints.append([x,y])
        c+=1
    if event == cv.EVENT_RBUTTONDOWN:
        myPoints.clear()
        c=0

def reorder():
    x,y=0,0
    mx=1e9
    newPoints = []
    for i in myPoints:
        if i[0]+i[1]<mx:
            mx = i[0]+i[1]
            x,y = i[0],i[1]
    newPoints.append([x,y])

    mx=0
    for i in myPoints:
        if i[0]-i[1]>mx:
            mx = i[0]-i[1]
            x,y = i[0],i[1]
    newPoints.append([x,y])

    mx=1e9

    for i in myPoints:
        if i[0]-i[1]<mx:
            mx = i[0]-i[1]
            x,y = i[0],i[1]
    newPoints.append([x,y])
    
    

    mx=0
    for i in myPoints:
        if i[0]+i[1]>mx:
            mx=i[0]+i[1]
            x,y=i[0],i[1]
    newPoints.append([x,y])
    return newPoints



img = cv.imread("/Users/hany/Downloads/tasks_images_/task_5/jhonsmith.jpg")
width = img.shape[1]
height = img.shape[0]

while True:
    copy = img.copy()
    for i in myPoints:
        cv.circle(copy, i, 5,(0,255,0),10)
    cv.imshow("original",copy)
    cv.setMouseCallback("original", mouse)
    if c==4:
        myPoints = reorder()
        pts1 = np.float32(myPoints)
        pts2 = np.float32([[0, 0],[width, 0], [0, height],[width, height]])
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        warp = cv.warpPerspective(img, matrix, (width, height))
        # warp = cv.cvtColor(warp, cv.COLOR_BGR2RGB)
        cv.imshow("l",warp)
    
    if cv.waitKey(1)==ord('q'):
        break
