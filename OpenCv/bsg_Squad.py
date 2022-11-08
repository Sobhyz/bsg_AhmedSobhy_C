import cv2 as cv
import numpy as np



img1 = cv.imread("/Users/Sobhyzz/bsg_AhmedSobhy_C/OpenCv/tasks_images_/task_6/coral1.jpg")
img2 = cv.imread("/Users/Sobhyzz/bsg_AhmedSobhy_C/OpenCv/tasks_images_/task_6/coral2.jpg")
img1 = cv.resize(img1,(int(img1.shape[1]*0.75),int(img1.shape[0]*0.75)))
img2 = cv.resize(img2,(int(img2.shape[1]*0.75),int(img2.shape[0]*0.75)))
img1 = np.hstack((img1,img2))
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
        rects.append(((tmpx,tmpy),(x,y),(0,255,0)))
        tmpx=tmpy=-1
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        tt = img.copy()
        cv.rectangle(tt, (tmpx,tmpy),(x,y),(0,255,0),5)
        cv.imshow("done",tt)
        cv.waitKey(1)
    if event == cv.EVENT_RBUTTONDOWN:
        tmpx=x
        tmpy=y
    elif event == cv.EVENT_RBUTTONUP:
        rects.append(((tmpx,tmpy),(x,y),(255,0,0)))
        tmpx=tmpy=-1
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        tt = img.copy()
        cv.rectangle(tt, (tmpx,tmpy),(x,y),(255,0,0),5)
        cv.imshow("done",tt)
        cv.waitKey(1)

while 1:
    global img
    img = np.zeros((720,1080,3),img1.dtype)
    img[50:50+img1.shape[0], 50:50+img1.shape[1]]=img1
    # img[img1.shape[0]:img1.shape[0]+img2.shape[0], img1.shape[0]:img1.shape[0]+img2.shape[1]]=img1
    for i in rects:
        cv.rectangle(img, i[0],i[1],i[2],5)
    cv.putText(img,"left click and drag for green rectangle",(20,480),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv.putText(img,"right click and drag for blue rectangle",(20,520),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv.putText(img,"press q to quit",(20,560),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv.putText(img,"press D to reset",(20,600),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv.imshow("done",img)
    cv.setMouseCallback("done", mouse)
    input = cv.waitKey(1)

    if input == ord('q'):
        break
    elif input==ord('D'):
        rects.clear()
cv.destroyAllWindows()