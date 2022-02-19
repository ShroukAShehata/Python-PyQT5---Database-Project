# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:48:13 2021

@author: DELL
"""
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import sqlite3



con = sqlite3.connect('WE School Students Database.db')
cur = con.cursor()



class AddStudent(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Add Student")
        self.setGeometry(450, 150, 750, 600)
        self.mainDesign()
        self.layouts()
        self.show()



    def mainDesign(self):

        self.setStyleSheet("background-color:pink; font-size:14pt")

        self.title = QLabel("Add Student")
        self.title.setStyleSheet('font-size: 24pt; font-family:Arial Bold; color:blue')

        self.idLbl = QLabel("National ID :")
        self.idEntry = QLineEdit()
        self.idEntry.setPlaceholderText("Enter Student National ID")

        self.englishnameLbl = QLabel("English Name :")
        self.englishnameEntry = QLineEdit()
        self.englishnameEntry.setPlaceholderText("Enter Student English Name")

        self.arabicnameLbl = QLabel("Arabic Name :")
        self.arabicnameEntry = QLineEdit()
        self.arabicnameEntry.setPlaceholderText("Enter Student Arabic Name")

        self.mailLbl = QLabel("Mail :")
        self.mailEntry = QLineEdit()
        self.mailEntry.setPlaceholderText("Enter Student Mail")

        self.mobileLbl = QLabel("Mobile :")
        self.mobileEntry = QLineEdit()
        self.mobileEntry.setPlaceholderText("Enter Student Mobile")


        self.gradeLbl = QLabel("Grade :")
        self.gradeEntry = QLineEdit()
        self.gradeEntry.setPlaceholderText("Enter Student Grade")

        self.specializationLbl = QLabel("Specialization :")
        self.specializationEntry = QLineEdit()
        self.specializationEntry.setPlaceholderText("Enter Student Specialization")

        self.addressLbl = QLabel("Address :")
        self.addressEntry = QLineEdit()
        self.addressEntry.setPlaceholderText("Enter Student Address")

        self.addButton = QPushButton("Add")
        self.addButton.setStyleSheet("background-color:blue ; font-size:10pt; color:white")
        self.addButton.clicked.connect(self.addStudentData)

    def layouts(self):

        self.bottomLayout = QFormLayout()


        self.bottomLayout.addRow(self.title)
        self.bottomLayout.addRow(self.idLbl, self.idEntry)
        self.bottomLayout.addRow(self.englishnameLbl, self.englishnameEntry)
        self.bottomLayout.addRow(self.arabicnameLbl, self.arabicnameEntry)
        self.bottomLayout.addRow(self.mailLbl, self.mailEntry)
        self.bottomLayout.addRow(self.mobileLbl, self.mobileEntry)
        self.bottomLayout.addRow(self.gradeLbl, self.gradeEntry)
        self.bottomLayout.addRow(self.specializationLbl, self.specializationEntry)
        self.bottomLayout.addRow(self.addressLbl, self.addressEntry)
        self.bottomLayout.addRow(self.addButton)

        self.setLayout(self.bottomLayout)


    def addStudentData(self):
        ID = self.idEntry.text()
        EnglishName = self.englishnameEntry.text()
        ArabicName = self.arabicnameEntry.text()
        Mail = self.mailEntry.text()
        Mobile = self.mobileEntry.text()
        Grade = self.gradeEntry.text()
        Specialization = self.specializationEntry.text()
        Address = self.addressEntry.text()


        if (ID != ""):
            try:
                cur.execute("INSERT INTO StudentsData VALUES (?,?,?,?,?,?,?,?)", (ID, EnglishName, ArabicName, Mail, Mobile, Grade, Specialization, Address));
                con.commit()
                #print("done")
                QMessageBox.information(self, "Success", "Student has been added")

            except:
                QMessageBox.information(self, "Warning", "Student has not been added")
        else:
            QMessageBox.information(self, "Warning", " ID cannot be empty")









