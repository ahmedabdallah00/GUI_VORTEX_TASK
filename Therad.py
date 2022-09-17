from lib2to3.pytree import convert
import cv2
from PyQt5.QtCore import QThread , Qt, pyqtSignal , pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap

class Thread(QThread):
    changePixman = pyqtSignal(QImage)

    def run(self):
        cap=cv2.VideoCapture(0)
        while True:
            ret, frame=cap.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h,w,c=image.shape
                byteperline=w*c
                qimage=QImage(image.data,w,h,byteperline,QImage.Format_RGB888)
                p=qimage.scaled(640,480,Qt.KeepAspectRatio)
                self.changePixman.emit(p)


c=Thread()                
