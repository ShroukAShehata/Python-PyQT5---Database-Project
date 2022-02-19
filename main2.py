import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import sqlite3


connection = sqlite3.connect("WE School Students Database.db")
cursor = connection.cursor()
'''
cursor.execute("DROP TABLE Grade1Results");
connection.commit()
cursor.execute("CREATE TABLE Grade1Results (NatId TEXT PRIMARY KEY ,Name VARCHAR(30) , Arabic VARCHAR(10) ,English VARCHAR(10) ,Physics VARCHAR(10),Maths VARCHAR(10), TheoriticalSpeciality VARCHAR(10), PracticalSpeciality VARCHAR(10), SiteTraining VARCHAR(10), Religion VARCHAR(10), TotalMarks VARCHAR(10), TotalPercentage VARCHAR(10) ) ");
connection.commit()

cursor.execute("INSERT INTO Grade1Results VALUES ('','Your Name','out of 50','out of 50','out of 40','out of 50','out of 120','out of 120','out of 120','out of 20','out of 550','out of 100%')");
cursor.execute("INSERT INTO Grade1Results VALUES ('1','Ibrahim Sabry Ibrahim','44.5','33.65','35.67','42.17','105.26','117.53','111.37','18.85','490.15','89.12')");
cursor.execute("INSERT INTO Grade1Results VALUES ('2','Ahmed ElAmir Ahmed','46.31','42.62','35.01','46.95','110.83','118.28','110.37','18.12','510.37','92.79')");
cursor.execute("INSERT INTO Grade1Results VALUES ('3','Ahmed Ehab Abdo','43.65','38.8','33.64','46.28','109.08','117.03','106.97','18.11','495.45','90.08')");
cursor.execute("INSERT INTO Grade1Results VALUES ('4','Ahmed Gamal Shaaban','45.27','39.87','33.27','43.35','94.6','112.33','92','17.97','460.69','83.76')");
cursor.execute("INSERT INTO Grade1Results VALUES ('5','Ahmed Hassan Ibrahim','44.93','40.37','34.98','41.89','107.01','111.28','112.67','18.35','493.13','89.66')");
cursor.execute("INSERT INTO Grade1Results VALUES ('6','Ahmed Zakaria Ahmed','45.56','44.72','35.53','44.18','109.31','114.78','92.67','18.29','486.75','88.50')");
cursor.execute("INSERT INTO Grade1Results VALUES ('7','Ahmed Samy Ahmed','46.93','46.13','37.45','45.72','111.07','117.78','104.67','17.97','475.83','86.51')");
cursor.execute("INSERT INTO Grade1Results VALUES ('8','Ahmed Soliman Abdelhamed','44.37','35.3','36.27','42.7','102.29','110.23','104.67','18.21','475.83','86.51')");
cursor.execute("INSERT INTO Grade1Results VALUES ('9','Ahmed Shaaban Hosny','42.18','36.25','31.91','39.99','95.66','103.16','104.67','18.12','453.82','82.51')");
cursor.execute("INSERT INTO Grade1Results VALUES ('10','Ahmed Ali Foaad','43.37','32.03','35.21','42.9','91.5','101.26','106.97','17.06','453.24','82.41')");
connection.commit()
'''
print("done")


class Main2(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Camp Application")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.Layouts()
        self.showResult()
        self.show()

    def UI(self):
        self.identry = QLineEdit(self)
        self.showbtn = QPushButton("Show")
        self.showbtn.clicked.connect(self.showResult)
        self.show()


    def Layouts(self):
        self.biggerlayout = QVBoxLayout()
        self.toplayout = QVBoxLayout()
        self.mainlayout = QFormLayout()

        self.biggerlayout.addLayout(self.toplayout)
        self.biggerlayout.addLayout(self.mainlayout)
        self.toplayout.addWidget(self.identry)
        self.toplayout.addWidget(self.showbtn)


        self.setLayout(self.biggerlayout)
        self.show()

    def showResult(self):
        for i in reversed(range(self.mainlayout.count())):
            widget=self.mainlayout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()




        studentid = self.identry.text()
        query = "SELECT * FROM Grade1Results WHERE NatId=?"
        studentResult = cursor.execute(query , (studentid,) ).fetchone();
        connection.commit()
        id = QLabel(studentResult[0])
        name = QLabel(studentResult[1])
        arabic = QLabel(studentResult[2])
        english  = QLabel(studentResult[3])
        physics = QLabel(studentResult[4])
        maths = QLabel(studentResult[5])
        theospec = QLabel(studentResult[6])
        practicalspec = QLabel(studentResult[7])
        site = QLabel(studentResult[8])
        religion = QLabel(studentResult[9])
        totalmarks = QLabel(studentResult[10])
        totalpercentage = QLabel(studentResult[11])


        self.mainlayout.addRow("Your Id :",id)
        self.mainlayout.addRow("Name :", name)
        self.mainlayout.addRow("Arabic :", arabic)
        self.mainlayout.addRow("English :", english)
        self.mainlayout.addRow("Physics :", physics)
        self.mainlayout.addRow("Maths :", maths)
        self.mainlayout.addRow("Theoritical Speciality :", theospec)
        self.mainlayout.addRow("Practical Speciality :", practicalspec)
        self.mainlayout.addRow("Site Training :", site)
        self.mainlayout.addRow("Religion :", religion)
        self.mainlayout.addRow("Total Marks :", totalmarks)
        self.mainlayout.addRow("Total Percentage :", totalpercentage)
'''
    def closeEvent(self, event):
        self.window = Window()
'''
       












        


