from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 398)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.Shutdown.setGeometry(QtCore.QRect(10, 90, 103, 37))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Shutdown.setFont(font)
        self.Shutdown.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Shutdown.setObjectName("Shutdown")
        self.Restart = QtWidgets.QPushButton(self.centralwidget)
        self.Restart.setGeometry(QtCore.QRect(180, 90, 103, 37))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Restart.setFont(font)
        self.Restart.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Restart.setObjectName("Restart")
        self.Hibernate = QtWidgets.QPushButton(self.centralwidget)
        self.Hibernate.setGeometry(QtCore.QRect(360, 90, 103, 37))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Hibernate.setFont(font)
        self.Hibernate.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Hibernate.setObjectName("Hibernate")
        self.Log_Off = QtWidgets.QPushButton(self.centralwidget)
        self.Log_Off.setGeometry(QtCore.QRect(540, 90, 103, 37))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Log_Off.setFont(font)
        self.Log_Off.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Log_Off.setObjectName("Log_Off")
        self.Command_Enter = QtWidgets.QLineEdit(self.centralwidget)
        self.Command_Enter.setGeometry(QtCore.QRect(10, 170, 191, 33))
        self.Command_Enter.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Command_Enter.setObjectName("Command_Enter")
        self.Run_Command = QtWidgets.QPushButton(self.centralwidget)
        self.Run_Command.setGeometry(QtCore.QRect(230, 170, 151, 37))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Run_Command.setFont(font)
        self.Run_Command.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Run_Command.setObjectName("Run_Command")
        self.Help = QtWidgets.QTextBrowser(self.centralwidget)
        self.Help.setGeometry(QtCore.QRect(5, 241, 681, 151))
        self.Help.setStyleSheet("background-color: rgb(0, 4, 255);\n"
"color: rgb(255, 255, 255);")
        self.Help.setObjectName("Help")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Shutdown.clicked.connect(self.Shutdownco)
        self.Restart.clicked.connect(self.restartco)
        self.Log_Off.clicked.connect(self.Log_Offco)
        self.Hibernate.clicked.connect(self.Hibernateco)
        self.Run_Command.clicked.connect(self.Advanced)
        self.Help.append('Usage: shutdown [/i | /l | /s | /sg | /r | /g | /a | /p | /h | /e | /o] [/hybrid] [/soft] [/fw] [/f]\n\
[/m \\computer][/t xxx][/d [p|u:]xx:yy [/c "comment"]]\n\
\n\
    No args    Display help. This is the same as typing /?.\n\
    /?         Display help. This is the same as not typing any options.\n\
    /i         Display the graphical user interface (GUI).\n\
               This must be the first option.\n\
    /l         Log off. This cannot be used with /m or /d options.\n\
    /s         Shutdown the computer.\n\
    /sg        Shutdown the computer. On the next boot, if Automatic Restart Sign-On\n\
               is enabled, automatically sign in and lock last interactive user.\n\
               After sign in, restart any registered applications.\n\
    /r         Full shutdown and restart the computer.\n\
    /g         Full shutdown and restart the computer. After the system is rebooted,\n\
               if Automatic Restart Sign-On is enabled, automatically sign in and\n\
               lock last interactive user.\n\
               After sign in, restart any registered applications.\n\
    /a         Abort a system shutdown.\n\
               This can only be used during the time-out period.\n\
               Combine with /fw to clear any pending boots to firmware.\n\
    /p         Turn off the local computer with no time-out or warning.\n\
               Can be used with /d and /f options.\n\
    /h         Hibernate the local computer.\n\
               Can be used with the /f option.\n\
    /hybrid    Performs a shutdown of the computer and prepares it for fast startup.\n\
               Must be used with /s option.\n\
    /fw        Combine with a shutdown option to cause the next boot to go to the\n\
               firmware user interface.\n\
    /e         Document the reason for an unexpected shutdown of a computer.\n\
    /o         Go to the advanced boot options menu and restart the computer.\n\
               Must be used with /r option.\n\
    /m \\computer Specify the target computer.\n\
    /t xxx     Set the time-out period before shutdown to xxx seconds.\n\
               The valid range is 0-315360000 (10 years), with a default of 30.\n\
               If the timeout period is greater than 0, the /f parameter is\n\
               implied.\n\
    /c "comment" Comment on the reason for the restart or shutdown.\n\
               Maximum of 512 characters allowed.\n\
    /f         Force running applications to close without forewarning users.\n\
               The /f parameter is implied when a value greater than 0 is\n\
               specified for the /t parameter.\n\
    /d [p|u:]xx:yy  Provide the reason for the restart or shutdown.\n\
               p indicates that the restart or shutdown is planned.\n\
               u indicates that the reason is user defined.\n\
               If neither p nor u is specified the restart or shutdown is\n\
               unplanned.\n\
               xx is the major reason number (positive integer less than 256).\n\
               yy is the minor reason number (positive integer less than 65536).\n\
\n\
Reasons on this computer:\n\
(E = Expected U = Unexpected P = planned, C = customer defined)')
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Shutdown.setText(_translate("MainWindow", "Shutdown"))
        self.Restart.setText(_translate("MainWindow", "Restart"))
        self.Hibernate.setText(_translate("MainWindow", "Hibernate"))
        self.Log_Off.setText(_translate("MainWindow", "Log Off"))
        self.Command_Enter.setText(_translate("MainWindow", "shutdown"))
        self.Run_Command.setText(_translate("MainWindow", "Run Command"))
    def Shutdownco(self):
        os.system('shutdown /l /s')
    def restartco(self):
        os.system('shutdown \l /r')
    def Log_Offco(self):
        os.system('shutdown \l')
    def Hibernateco(self):
        os.system('shutdown /h')
    def Advanced(self):
        comtext=self.Command_Enter.text()
        os.system(comtext)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
