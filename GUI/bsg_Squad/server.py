from multiprocessing.connection import Client as cli
import cv2 as cv
import base64

adrr = ('0.0.0.0',12345)
conn = cli(adrr, authkey=b'bsg')

vid = cv.VideoCapture(0)
while True:
    while vid.isOpened():
        _,frame = vid.read()
        encoded,buffer = cv.imencode('.jpg',frame,[cv.IMWRITE_JPEG_QUALITY,80])
        message = base64.b64encode(buffer)
        conn.send(message)
        