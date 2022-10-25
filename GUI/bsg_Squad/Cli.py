from multiprocessing.connection import Listener as l
import cv2 as cv
import numpy as np
import base64
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("bsg_squad/form.ui",self)
        self.Photo = self.findChild(QLabel, "label")
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.show()
    def ImageUpdateSlot(self, Image):
        self.Photo.setPixmap(QPixmap.fromImage(Image))
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):
        self.ThreadActive = True
        self.adrr = ('0.0.0.0',12345)
        self.lis = l(self.adrr, authkey=b'bsg')
        self.conn = self.lis.accept()
        
        while self.ThreadActive:
            packet = self.conn.recv()
            data = base64.b64decode(packet,' /')
            npdata = np.fromstring(data,dtype=np.uint8)
            frame = cv.imdecode(npdata,1)
            frame = cv.flip(frame, 1)
            
            converted = QImage(frame, frame.shape[1],
                            frame.shape[0], frame.shape[1] * 3,QImage.Format_RGB888).rgbSwapped()
            Pic = converted.scaled(640, 480, Qt.KeepAspectRatio)
            self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()



app = QApplication(sys.argv)
UiWindow = UI()
app.exec_()


