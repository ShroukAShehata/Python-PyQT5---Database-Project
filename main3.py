from PyQt5.QtWidgets  import *
from PyQt5.QtCore  import *
from PyQt5.QtGui  import *
import sys 
import os
import sqlite3

con = sqlite3.connect('WE School Students Database.db')
cursor = con.cursor()

#cursor.execute("CREATE TABLE Applicants ( Name VARCHAR(30), ID VARCHAR(20), Mail VARCHAR(30), Mobile VARCHAR(20), University VARCHAR(20), College VARCHAR(20), GraduationYear VARCHAR(20), Vacancy VARCHAR(30), CV VARCHAR(100) ) ")
#con.commit()

#cursor.execute("CREATE TABLE Results (NatID VARCHAR(20),State VARCHAR(30),  InterviewDate VARCHAR(30))")
#con.commit()
'''
cursor.execute("INSERT INTO Results VALUES ('','State','InterviewDate')")
cursor.execute("INSERT INTO Results VALUES ('1','Accepted','Sunday 9:00am')")
cursor.execute("INSERT INTO Results VALUES ('2','Not Accepted','No Interview')")
cursor.execute("INSERT INTO Results VALUES ('3','Accepted','Saturday 10:00am')")
cursor.execute("INSERT INTO Results VALUES ('4','Accepted','Saturday 10:00am')")
cursor.execute("INSERT INTO Results VALUES ('5','Accepted','Monday 10:00am')")
con.commit()
'''



class Main3(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("WE School Careers Form")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.Layouts()
        self.show()


    def UI(self):

        self.applytitle = QLabel("Apply Now")
        self.applytitle.setStyleSheet("color:blue; font-size:30pt; font-family:Arial Bold")

        self.namelbl = QLabel("Name")
        self.nameentry = QLineEdit()
        self.idlbl = QLabel("ID")
        self.identry = QLineEdit()
        self.maillbl = QLabel("Mail")
        self.mailentry = QLineEdit()
        self.mobilelbl = QLabel("Mobile")
        self.mobileentry = QLineEdit()
        self.universitylbl = QLabel("University")
        self.universityentry = QLineEdit()
        self.collegelbl = QLabel("College")
        self.collegeentry = QLineEdit()
        self.graduationlbl = QLabel("Graduation Year")
        self.graduationentry = QLineEdit()
        self.cvlbl = QLabel("Upload your cv")
        self.cventry = QLineEdit()
        self.cventry.setPlaceholderText("Insert google drive link for your cv")
        self.vacancylbl = QLabel("Vacancy")
        self.vacancy = QComboBox()
        self.vacancy.addItems(["","Coding/Programmer Teacher","Character Building Teacher","Technicl Drawing teacher","Physics teacher","PE teacher","Maths Teacher","English Teacher"])
        self.submitbtn = QPushButton("Submit")
        self.submitbtn.setStyleSheet("background-color:yellow;")
        self.submitbtn.clicked.connect(self.submitfunction)

        self.showtitle = QLabel("Check your state")
        self.showtitle.setStyleSheet("color:blue; font-size:22pt; font-family:Arial Bold")
        self.idresultlbl = QLabel("Enter Your Id")
        self.idresultentry = QLineEdit()
        self.showbtn = QPushButton("Show")
        self.showbtn.setStyleSheet("background-color:orange")
        self.showbtn.clicked.connect(self.showResult)
        self.resultlabel = QLabel("")
        self.resultlabel.setFont(QFont('Arial',20))
        self.resultlabel.setStyleSheet("color:blue")
        self.show()


    def Layouts(self):

        self.mainlayout = QVBoxLayout()
        self.toplayout = QFormLayout()
        self.bottomlayout = QVBoxLayout()

        self.mainlayout.addLayout(self.toplayout)
        self.mainlayout.addLayout(self.bottomlayout)

        self.toplayout.addRow(self.applytitle)
        self.toplayout.addRow(self.namelbl,self.nameentry)
        self.toplayout.addRow(self.idlbl, self.identry)
        self.toplayout.addRow(self.maillbl, self.mailentry)
        self.toplayout.addRow(self.mobilelbl, self.mobileentry)
        self.toplayout.addRow(self.universitylbl, self.universityentry)
        self.toplayout.addRow(self.collegelbl, self.collegeentry)
        self.toplayout.addRow(self.graduationlbl, self.graduationentry)
        self.toplayout.addRow(self.cvlbl, self.cventry)
        self.toplayout.addRow(self.vacancylbl, self.vacancy)
        self.toplayout.addRow(self.submitbtn)


        self.bottomlayout.addStretch()
        self.bottomlayout.addStretch()
        self.bottomlayout.addWidget(self.showtitle)
        self.bottomlayout.addWidget(self.idresultlbl)
        self.bottomlayout.addWidget(self.idresultentry)
        self.bottomlayout.addWidget(self.showbtn)
        self.bottomlayout.addStretch()
        self.bottomlayout.addWidget(self.resultlabel)
        self.bottomlayout.addStretch()


        self.setLayout(self.mainlayout)
        self.show()





    def submitfunction(self):
        if self.nameentry != "":
            name = self.nameentry.text()
            id = self.identry.text()
            mail = self.mailentry.text()
            mobile = self.mobileentry.text()
            university = self.universityentry.text()
            college = self.collegeentry.text()
            gradyear = self.graduationentry.text()
            job = self.vacancy.currentText()
            cv = self.cventry.text()

            if job is not None:
                cursor.execute("INSERT INTO Applicants VALUES(?,?,?,?,?,?,?,?,?)" , (name,id,mail,mobile,university,college,gradyear,job,cv))
                con.commit()
                QMessageBox.information(self,"Information","Applicant has been added")



    def showResult(self):

        Id = self.idresultentry.text()
        result = str(cursor.execute("SELECT * FROM Results WHERE NatID = ?",(Id,)).fetchone())
        self.resultlabel.setText(result)
        self.resultlabel.setStyleSheet("color:blue; border:1px solid blue")
        self.show()

'''
    def closeEvent(self, event):
        self.window = Window()
'''
       






