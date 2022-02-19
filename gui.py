import PyQt5
from PyQt5 import QtCore , QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import sqlite3
from PyQt5 import QtWebEngineWidgets

import main
from main import Main

import main2
from main2 import Main2

import main3
from main3 import Main3



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Future Career Camp Projects")
        self.setGeometry(450, 110, 650, 600)
        self.UI()
        self.show()

    def UI(self):
        self.setStyleSheet("background-color:white")
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QHBoxLayout()

        self.btn1 = QPushButton("Students Database")
        self.btn1.clicked.connect(self.firstproject)
        self.btn1.setStyleSheet("color:white; background-color:blue; font-size:15pt; font-family:Arial Bold")
        self.btn2 = QPushButton("Exam Marks")
        self.btn2.clicked.connect(self.secondproject)
        self.btn2.setStyleSheet("color:white; background-color:blue; font-size:15pt; font-family:Arial Bold")
        self.btn3 = QPushButton("Career Form")
        self.btn3.clicked.connect(self.thirdproject)
        self.btn3.setStyleSheet("color:white; background-color:blue; font-size:15pt; font-family:Arial Bold")
        self.btn4 = QPushButton("WE School Website")
        self.btn4.clicked.connect(self.webproject)
        self.btn4.setStyleSheet("color:white; background-color:orange; font-size:15pt; font-family:Arial Bold")

        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('cover2.PNG'))
     
        
        self.topLayout.addWidget(self.btn1)
        self.topLayout.addWidget(self.btn2)
        self.topLayout.addWidget(self.btn3)
        self.topLayout.addWidget(self.btn4)

        self.bottomLayout.addWidget(self.image)
    
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        self.setLayout(self.mainLayout)
        self.show()

    def firstproject(self):
        self.object1 = Main()
        self.close()

    def secondproject(self):
        self.object2 = Main2()
        self.close()

    def thirdproject(self):
        self.object3 = Main3()
        self.close()

    def webproject(self):
        print("file:///E:/Work/We%20School/Camp/Web%20Design%20Content/WE%20School%20Website-%20ed1/final%20project%20home%20.html")


    
        
    
        
        


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()


    

        
        
'''
app = QtWidgets.QApplication(sys.argv)
view = QtWebEngineWidgets.QWebEngineView()

view.load(QtCore.QUrl().fromLocalFile(
    os.path.split(os.path.abspath(__file__))[0]+r'\E:\Work\We School\Camp\Web Design Content\WE School Website- ed1\final project home .html'
))
'''
