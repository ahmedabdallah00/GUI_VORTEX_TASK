import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
class Window(QWidget):

    def __init__():
        pass
    
    def __init__(self,w,h,left,top,color):
        super().__init__()        
        self.setGeometry(w,h,left,top)
        self.setWindowTitle('background-color:{color};')

    def set_w(self,w):
        self.w=w 

    def get_w(self):
        return self.w

    def set_h(self,h):
        self.h=h

    def get_h(self):
        return self.h  

    def set_left(self,left):
        self.left=left

    def get_left(self):
        return self.left

    def set_top(self,top):
        self.top=top

    def get_top(self):
        return self.top

    def set_color(self,color):
        self.color=color

    def get_color(self):
        return self.color

            


        