from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 706)
        MainWindow.setStyleSheet("background-color: #a6e7ff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 60, 911, 101))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 911, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.le1.setStyleSheet("border:none;")
        self.le1.setObjectName("le1")
        self.horizontalLayout.addWidget(self.le1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.le2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.le2.setStyleSheet("border:none;")
        self.le2.setObjectName("le2")
        self.horizontalLayout.addWidget(self.le2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.le3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.le3.setStyleSheet("border:none;")
        self.le3.setObjectName("le3")
        self.horizontalLayout.addWidget(self.le3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.le4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.le4.setStyleSheet("border:none;")
        self.le4.setObjectName("le4")
        self.horizontalLayout.addWidget(self.le4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 410, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 200, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(590, 200, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.le5 = QtWidgets.QLineEdit(self.centralwidget)
        self.le5.setGeometry(QtCore.QRect(230, 190, 113, 31))
        self.le5.setStyleSheet("border:none;")
        self.le5.setObjectName("le5")
        self.le6 = QtWidgets.QLineEdit(self.centralwidget)
        self.le6.setGeometry(QtCore.QRect(700, 190, 113, 31))
        self.le6.setStyleSheet("border:none;")
        self.le6.setObjectName("le6")
        self.horizontalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame_2.setGeometry(QtCore.QRect(100, 260, 321, 41))
        self.horizontalFrame_2.setStyleSheet("background-color:white;")
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb1 = QtWidgets.QRadioButton(self.horizontalFrame_2)
        self.rb1.setStyleSheet("background-color:white;\n"
"")
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_2.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.horizontalFrame_2)
        self.rb2.setStyleSheet("background-color:white;\n"
"")
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_2.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.horizontalFrame_2)
        self.rb3.setStyleSheet("background-color:white;\n"
"")
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_2.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.horizontalFrame_2)
        self.rb4.setStyleSheet("background-color:white;\n"
"")
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_2.addWidget(self.rb4)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 240, 361, 401))
        self.widget.setStyleSheet("background-color:white;")
        self.widget.setObjectName("widget")
        self.list1 = QtWidgets.QListWidget(self.widget)
        self.list1.setGeometry(QtCore.QRect(50, 70, 251, 321))
        self.list1.setStyleSheet("background-color:white;")
        self.list1.setObjectName("list1")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(570, 240, 371, 401))
        self.widget_2.setStyleSheet("background-color:white;")
        self.widget_2.setObjectName("widget_2")
        self.list2 = QtWidgets.QListWidget(self.widget_2)
        self.list2.setGeometry(QtCore.QRect(60, 50, 251, 341))
        self.list2.setStyleSheet("background-color:white;")
        self.list2.setObjectName("list2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(754, 260, 85, 16))
        self.label_9.setStyleSheet("background-color:white;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(670, 260, 70, 16))
        self.label_10.setStyleSheet("background-color:white;\n"
"")
        self.label_10.setObjectName("label_10")
        self.widget_2.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.widget.raise_()
        self.frame.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.le5.raise_()
        self.le6.raise_()
        self.horizontalFrame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuFile.addAction(self.actionNEW_Team)
        self.menuFile.addAction(self.actionOPEN_Team)
        self.menuFile.addAction(self.actionSAVE_Team)
        self.menuFile.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuFile.menuAction())

        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)

        self.rb1.toggled.connect(self.ctg)
        self.rb2.toggled.connect(self.ctg)
        self.rb3.toggled.connect(self.ctg)
        self.rb4.toggled.connect(self.ctg)
        
        self.menuFile.triggered[QtWidgets.QAction].connect(self.menufunction)
        
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.le1.setPlaceholderText(_translate("MainWindow", "##"))
        self.label_2.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.le2.setPlaceholderText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.le3.setPlaceholderText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Wicket-Keepers (WK)"))
        self.le4.setPlaceholderText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "Your Selections"))
        self.label_6.setText(_translate("MainWindow", ">"))
        self.label_7.setText(_translate("MainWindow", "Points Available"))
        self.label_8.setText(_translate("MainWindow", "Points Used"))
        self.le5.setPlaceholderText(_translate("MainWindow", "#####"))
        self.le6.setPlaceholderText(_translate("MainWindow", "#####"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.label_9.setText(_translate("MainWindow", "Displayed Here"))
        self.label_10.setText(_translate("MainWindow", "Team Name"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        
        
    def menufunction(self,action):
        txt = (action.text())
        if txt == 'NEW Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            text, ok = QtWidgets.QInputDialog.getText(MainWindow, 'Team', 'Enter name of Team: ')
            if ok:
                self.label_9.setText(str(text))
            self.show()
            
        if text == 'SAVE Team':
            count = self.list2.count()
            select=""
            for i in range(count):
                select = select + self.list2.item(i).text()
                if i < count-1:
                    select = select + ","
            self.saveTeam(self.label_9.text(),select,self.used)

        if text == 'OPEN Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            self.show()
            self.openTeam()


    def show(self):
        self.le1.setText(str(self.bat))
        self.le2.setText(str(self.bwl))
        self.le3.setText(str(self.ar))
        self.le4.setText(str(self.wk))
        self.le5.setText(str(self.avl))
        self.le6.setText(str(self.used))

    def saveTeam(self,name,players,value):
        if self.bat + self.bwl + self.ar + self.wk!=11:
            self.showdlg("Insufficient Players.!!")
            return
        sql = "INSERT INTO teams (Name, Players, Value) VALUES ('"+name+"','"+players+"','"+str(value)+"');"
        try:
            cur = cricket.execute(sql)
            self.showdlg("Team Saved Successfully")
            cricket.commit()
        except:
            self.showdlg("Error in Operation")
            cricket.rollback()

    def openTeam(self):
        sqlq1 = "SELECT Name FROM teams;"
        cur = cricket.execute(sqlq1)
        teams = []
        for row in cur:
            teams.append[row[0]]
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",teams,0,False)
        if ok and team:
            self.label_9.setText(team)
        sqlq2 = "SELECT Players,Value FROM teams WHERE Name='"+team+"';"
        cur = cricket.execute(sqlq2)
        row = cur.fetchone()
        select = row[0].split(',')
        self.list2.addItems(select)
        self.le6 = row[1]
        self.le5 = 1000 - row[1]
        count = self.list2.count()
        for i in range(count-1):
            player = self.list2.item(i).text()
            sql = "SELECT Ctg FROM stats WHERE Player = '"+player+"';"
            cur.execute(sql)
            row = cur.fetchone()
            category = row[0]
            if category == "BAT" :
                self.le1 = self.le1 + 1
            if category == "BWL":
                self.le2 = self.le2 + 1
            if category == "AR":
                self.le3 = self.le3 + 1
            if category == "WK":
                self.le4 = self.le4 + 1
        self.show()
        
        
    def showdlg(self,msg):
        Dialog = QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team")
        ret = Dialog.exec()

    def removelist1(self,item):
        category = ''
        if self.rb1.isChecked()==True:
            category = 'BAT'
        if self.rb2.isChecked()==True:
            category = 'BWL'
        if self.rb3.isChecked()==True:
            category = 'AR'
        if self.rb4.isChecked()==True:
            category = 'WK'
        ret = self.criteria(category, item)
        if ret == True:
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())
            self.show()
        
    def criteria(self,category,item):
        msg = ""
        if category=="BAT" and self.bat>=5:
            msg="You can not select more than 5 Batsmen"
        if category=="BWL" and self.bwl>=5:
            msg="You can not select more than 5 Bowlers"
        if category=="AR" and self.ar>=3:
            msg="You can not select more than 3 Allrounders"
        if category=="WK" and self.wk>=1:
            msg="You can not select more than 1 WicketKeeper"
        if msg!='':
            self.showdlg(msg)
            return False

        if self.avl<=0:
            msg = "You Have Exhausted Your Points"
            self.showdlg(msg)
            return False

        if category=="BAT":
            self.bat+=1
        if category=="BWL":
            self.bwl+=1
        if category=="AR":
            self.ar+=1
        if category=="WK":
            self.wk+=1

        sql = "SELECT Player, Value FROM stats WHERE Player = '"+item.text()+"';"
        cur = cricket.execute(sql)
        row = cur.fetchone()
        self.avl -= int(row[1])
        self.used += int(row[1])
        return True

    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        cur = cricket.execute("SELECT Player, Value, Ctg FROM stats WHERE Player = '"+item.text()+"';")
        row = cur.fetchone()
        self.avl = self.avl + int(row[1])
        self.used = self.used - int(row[1])
        category = row[2]
        if category=="BAT":
            self.bat-=1
            if self.rb1.isChecked()==True:
                self.list1.addItem(item.text())
        if category=="BWL":
            self.bwl-=1
            if self.rb2.isChecked()==True:
                self.list1.addItem(item.text())
        if category=="AR":
            self.ar-=1
            if self.rb3.isChecked()==True:
                self.list1.addItem(item.text())
        if category=="WK":
            self.wk-=1
            if self.rb4.isChecked()==True:
                self.list1.addItem(item.text())
        self.show()

    def ctg(self):
        category = ''
        if self.rb1.isChecked()==True:
            category='BAT'
        if self.rb2.isChecked()==True:
            category='BWL'
        if self.rb3.isChecked()==True:
            category='AR'
        if self.rb4.isChecked()==True:
            category='WK'
        self.fillList(category) 

    def fillList(self, category):
        self.list1.clear()
        sql = "SELECT Player FROM stats WHERE Ctg ='"+category+"';"
        cur = cricket.execute(sql)
        for row in cur:
            select = []
            for i in range(self.list2.count()):
                select.append(self.list2.item(i).text())
            if row[0] not in select:
                self.list1.addItem(row[0])

    
        
if __name__ == "__main__":
    import sqlite3 
    import sys
    cricket = sqlite3.connect('fantasycricket.db')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
