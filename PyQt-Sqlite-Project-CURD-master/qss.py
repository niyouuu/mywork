# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'designerzVsldB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 751, 551))
        self.frame.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(40, 110, 241, 251))
        self.frame_3.setStyleSheet(u"background-color: rgb(170, 170, 127);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(320, 110, 241, 251))
        self.frame_4.setStyleSheet(u"background-color: rgb(170, 170, 127);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 460, 751, 91))
        self.label.setStyleSheet(u"font: 28pt \"3DS Fonticon\";")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(580, 110, 161, 61))
        self.pushButton.setStyleSheet(u"font: 14pt \"3DS Fonticon\";\n"
"background-color: rgb(244, 138, 0);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(580, 210, 161, 61))
        self.pushButton_2.setStyleSheet(u"font: 14pt \"3DS Fonticon\";\n"
"background-color: rgb(244, 138, 0);")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(580, 300, 161, 61))
        self.pushButton_3.setStyleSheet(u"font: 14pt \"3DS Fonticon\";\n"
"background-color: rgb(244, 138, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"                 \u672a\u4fdd\u5b58", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u672c\u5730\u5bfc\u5165\u7167\u7247", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u7167", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5e76\u88c1\u526a\u7167\u7247", None))
    # retranslateUi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.showFullScreen()
    # window.searchButtonClicked()
    sys.exit(app.exec_())

