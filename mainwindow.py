

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/testkochock2fdsjjqwertyuioupudupulipadiksimontareweqwertapi.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 431, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("backgroundimagemainwindowj.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
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
        self.actionheight_calc2 = QtWidgets.QAction(MainWindow)
        self.actionheight_calc2.setObjectName("actionheight_calc2")
        self.actionstone_velocity = QtWidgets.QAction(MainWindow)
        self.actionstone_velocity.setObjectName("actionstone_velocity")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionsettings = QtWidgets.QAction(MainWindow)
        self.actionsettings.setObjectName("actionsettings")
        self.actionsettings_1 = QtWidgets.QAction(MainWindow)
        self.actionsettings_1.setObjectName("actionsettings_1")
        self.menutools.addAction(self.actionheight_calc1)
        self.menutools.addAction(self.actionheight_calc2)
        self.menutools.addAction(self.actionstone_velocity)
        self.menusettings.addAction(self.actionsettings_1)
        self.menuhelp.addAction(self.actionhelp)
        self.menuhelp.addAction(self.actionabout)
        self.menubar.addAction(self.menutools.menuAction())
        self.menubar.addAction(self.menusettings.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.actionabout.triggered.connect(self.about_open)
        
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menutools.setTitle(_translate("MainWindow", "tools"))
        self.menusettings.setTitle(_translate("MainWindow", "settings"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionheight_calc1.setText(_translate("MainWindow", "height calc1"))
        self.actionheight_calc1.setStatusTip(_translate("MainWindow", "calculate height from free fall"))
        self.actionheight_calc1.setShortcut(_translate("MainWindow", "Ctrl+H, Ctrl+1"))
        self.actionheight_calc2.setText(_translate("MainWindow", "height calc2"))
        self.actionheight_calc2.setStatusTip(_translate("MainWindow", "calculate height for free fall up and down"))
        self.actionheight_calc2.setShortcut(_translate("MainWindow", "Ctrl+H, Ctrl+2"))
        self.actionstone_velocity.setText(_translate("MainWindow", "stone velocity"))
        self.actionstone_velocity.setStatusTip(_translate("MainWindow", "how fast can you throw a stone"))
        self.actionstone_velocity.setShortcut(_translate("MainWindow", "Ctrl+S, Ctrl+V"))
        self.actionhelp.setText(_translate("MainWindow", "help"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionsettings.setText(_translate("MainWindow", "settings"))
        self.actionsettings_1.setText(_translate("MainWindow", "settings 1"))
        self.actionsettings_1.setStatusTip(_translate("MainWindow", "configure owgendi"))
        self.actionsettings_1.setShortcut(_translate("MainWindow", "Ctrl+S, Ctrl+1"))
        
    def about_open(self):
        about = QMessageBox()
        about.setWindowTitle("about")
        about.setText("this is a simple calculator to calculate height based on an objects time in free fall with no air resistance")
        about.setIcon(QMessageBox.Information)
        about.setDetailedText("the formula is: gravitational acceleration divided by two times time in free fall squared, g/2 * T*T")
        a = about.exec_() 
         








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
