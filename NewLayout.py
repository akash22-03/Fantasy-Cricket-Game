import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CricketEvaluation(object):
    def setupUi(self, CricketEvaluation):
        CricketEvaluation.setObjectName("CricketEvaluation")
        CricketEvaluation.resize(731, 731)
        self.frame = QtWidgets.QFrame(CricketEvaluation)
        self.frame.setGeometry(QtCore.QRect(0, 0, 731, 731))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 701, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("color:white; font-size:20px; font-weight:bold;background-color:none;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("background-color:white;")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color:white; font-size:20px; font-weight:bold;text-align: center; background-color:none;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet("background-color:white;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 620, 691, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton.setStyleSheet("color:white; font-size:20px; font-weight:bold;padding:10px;background-color:black;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.scorelabel = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.scorelabel.setStyleSheet("height:35px; background-color:white;font-size:20px;padding-left:10;font-weight:bold;")
        self.scorelabel.setObjectName("scorelabel")
        self.horizontalLayout_3.addWidget(self.scorelabel)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 260, 691, 311))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.listWidget.setStyleSheet("background-color:white;")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.listWidget_2.setStyleSheet("background-color:white;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_4.addWidget(self.listWidget_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 140, 691, 20))
        self.line.setStyleSheet("background-color:none;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(20, 230, 691, 20))
        self.line_2.setStyleSheet("background-color:none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(20, 590, 691, 20))
        self.line_3.setStyleSheet("background-color:none;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(100, 180, 74, 24))
        self.label_4.setStyleSheet("color:white; font-size:20px; font-weight:bold;text-align: center;background-color:none;")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(550, 170, 101, 51))
        self.label_3.setStyleSheet("color:white; font-size:20px; font-weight:bold;text-align: center;background-color:none;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 731, 731))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("back.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.label_4.raise_()
        self.label_3.raise_()

        self.retranslateUi(CricketEvaluation)
        QtCore.QMetaObject.connectSlotsByName(CricketEvaluation)
        
        #My Codes
        conn = sqlite3.connect('fantasycricket.db')
        sql="select name from teams"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.comboBox.addItem(row[0])        
        conn.close()

        self.pushButton.clicked.connect(self.calculate)
        
    def calculate(self):
        import sqlite3
        conn = sqlite3.connect('fantasycricket.db')
        team=self.comboBox.currentText()
        self.listWidget.clear()
        sqlq="select players, value from teams where name='"+team+"'"
        cur=conn.execute(sqlq)
        row=cur.fetchone()

        selected=row[0].split(',')

        self.listWidget.addItems(selected)
        teamttl=0

        self.listWidget_2.clear()
        match=self.comboBox_2.currentText()
        for i in range(self.listWidget.count()):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.listWidget.item(i).text()
            cursor=conn.execute("select * from "+match+" where player='"+nm+"'")
            row=cursor.fetchone()
            batscore=int(row[1]/2)
            if batscore>=50:
                batscore+=5
            if batscore>=100:
                batscore+=10
            if row[1]>0:
                sr=row[1]/row[2]
                if sr>=80 and sr<100:
                    batscore+=2
                if sr>=100:
                    batscore+=4
            batscore=batscore+row[3]
            batscore=batscore+2*row[4]
            bowlscore=row[8]*10
            if row[8]>=3:
                bowlscore=bowlscore+5
            if row[8]>=5:
                bowlscore=bowlscore=bowlscore+10
            if row[7]>0:
                er=6*row[7]/row[5]
                if er<=2:
                    bowlscore=bowlscore+10
                if er>2 and er<=3.5:
                    bowlscore=bowlscore+7
                if er>3.5 and er<=4.5:
                    bowlscore=bowlscore+4
            fieldscore=(row[9]+row[10]+row[11])*10            
            ttl=batscore+bowlscore+fieldscore
            self.listWidget_2.addItem(str(ttl))
            teamttl=teamttl+ttl
        self.scorelabel.setText(str(teamttl))
        
    def retranslateUi(self, CricketEvaluation):
        _translate = QtCore.QCoreApplication.translate
        CricketEvaluation.setWindowTitle(_translate("CricketEvaluation", "Form"))
        self.label.setText(_translate("CricketEvaluation", "Pick A Team "))
        self.label_2.setText(_translate("CricketEvaluation", "Pick A Match"))
        self.pushButton.setText(_translate("CricketEvaluation", "Calculate Score"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Match1"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Match2"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Match3"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Match4"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Match5"))
        self.scorelabel.setPlaceholderText(_translate("CricketEvaluation", "00"))
        self.label_4.setText(_translate("CricketEvaluation", "Players"))
        self.label_3.setText(_translate("CricketEvaluation", "Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CricketEvaluation = QtWidgets.QWidget()
    ui = Ui_CricketEvaluation()
    ui.setupUi(CricketEvaluation)
    CricketEvaluation.show()
    sys.exit(app.exec_())
