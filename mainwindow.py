# 5 14 1


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox

class Ui_FirstWindow((object)):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        ##icon = QtGui.QIcon()
        ##icon.addPixmap(QtGui.QPixmap(" "), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ##MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(30, 30, 431, 551))
        #self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap(""))
        #self.label.setScaledContents(True)
        #self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 30))
        self.menubar.setObjectName("menubar")
        self.menutools = QtWidgets.QMenu(self.menubar)
        self.menutools.setObjectName("menutools")
        self.menusettings = QtWidgets.QMenu(self.menubar)
        self.menusettings.setObjectName("menusettings")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionheight_calc1 = QtWidgets.QAction(MainWindow)
        self.actionheight_calc1.setObjectName("actionheight_calc1")
        
        
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        
        
        self.menutools.addAction(self.actionheight_calc1)
        self.menuhelp.addAction(self.actionabout)
        self.menubar.addAction(self.menutools.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.actionabout.triggered.connect(self.about_open)
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menutools.setTitle(_translate("MainWindow", "calculator"))
        self.menuhelp.setTitle(_translate("MainWindow", "about"))
        self.actionheight_calc1.setText(_translate("MainWindow", "height calc1"))
        self.actionheight_calc1.setStatusTip(_translate("MainWindow", "calculate height from free fall"))
        self.actionheight_calc1.setShortcut(_translate("MainWindow", "Ctrl+H, Ctrl+1"))
        self.actionabout.setText(_translate("MainWindow", "about"))

        
        
        
    
    def LoadSecondWindow(self):
        SecondWindow = QtWidgets.QMainWindow()
        ui = Ui_SecondWindow()
        ui.setupUi(SecondWindow)
        SecondWindow.show()
        
        
    
    def about_open(self):
        about = QMessageBox()
        about.setWindowTitle("about")
        about.setText("this is a simple calculator to calculate height based on an objects time in free fall with no air resistance")
        about.setIcon(QMessageBox.Information)
        about.setDetailedText("the formula is: gravitational acceleration divided by two times time in free fall squared, g/2 * T*T")
        a = about.exec_() 
         
        
class Ui_SecondWindow(object):
    
    num = 0.0
    g2 = 9.8
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 429)
        
        ##icon = QtGui.QIcon()
        ##icon.addPixmap(QtGui.QPixmap(" "), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ##MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 0, 501, 81))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(160, 210, 341, 91))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        
        self.startbutton = QtWidgets.QPushButton(self.centralwidget)
        self.startbutton.setGeometry(QtCore.QRect(10, 100, 251, 71))
        self.startbutton.setObjectName("startbutton")
        self.startbutton.clicked.connect(self.start_stopwatch)
        
        self.stopbutton = QtWidgets.QPushButton(self.centralwidget)
        self.stopbutton.setGeometry(QtCore.QRect(270, 100, 231, 71))
        self.stopbutton.setObjectName("stopbutton")
        self.stopbutton.clicked.connect(self.stop_stopwatch)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 200, 91, 111))
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 32))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startbutton.setText(_translate("MainWindow", "start"))
        self.stopbutton.setText(_translate("MainWindow", "stop"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">M:</span></p></body></html>"))



    def timeshow(self):
        self.num += 1
        self.lcdNumber.display(self.num/10)
        

    def start_stopwatch(self):
        self.lcdNumber_2.display(0)
        self.num = 0
        self.stopwatch = QtCore.QTimer()
        self.stopwatch.timeout.connect(self.timeshow)
        self.stopwatch.start(100)
        
       

    def stop_stopwatch(self):
        self.stopwatch.stop()
        self.lcdNumber_2.display(self.g2/2*(self.num/10)**2)
        
        
        
        
        
        
        
class Controller:

#init
    def Show_FirstWindow(self):
        self.FirstWindow = QtWidgets.QMainWindow()
        self.ui = Ui_FirstWindow()
        self.ui.setupUi(self.FirstWindow)
        self.ui.actionheight_calc1.triggered.connect(self.Show_SecondWindow)
        self.FirstWindow.show()

    def Show_SecondWindow(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.SecondWindow)
        self.SecondWindow.show()

   

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_FirstWindow()
    sys.exit(app.exec_())        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
