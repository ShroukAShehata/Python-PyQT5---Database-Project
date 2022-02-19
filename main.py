# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 09:51:19 2021

@author: DELL
"""
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import sqlite3
import add
from add import AddStudent



con = sqlite3.connect('WE School Students Database.db')
cur = con.cursor()
print("connected")

#cur.execute("CREATE TABLE StudentsData (Id VARCHAR(20) PRIMARY KEY, EnglishName VARCHAR(40),ArabicName VARCHAR(40), Mail VARCHAR(20), Mobile VARCHAR(20), Grade VARCHAR(10), Specialization  VARCHAR(20), Address VARCHAR(50) )" );
#con.commit()
#print ("Table created successfully")


'''
cur.execute("INSERT INTO StudentsData VALUES ('22300000000000','Yousef Hasanen','يوسف حسنين','yousefhasanen@gmail.com','0100000000','2','IT','Cairo')")
cur.execute("INSERT INTO StudentsData VALUES ('22400000000000','Yousef Mohamed','يوسف محمد','yousefmohamed@gmail.com','0100000000','2','IT','Cairo')")
cur.execute("INSERT INTO StudentsData VALUES ('22500000000000','Mostafa Yasser','مصطفي ياسر','mostafayasser@gmail.com','0100000000','2','IT','Cairo')")
cur.execute("INSERT INTO StudentsData VALUES ('22600000000000','Alaa Mohamed','الاءعبدالوهاب','alaaabdelwahab@gmail.com','0100000000','2','IT','Cairo')")
con.commit()
'''



class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("WE School Students Database")
        self.setGeometry(450, 150, 750, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getStudents()
        self.studentSelect()
        self.deleteStudent()

    def mainDesign(self):
        self.studentList = QListWidget()
        self.studentList.setStyleSheet("background-color:powderblue")
        self.studentList.itemClicked.connect(self.studentSelect)

        self.btnNew = QPushButton("Add")
        self.btnNew.setStyleSheet("background-color:blue; color:white")
        self.btnNew.clicked.connect(self.addStudent)

        self.btnDelete = QPushButton("Delete")
        self.btnDelete.setStyleSheet("background-color:orange; color:white")
        self.btnDelete.clicked.connect(self.deleteStudent)


    def layouts(self):
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()

        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 40)
        self.mainLayout.addLayout(self.rightMainLayout, 60)

        self.rightTopLayout.addWidget(self.studentList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnDelete)

        self.setLayout(self.mainLayout)

    def addStudent(self):
        self.newStudent = AddStudent()
        self.close()

    def getStudents(self):
        query = "SELECT EnglishName FROM StudentsData ORDER BY EnglishName ASC"
        students = cur.execute(query).fetchall()   #[e1,e2,e3,....]
        i = 1
        for student in students:
            self.studentList.addItem(str(i)+"-"+str(student[0]))
            i = i+1


    def studentSelect(self):
        for i in reversed(range(self.leftLayout.count())):
            widget= self.leftLayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        item = self.studentList.currentItem()
        if item is not None:
            selstudent = item.text().split("-")[1]
            query = "SELECT * FROM StudentsData WHERE EnglishName = ?"
            selectedstudent = cur.execute(query,(selstudent,)).fetchone()
            con.commit()

            ID = QLabel(selectedstudent[0])
            englishname = QLabel(selectedstudent[1])
            arabicname = QLabel(selectedstudent[2])
            mail = QLabel(selectedstudent[3])
            mobile = QLabel(selectedstudent[4])
            grade = QLabel(str(selectedstudent[5]))
            specialization = QLabel(selectedstudent[6])
            address = QLabel(selectedstudent[7])
            self.leftLayout.setVerticalSpacing(30)



            self.leftLayout.addRow("National ID: ", ID)
            self.leftLayout.addRow("English Name: ", englishname)
            self.leftLayout.addRow("Arabic Name: ", arabicname)
            self.leftLayout.addRow("Mail: ", mail)
            self.leftLayout.addRow("Mobile: ", mobile)
            self.leftLayout.addRow("Grade: ", grade)
            self.leftLayout.addRow("Specialization: ", specialization)
            self.leftLayout.addRow("Address: ", address)


    def deleteStudent(self):
        item = self.studentList.currentItem()
        if item is not None:
            delstudent = item.text().split("-")[1]
            try:
                cur.execute("DELETE FROM StudentsData WHERE EnglishName = ?",(delstudent,))
                con.commit()
                QMessageBox.information(self,"Information","The person has been deleted")
                self.close()
                self.main = Main()
            except:
                QMessageBox.information(self, "Warning!", "Student has not been deleted")

'''
    def closeEvent(self, event):
        self.window = Window()
'''
       
















