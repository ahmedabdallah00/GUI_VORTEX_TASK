import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit

app= QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Python")
l0=QFormLayout()
t=QVBoxLayout()
l =QHBoxLayout()
l0.addRow("screen",QLineEdit())

l1=QVBoxLayout()
l1.addWidget(QPushButton("ac"))
l1.addWidget(QPushButton("1"))
l1.addWidget(QPushButton("2"))
l1.addWidget(QPushButton("3"))
l1.addWidget(QPushButton("0"))
l2=QVBoxLayout()
l2.addWidget(QPushButton("M"))
l2.addWidget(QPushButton("4"))
l2.addWidget(QPushButton("5"))
l2.addWidget(QPushButton("6"))
l2.addWidget(QPushButton("="))
l3=QVBoxLayout()
l3.addWidget(QPushButton("MR"))
l3.addWidget(QPushButton("7"))
l3.addWidget(QPushButton("8"))
l3.addWidget(QPushButton("9"))
l3.addWidget(QPushButton("("))
l4=QVBoxLayout()
l4.addWidget(QPushButton("-"))
l4.addWidget(QPushButton("/"))
l4.addWidget(QPushButton("*"))
l4.addWidget(QPushButton("+"))
l4.addWidget(QPushButton(")"))

l.addLayout(l1)
l.addLayout(l2)
l.addLayout(l3)
l.addLayout(l4)
t.addLayout(l0)
t.addLayout(l)

window.setLayout(t)
window.show()
sys.exit(app.exec_())
