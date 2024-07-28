import os
import shutil
import sys

from PyQt5 import QtWidgets
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
from PyQt5.QtSql import *


class addwordDialog(QDialog):
    add_word_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addwordDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("添加配对词语")
        self.imagepath = "" # 图片

    def setUpUI(self):
        icon = QIcon()
        icon.addPixmap(QPixmap('logo.jpg'))
        # self.setStyleSheet("    background-color: rgb(255,255,255);\n")
        self.resize(600, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # 标题
        self.titlelabel = QLabel("添加词语")
        # 内容
        self.wordNameLabel = QLabel("词语名:")
        self.audio_path_label = QLabel("音频文件:")
        # lineEdit控件
        self.strNameEdit = QLineEdit()
        self.strNameEdit.setMaxLength(10)

        # 录音相关
        from standard_audio import StandardAudioRecorder
        self.vbox = QVBoxLayout()
        self.audiorecorder = StandardAudioRecorder()
        self.audiorecorder.generate_clicked.connect(self.setAudioText)
        self.audiorecorder.audio_clicked.connect(self.setGenerateLabel)
        self.vbox.addWidget(self.audiorecorder)

        self.audiopack_widget = QWidget()
        self.audiopack_widget.setLayout(self.vbox)

        self.generate_label = QLabel("尚未选择音频")
        self.imageBtn = QPushButton("上传图片")# 图片
        self.imageBtn.clicked.connect(self.imageBtnClicked)
        self.imagelabel = QLabel()
        # 提交
        self.addBtn = QPushButton("添 加")
        self.addBtn.clicked.connect(self.addBtnClicked)

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.wordNameLabel,self.strNameEdit)

        self.layout.addRow(self.audio_path_label,self.generate_label)
        self.layout.addRow("",self.audiopack_widget)
        self.layout.addRow("词语图片：",self.imageBtn)# 图片
        self.layout.addRow("",self.imagelabel)
        self.layout.addRow("", self.addBtn)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)
        self.wordNameLabel.setFont(font)
        self.strNameEdit.setFont(font)
        self.audio_path_label.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.addBtn.setFont(font)
        self.addBtn.setFixedHeight(32)
        self.addBtn.setFixedWidth(600)

        # 设置间距
        self.titlelabel.setMargin(8)

        lab = [self.addBtn,self.imageBtn]
        tb = [self.strNameEdit]
        # font = QtGui.QFont()
        # font.setPointSize(15)  # 括号里的数字可以设置成自己想要的字体大小
        # # font.setFamily("SimHei")  # 黑体
        # font.setFamily("SimSun")  # 宋体
        for i in lab:
            i.setStyleSheet("QPushButton{\n"
                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"
                            "    color:white;\n"
                            "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 5px;font-family: 微软雅黑;\n"
                            "}\n"
                            "QPushButton:pressed{\n"
                            "    background:black;\n"
                            "}")
            i.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
            font.setPixelSize(16)
            i.setFont(font)
            i.setFixedHeight(33)
            # i.setFixedWidth(800)
        for i in tb:
            i.setStyleSheet("border:2px solid rgb(186,186,186);\n"
                            "border-radius:10px\n"
                            "")

    def addBtnClicked(self):
        try:
            wordName =self.strNameEdit.text()

            if (wordName == "" ):
                self.messageBox = QMessageBox()
                icon = QIcon()
                icon.addPixmap(QPixmap('logo.jpg'))
                self.messageBox.setWindowIcon(icon)
                self.messageBox.setStyleSheet("QMessageBox {\n"
                                              "    border-radius:3px;\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"

                                              "}\n"
                                              "\n"
                                              "QMessageBox QLabel { \n"
                                              "    color: #298DFF;\n"
                                              "    background-color: transparent;\n"
                                              "    min-width: 240px;\n"
                                              "    min-height: 40px; \n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QLabel {\n"
                                              "    width: 40px;\n"
                                              "    height: 40px; \n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton { \n"
                                              "    border: 1px solid #298DFF;\n"
                                              "    border-radius: 3px;\n"
                                              "    background-color: #F2F2F2;\n"
                                              "    color: #298DFF;\n"
                                              "    font-family: \"Microsoft YaHei\";\n"
                                              "    font-size: 10pt;\n"
                                              "    min-width: 70px;\n"
                                              "    min-height: 25px;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton:hover {\n"
                                              "    background-color: #298DFF;\n"
                                              "    color: #F2F2F2;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton:pressed {\n"
                                              "    background-color: #257FE6;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QDialogButtonBox#qt_msgbox_buttonbox { \n"
                                              "    button-layout: 0; \n"
                                              "}\n"
                                              "")

                self.messageBox.setWindowTitle('提示')
                font = QFont()
                font.setPixelSize(20)
                self.messageBox.setFont(font)

                self.messageBox.setText('有字段为空，修改失败')

                self.messageBox.setStandardButtons(QMessageBox.Yes)

                buttonY = self.messageBox.button(QMessageBox.Yes)

                buttonY.setText('确认')

                self.messageBox.exec_()
                # print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
                return
            elif not os.path.exists("audio/temp_save_audio.mp3"):
                self.messageBox = QMessageBox()
                icon = QIcon()
                icon.addPixmap(QPixmap('logo.jpg'))
                self.messageBox.setWindowIcon(icon)
                self.messageBox.setStyleSheet("QMessageBox {\n"
                                              "    border-radius:3px;\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"

                                              "}\n"
                                              "\n"
                                              "QMessageBox QLabel { \n"
                                              "    color: #298DFF;\n"
                                              "    background-color: transparent;\n"
                                              "    min-width: 240px;\n"
                                              "    min-height: 40px; \n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QLabel {\n"
                                              "    width: 40px;\n"
                                              "    height: 40px; \n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton { \n"
                                              "    border: 1px solid #298DFF;\n"
                                              "    border-radius: 3px;\n"
                                              "    background-color: #F2F2F2;\n"
                                              "    color: #298DFF;\n"
                                              "    font-family: \"Microsoft YaHei\";\n"
                                              "    font-size: 10pt;\n"
                                              "    min-width: 70px;\n"
                                              "    min-height: 25px;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton:hover {\n"
                                              "    background-color: #298DFF;\n"
                                              "    color: #F2F2F2;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton:pressed {\n"
                                              "    background-color: #257FE6;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QDialogButtonBox#qt_msgbox_buttonbox { \n"
                                              "    button-layout: 0; \n"
                                              "}\n"
                                              "")

                self.messageBox.setWindowTitle('提示')
                font = QFont()
                font.setPixelSize(20)
                self.messageBox.setFont(font)

                self.messageBox.setText('请选择一条音频')

                self.messageBox.setStandardButtons(QMessageBox.Yes)

                buttonY = self.messageBox.button(QMessageBox.Yes)

                buttonY.setText('确认')

                self.messageBox.exec_()
                # print(QMessageBox.warning(self, "警告", "请选择一条音频", QMessageBox.Yes, QMessageBox.Yes))
                return
            else:
                db = QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName('database.db')
                db.open()
                query = QSqlQuery()
                # 如果已存在，则update Book表的现存量，剩余可借量，不存在，则insert Book表，同时insert buyordrop表
                sql = "SELECT * FROM pdwords WHERE pdword_name='%s'" % (wordName)
                query.exec_(sql)
                if (query.next()):
                    self.messageBox = QMessageBox()
                    icon = QIcon()
                    icon.addPixmap(QPixmap('logo.jpg'))
                    self.messageBox.setWindowIcon(icon)
                    self.messageBox.setStyleSheet("QMessageBox {\n"
                                                  "    border-radius:3px;\n"
                                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"

                                                  "}\n"
                                                  "\n"
                                                  "QMessageBox QLabel { \n"
                                                  "    color: #298DFF;\n"
                                                  "    background-color: transparent;\n"
                                                  "    min-width: 240px;\n"
                                                  "    min-height: 40px; \n"
                                                  "}\n"
                                                  "\n"
                                                  "QMessageBox QLabel {\n"
                                                  "    width: 40px;\n"
                                                  "    height: 40px; \n"
                                                  "}\n"
                                                  "\n"
                                                  "QMessageBox QPushButton { \n"
                                                  "    border: 1px solid #298DFF;\n"
                                                  "    border-radius: 3px;\n"
                                                  "    background-color: #F2F2F2;\n"
                                                  "    color: #298DFF;\n"
                                                  "    font-family: \"Microsoft YaHei\";\n"
                                                  "    font-size: 10pt;\n"
                                                  "    min-width: 70px;\n"
                                                  "    min-height: 25px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QMessageBox QPushButton:hover {\n"
                                                  "    background-color: #298DFF;\n"
                                                  "    color: #F2F2F2;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QMessageBox QPushButton:pressed {\n"
                                                  "    background-color: #257FE6;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QMessageBox QDialogButtonBox#qt_msgbox_buttonbox { \n"
                                                  "    button-layout: 0; \n"
                                                  "}\n"
                                                  "")

                    self.messageBox.setWindowTitle('提示')
                    font = QFont()
                    font.setPixelSize(20)
                    self.messageBox.setFont(font)

                    self.messageBox.setText('词语名已存在')

                    self.messageBox.setStandardButtons(QMessageBox.Yes)

                    buttonY = self.messageBox.button(QMessageBox.Yes)

                    buttonY.setText('确认')

                    self.messageBox.exec_()
                    # print(QMessageBox.warning(self, "警告", "词语名已存在", QMessageBox.Yes, QMessageBox.Yes))
                    return
                # 分两步，1保存并获取自增编号，2修改音频路径
                sql = "INSERT INTO pdwords(pdword_name,pdword_audio,pdword_image) VALUES ('%s','%s','%s');" % (
                    wordName, "audio_path","pic/"+wordName+".jpg")
                query.exec_(sql)
                db.commit()
                query.exec_("SELECT last_insert_rowid();")
                print(query.next())
                #得知自增编号
                new_word_id = query.value(0)
                wordAudio = "audio/pdword/"+str(new_word_id)+".mp3"
                wordImage="pic/"+str(new_word_id)+".jpg"
                sql = "UPDATE pdwords SET pdword_audio='%s',pdword_image='%s' WHERE pdword_no=%d" % (wordAudio,wordImage, new_word_id)
                query.exec_(sql)
                db.commit()
                target_path="audio/pdword"
                new_name = str(new_word_id)+".mp3"
                self.transAudio(target_path,new_name)#将save_temp_audio.mp3改名并剪切到目标路径
                if not self.imagepath=="":# 图像
                    new_name = str(new_word_id)+".jpg"
                    self.copyImage(new_name)
                self.messageBox = QMessageBox()
                icon = QIcon()
                icon.addPixmap(QPixmap('logo.jpg'))
                self.messageBox.setWindowIcon(icon)
                self.messageBox.setStyleSheet("QMessageBox {\n"
                                              "    border-radius:3px;\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"

                                              "}\n"
                                              "\n"
                                              "QMessageBox QLabel { \n"
                                              "    color: #298DFF;\n"
                                              "    background-color: transparent;\n"
                                              "    min-width: 240px;\n"
                                              "    min-height: 40px; \n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QLabel {\n"
                                              "    width: 40px;\n"
                                              "    height: 40px; \n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton { \n"
                                              "    border: 1px solid #298DFF;\n"
                                              "    border-radius: 3px;\n"
                                              "    background-color: #F2F2F2;\n"
                                              "    color: #298DFF;\n"
                                              "    font-family: \"Microsoft YaHei\";\n"
                                              "    font-size: 10pt;\n"
                                              "    min-width: 70px;\n"
                                              "    min-height: 25px;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton:hover {\n"
                                              "    background-color: #298DFF;\n"
                                              "    color: #F2F2F2;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton:pressed {\n"
                                              "    background-color: #257FE6;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QDialogButtonBox#qt_msgbox_buttonbox { \n"
                                              "    button-layout: 0; \n"
                                              "}\n"
                                              "")

                self.messageBox.setWindowTitle('提示')
                font = QFont()
                font.setPixelSize(20)
                self.messageBox.setFont(font)

                self.messageBox.setText('添加词语成功！')

                self.messageBox.setStandardButtons(QMessageBox.Yes)

                buttonY = self.messageBox.button(QMessageBox.Yes)

                buttonY.setText('确认')

                self.messageBox.exec_()
                # print(QMessageBox.information(self, "提示", "添加词语成功!", QMessageBox.Yes, QMessageBox.Yes))
                self.add_word_success_signal.emit()
                self.close()
                self.clearEdit()
            return
        except Exception as e:
            print(f'Error: {e}')

    def clearEdit(self):
       self.strNameEdit.clear()

    # 将temp_save_audio.mp3剪切到对应的音频文件夹下保存
    def transAudio(self, target_path,new_name):
        try:
            # 目标文件夹
            source_path = "audio"
            audio_name ="temp_save_audio.mp3"
            if not os.path.exists(os.path.join(source_path, audio_name)):
                # print(QMessageBox.warning(self, "警告", "请选择一条音频", QMessageBox.Yes, QMessageBox.Yes))
                self.messageBox = QMessageBox()
                icon = QIcon()
                icon.addPixmap(QPixmap('logo.jpg'))
                self.messageBox.setWindowIcon(icon)
                self.messageBox.setStyleSheet("QMessageBox {\n"
                                              "    border-radius:3px;\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"

                                              "}\n"
                                              "\n"
                                              "QMessageBox QLabel { \n"
                                              "    color: #298DFF;\n"
                                              "    background-color: transparent;\n"
                                              "    min-width: 240px;\n"
                                              "    min-height: 40px; \n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QLabel {\n"
                                              "    width: 40px;\n"
                                              "    height: 40px; \n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton { \n"
                                              "    border: 1px solid #298DFF;\n"
                                              "    border-radius: 3px;\n"
                                              "    background-color: #F2F2F2;\n"
                                              "    color: #298DFF;\n"
                                              "    font-family: \"Microsoft YaHei\";\n"
                                              "    font-size: 10pt;\n"
                                              "    min-width: 70px;\n"
                                              "    min-height: 25px;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton:hover {\n"
                                              "    background-color: #298DFF;\n"
                                              "    color: #F2F2F2;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QPushButton:pressed {\n"
                                              "    background-color: #257FE6;\n"
                                              "}\n"
                                              "\n"
                                              "QMessageBox QDialogButtonBox#qt_msgbox_buttonbox { \n"
                                              "    button-layout: 0; \n"
                                              "}\n"
                                              "")

                self.messageBox.setWindowTitle('提示')
                font = QFont()
                font.setPixelSize(20)
                self.messageBox.setFont(font)

                self.messageBox.setText('请选择一条音频')

                self.messageBox.setStandardButtons(QMessageBox.Yes)

                buttonY = self.messageBox.button(QMessageBox.Yes)

                buttonY.setText('确认')

                self.messageBox.exec_()
            if not os.path.exists(target_path):
                os.makedirs(target_path)  # 如果文件夹不存在，则创建文件夹
            # 将音频重命名为new_name
            os.rename(os.path.join(source_path, audio_name), os.path.join(source_path, new_name))
            # 将音频复制到目标路径下，source_path包含文件名及后缀名，video_name是其中分离出的文件名
            shutil.move(os.path.join(source_path, new_name), os.path.join(target_path, new_name))
        except Exception as e:
            print(f'Error: {e}')

    def get_str_name_edit(self):
        return self.strNameEdit

    def setAudioText(self):
        self.audiorecorder.set_text_str(self.strNameEdit.text())

    def setGenerateLabel(self):
        self.generate_label.setText("已选中音频文件")

    def imageBtnClicked(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open jpg file", "", "jpg Files (*.jpg)")
        self.imagepath=file_path
        if self.imagepath:
            # Set the pixmap content of the label
            pixmap = QPixmap(self.imagepath)
            scaled_pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.imagelabel.setPixmap(scaled_pixmap)
            self.imagelabel.setScaledContents(True)
    # 复制图片
    def copyImage(self,new_name):
        try:
            source_path=self.imagepath
            # 目标文件夹
            image_name = os.path.basename(source_path)  # 包含后缀名
            target_path = "pic"
            if not os.path.exists(target_path):
                os.makedirs(target_path)  # 如果文件夹不存在，则创建文件夹
            # 将音频复制到目标路径下，source_path包含文件名及后缀名，image_name是其中分离出的文件名
            shutil.copy(source_path, os.path.join(target_path, image_name))
            if os.path.exists(os.path.join(target_path, new_name)):
                os.remove(os.path.join(target_path, new_name))
            # 将音频重命名为new_name.jpg
            os.rename(os.path.join(target_path, image_name), os.path.join(target_path, new_name))
        except Exception as e:
            print(f'Error: {e}')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = addwordDialog()
    mainMindow.show()
    sys.exit(app.exec_())