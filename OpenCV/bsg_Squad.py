import cv2 as cv
import numpy as np

r,g,b=0,255,0


rects = []
tmpx,tmpy=-1,-1
def mouse(event,x,y,flags,param):
    global tmpx
    global tmpy
    global img
    if event == cv.EVENT_LBUTTONDOWN:
        tmpx=x
        tmpy=y
    elif event == cv.EVENT_LBUTTONUP:
        rects.append(((tmpx,tmpy),(x,y),(b,g,r)))
        tmpx=tmpy=-1
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        tt = img.copy()
        cv.rectangle(tt, (tmpx,tmpy),(x,y),(b,g,r),5)
        cv.imshow("done",tt)
        cv.waitKey(1)
    elif event == cv.EVENT_RBUTTONDOWN:
        rects.pop()

while 1:
    global img
    img = np.zeros((400,400,3), np.uint8)  
    for i in rects:
        cv.rectangle(img, i[0],i[1],i[2],5)
    cv.imshow("done",img)
    cv.setMouseCallback("done", mouse)
    input = cv.waitKey(1)

    if input == ord('q'):
        break
    elif input == ord('r'):
        r,g,b=255,0,0
    elif input == ord('g'):
        r,g,b = 0,255,0
    elif input == ord('b'):
        r,g,b=0,0,255
cv.destroyAllWindows()