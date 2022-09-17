from threading import Thread
import cv2
import sys
from PyQt5.QtCore import QThread , Qt, pyqtSignal , pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from Therad import Thread


class Appvideo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self,image):
        self.label.setPixmap(QPixmap.fromImage(image)) 

    def showspeed(self):

        self.speed=100
        self.unit_s='m/s'
        text="speed of rov: "+ str(self.speed)+" "+str(self.unit_s)
        self.label.setText('<h1 style="color.blue">'+ text+'</h1>')
    
    def showacc(self):
    
        self.acc=0
        self.unit_a='m/s**2'
        text="acc of rov: "+ str(self.acc)+" "+str(self.unit_a)
        self.label.setText('<h1 style="color.blue">'+ text+'</h1>')

    def showdic(self):
        
        self.angle=0
        self.di='south'
        text="angle of rov: "+ str(self.angle)+" to "+str(self.di)
        self.label.setText('<h1 style="color.blue">'+ text+'</h1>')

    def showCounter(self):   
        self.minute=0
        self.second=0
        self.startwatch=False
        self.label=QLabel(self)
        self.label.setGeometry(100,40,150,70)
        self.start=QPushButton("start",self)
        self.start.setGeometry(50,120,100,40)
        self.start.pressed.connect(self.Start)
        self.reset=QPushButton("reset",self)
        self.reset.setGeometry(160,120,100,40)
        self.reset.pressed.connect(self.Reset)
        timer=QTimer(self)
        timer.timeout.connect(self.showCounter)
        timer.start(1000)
        self.show()
   
    def Reset(self):
        self.minute=0
        self.second=0
    
    def Start(self):
        if self.start.text()=='stop':
            self.start.setText("Resume")
            self.startwatch= False

        else:
            self.startwatch= True
            self.start.setText("stop")

    
    def Reset(self):
        self.minute=0
        self.second=0

    def Start(self):
        if self.start.text()=='stop':
            self.start.setText("Resume")
            self.startwatch= False

        else:
            self.startwatch= True
            self.start.setText("stop")
     
    
    def initUI(self):
        self.setWindowTitle("video Widget")   
        self.setGeometry(100,100,640,480)
        self.resize(1800,1200)
        self.label=QLabel(self)
        self.label.move(280,120)
        self.label.resize(640,480)
        th=Thread(self)
        th.changePixman.connect(self.setImage)
        th.start()

app=QApplication(sys.argv)     
vapp= Appvideo()
vapp.showacc()
vapp.showspeed()
vapp.showdic()
vapp.showCounter()
app.exec_()
