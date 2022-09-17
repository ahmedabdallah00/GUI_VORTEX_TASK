import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from Window import Window


w=250
h=250
top=250
left=250
color='blue'
app=QApplication(sys.argv)



w1=Window(w,h,top,left,color)
w1.show()
sys.exit(app.exec_())