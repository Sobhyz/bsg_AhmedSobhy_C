from sre_constants import SUCCESS
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("form.ui",self)

        self.openPhoto = self.findChild(QPushButton, "pushButton")
        self.Photo = self.findChild(QLabel, "label")

        self.openPhoto.clicked.connect(self.OP)

        self.show()
    def OP(self):
        fname = QFileDialog.getOpenFileName(self,"Open File","","PNG files(*.png);;Jpeg files(*.jpeg);;Jpg files(*.jpg) ")
        self.pixmap = QPixmap(fname[0])
        self.Photo.setPixmap(self.pixmap)


app = QApplication(sys.argv)
UiWindow = UI()
app.exec_()