from PyQt5 import QtCore, QtGui, QtWidgets

op=""
num1,num2=0,0
c=1
d=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 728)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 491, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.mod = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("%"))
        self.mod.setGeometry(QtCore.QRect(20, 130, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.mod.setFont(font)
        self.mod.setObjectName("mod")
        self.c = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("C"))
        self.c.setGeometry(QtCore.QRect(150, 130, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.c.setFont(font)
        self.c.setObjectName("c")
        self.l = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("<<"))
        self.l.setGeometry(QtCore.QRect(280, 130, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.l.setFont(font)
        self.l.setObjectName("l")
        self.div = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("/"))
        self.div.setGeometry(QtCore.QRect(410, 130, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.div.setFont(font)
        self.div.setObjectName("div")
        self.mul = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("x"))
        self.mul.setGeometry(QtCore.QRect(410, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.mul.setFont(font)
        self.mul.setObjectName("mul")
        self.eight = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("8"))
        self.eight.setGeometry(QtCore.QRect(150, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.seven = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("7"))
        self.seven.setGeometry(QtCore.QRect(20, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.nine = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("9"))
        self.nine.setGeometry(QtCore.QRect(280, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.min = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("-"))
        self.min.setGeometry(QtCore.QRect(410, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.min.setFont(font)
        self.min.setObjectName("min")
        self.five = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("5"))
        self.five.setGeometry(QtCore.QRect(150, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.four = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("4"))
        self.four.setGeometry(QtCore.QRect(20, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.six = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("6"))
        self.six.setGeometry(QtCore.QRect(280, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.plus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("+"))
        self.plus.setGeometry(QtCore.QRect(410, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.one = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("1"))
        self.one.setGeometry(QtCore.QRect(20, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.dot = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("."))
        self.dot.setGeometry(QtCore.QRect(280, 570, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.dot.setFont(font)
        self.dot.setObjectName("dot")
        self.zero = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("0"))
        self.zero.setGeometry(QtCore.QRect(150, 570, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.three = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("3"))
        self.three.setGeometry(QtCore.QRect(280, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.two = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("2"))
        self.two.setGeometry(QtCore.QRect(150, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.eq = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("="))
        self.eq.setGeometry(QtCore.QRect(410, 570, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.eq.setFont(font)
        self.eq.setObjectName("eq")
        self.nott = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.press("!"))
        self.nott.setGeometry(QtCore.QRect(20, 570, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.nott.setFont(font)
        self.nott.setObjectName("nott")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 22))
        self.menubar.setObjectName("menubar")
        self.menuCASIO = QtWidgets.QMenu(self.menubar)
        self.menuCASIO.setObjectName("menuCASIO")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCASIO.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press(self,pr):
        global op,d,num1,num2,c
        if pr == 'C':
            self.label.setText('0')
            num1=num2=0
            d=0
            c=1
            op=""
        elif pr == '%':
            if op=="":
                op+=pr
                d=0
                c=1
        elif pr == '/':
            if op=="":
                op+=pr
                c=1
                d=0
        elif pr == '-':
            if op=="":
                op+=pr
                d=0
                c=1
        elif pr == 'x':
            if op=="":
                op+=pr
                d=0
                c=1
        elif pr == '+':
            if op=="":
                op+=pr
                d=0
                c=1
        if pr=='!':
            if op=="":
                num1*=-1
                d=0
            else:
                num2*=-1
                d=0
        if pr == '<<':
            if op=="":
                num1=int(num1/10)
            else:
                num2=int(num2/10)
        if pr>='0' and pr<='9':
            if op=="":
                if d:
                    num1+=(int(pr)/(10**c))
                    c+=1
                else:
                    num1*=10
                    num1+=int(pr)
            else:
                if d:
                    num2+=(int(pr)/(10**c))
                    c+=1
                else:
                    num2*=10
                    num2+=int(pr)
        if pr =='.':
            d=1
        if pr == '=' and num2 !=0:
            if op=="x":
                self.label.setText(f"{num1*num2}")
            elif op=="/":
                self.label.setText(f"{num1/num2}")
            elif op=="%":
                self.label.setText(f"{num1%num2}")
            elif op=="+":
                self.label.setText(f"{num1+num2}")
            elif op=="-":
                self.label.setText(f"{num1-num2}")
            num1=num2=0
            op=""
            d=0
            c=1
            
        elif op=="":
            self.label.setText(f"{num1}")
        else:
            if num2==0:
                self.label.setText('0')
            self.label.setText(f"{num2}")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CASIO"))
        self.label.setText(_translate("MainWindow", "0"))
        self.mod.setText(_translate("MainWindow", "%"))
        self.c.setText(_translate("MainWindow", "C"))
        self.l.setText(_translate("MainWindow", "<<"))
        self.div.setText(_translate("MainWindow", "/"))
        self.mul.setText(_translate("MainWindow", "X"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.min.setText(_translate("MainWindow", "-"))
        self.five.setText(_translate("MainWindow", "5"))
        self.four.setText(_translate("MainWindow", "4"))
        self.six.setText(_translate("MainWindow", "6"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.one.setText(_translate("MainWindow", "1"))
        self.dot.setText(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.three.setText(_translate("MainWindow", "3"))
        self.two.setText(_translate("MainWindow", "2"))
        self.eq.setText(_translate("MainWindow", "="))
        self.nott.setText(_translate("MainWindow", "+/-"))
        self.menuCASIO.setTitle(_translate("MainWindow", "CASIO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
