import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import time
from PyQt5.QtSql import *
class fullScreenVedioDialog(QDialog):
    add_pa_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(fullScreenVedioDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("全屏播放")

    def setUpUI(self):
        self.desktop = QApplication.desktop()
        self.resize(self.desktop.width(),self.desktop.height())
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # 播放器
        self.videowidget = QVideoWidget()
        self.player = QMediaPlayer()
        self.videowidget.resize(300, 300)
        self.player.setVideoOutput(self.videowidget)
        # 按钮
        self.btnlayout=QHBoxLayout()
        self.playBtn=QPushButton("播放")
        self.playBtn.clicked.connect(self.play)
        self.quitBtn=QPushButton("退出全屏")
        self.quitBtn.clicked.connect(self.quit)
        self.btnlayout.addWidget(self.playBtn)
        self.btnlayout.addWidget(self.quitBtn)

        # 添加进formlayout
        self.layout.addWidget(self.videowidget)
        self.layout.addLayout(self.btnlayout)

        qb = [self.playBtn, self.quitBtn]
        font = QtGui.QFont()
        font.setPointSize(15)  # 括号里的数字可以设置成自己想要的字体大小
        # font.setFamily("SimHei")  # 黑体
        font.setFamily("SimSun")  # 宋体
        for i in qb:
            i.setFixedSize(850, 35)
            i.setStyleSheet("QPushButton{\n"
                            "    background-color: rgb(170, 255, 127);\n"
                            "    color: rgb(81, 71, 81);\n"
                            "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                            "}\n"
                            "QPushButton:pressed{\n"
                            "    background:yellow;\n"
                            "}")
            i.setFont(font)

    def setMedia(self,path):
        media_path=path
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(media_path)))
    def play(self):
        self.player.setVolume(80)
        self.player.play()
    def quit(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    mainWindow = fullScreenVedioDialog()
    mainWindow.setMedia("pa_video/pa0_s0.mp4")
    # mainWindow.showFullScreen()
    mainWindow.show()
    mainWindow.play()
    sys.exit(app.exec_())