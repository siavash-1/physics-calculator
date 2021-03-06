#
from PyQt5 import QtCore, QtGui, QtWidgets 
import sys


class Ui_MainWindow(object):
    
    num = 0.0
    g2 = 9.8
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 429)
        
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(""), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #MainWindow.setWindowIcon(icon)
        
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
        
    
    
    
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
