from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Stop Watch")
        self.setGeometry(100, 100, 400, 500)
        self.UI()
        self.show()
        
    def UI(self):
        self.count = 0
        self.flag=False
        self.label = QLabel(self)
        self.label.setGeometry(75, 100, 250, 70)
        self.label.setStyleSheet('border : 4px solid black;')
        self.label.setText(str(self.count))
        self.label.setFont(QFont('Arial', 25))
        self.label.setAlignment(Qt.AlignCenter)
        start = QPushButton('Start', self)
        start.setGeometry(125,250,150,40)
        start.pressed.connect(self.Start)
        pause = QPushButton('Pause', self)
        pause.setGeometry(125,300,150,40)
        pause.pressed.connect(self.Pause)
        reset = QPushButton('Reset', self)
        reset.setGeometry(125,350,150,40)
        reset.pressed.connect(self.Reset)
        timer= QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)


    def Start(self):
        self.flag=True
    def Reset(self):
        self.count = 0
        self.flag=False
        self.label.setText(str(self.count))
    def Pause(self):
        self.flag=False

    def showTime(self):
        if (self.flag == True) :
            self.count+=1
        self.label.setText(str(self.count))


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())