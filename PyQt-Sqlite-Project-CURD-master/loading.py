# from PyQt5 import QtGui
# from PyQt5.QtGui import QIcon, QPixmap
# from PyQt5.QtWidgets import QMainWindow, QProgressBar, QApplication, QLabel, QStatusBar, QPushButton
# import sys
# from indexres import *
# import indexres
# class SampleBar(QMainWindow):
#     def __init__(self, parent=None):
#         super(SampleBar, self).__init__(parent)
#         self.setMinimumSize(400, 100)
#         self.setWindowTitle("加载中，请稍后... ")
#         icon = QIcon()
#         icon.addPixmap(QPixmap('indexres/logo.jpg'))
#         # self.resize(1200, 750)
#         self.setStyleSheet("background-image: url(indexres/img.png);")
#         window_pale = QtGui.QPalette()
#         window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("indexres/img.png")))
#         self.statusBar = QStatusBar()
#         self.statusBar.setStyleSheet('QStatusBar::item {border: none;}')
#         self.setStatusBar(self.statusBar)
#         self.progressBar = QProgressBar()
#         self.label = QLabel()
#         self.label.setText("加载中，请稍后... ")
#         self.statusBar.addPermanentWidget(self.label, stretch=2)
#         self.statusBar.addPermanentWidget(self.progressBar, stretch=4)
#         self.progressBar.setRange(0, 100)
#         self.progressBar.setMinimum(0)
#         self.progressBar.setMaximum(0)
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = SampleBar()
#     main.setStyleSheet("#SampleBar{border-image:url(:/indexres/img.png)}")  # 这里使用相对路径，也可以使用绝对路径
#     main.show()
#     sys.exit(app.exec_())
import sys
from t_main import IndexWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, Qt, QThread
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QDialog, QApplication
from t_main import LoginDialog
import math


class LoadingWidget(QDialog):
    def __init__(self):
        super(LoadingWidget, self).__init__()
        # self.setupUi(self)
        self.offset = 0
        # 定时器
        self.startTimer(50)
        self.setFixedSize(150, 150)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Tool | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def timerEvent(self, evt):
        self.offset += 1
        if self.offset > 11:
            self.offset = 0
        self.update()

    def paintEvent(self, evt):
        painter = QPainter(self)
        # 动反锯齿
        painter.setRenderHint(QPainter.Antialiasing, True)
        width = self.width()
        height = self.height()
        painter.translate(width >> 1, height >> 1)

        offset_dest = (width - 30) / 2
        painter.setPen(QPen(Qt.NoPen))
        # 计算小圆坐标
        for i in range(3):
            point = QPoint(0, 0)
            painter.setBrush(QColor(50 + i * 50, 20 + i * 90, 40 + i * 5, 80 + i * 80))
            point.setX(offset_dest * math.sin((-self.offset + i) * math.pi / 6))
            point.setY(offset_dest * math.cos((-self.offset + i) * math.pi / 6))
            painter.drawEllipse(point.x() - 10, point.y() - 10, 20, 20)

        for i in range(9):
            point = QPoint(0, 0)
            painter.setBrush(QColor(255, 190 - i * 20, i * 15, 255 - i * 32))
            point.setX(offset_dest * math.sin((-self.offset + i + 3) * math.pi / 6))
            point.setY(offset_dest * math.cos((-self.offset + i + 3) * math.pi / 6))
            painter.drawEllipse(point.x() - 10, point.y() - 10, 20, 20)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder = LoadingWidget()
    recorder.show()
    sys.exit(app.exec_())

