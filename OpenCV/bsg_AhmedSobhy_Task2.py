import cv2 as cv


vid = cv.VideoCapture(0)
cap = 0

saved = cv.VideoWriter("video.avi", cv.VideoWriter_fourcc(*'MJPG'), 20.0, (720,480))
r=0
g=0
h=0
x=0
s=0
width,height = 720,480

while 1:
    success, img = vid.read()
    img = cv.resize(img,(width,height))

    if x:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        M = cv.getRotationMatrix2D((width/2,height/2),90,1) 
        rotate = cv.warpAffine(img,M,(width,height)) 
        cv.imshow("GRAY", gray)
        cv.imshow("HSV",hsv)
        cv.imshow("Rotated",rotate)
    if g:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    elif h:
        img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    if r:
        M = cv.getRotationMatrix2D((width/2,height/2),90,1) 
        img = cv.warpAffine(img,M,(width,height)) 
    if s:
        saved.write(img)
    cv.imshow("final", img)
    input = cv.waitKey(1)
    
    if input == ord('c'):
        cv.imwrite(f"img {cap}.png", img)
        cap+=1
    elif input == ord('s'):
        s=1
    elif input==ord('g'):
        g,h,x=1,0,0
    elif input == ord('h'):
        h,g,x=1,0,0
    elif input == ord('z'):
        r=g=h=x=0
    elif input == ord('r'):
        r,x=1,0
    elif input == ord('x'):
        x,h,g,r=1,0,0,0
    elif input == ord('q'):
        break
vid.release()
saved.release()