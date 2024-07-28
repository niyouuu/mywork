import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
from PyQt5.QtSql import *


class addPaDialog(QDialog):
    add_pa_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addPaDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("添加患者")

    def setUpUI(self):
        # self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  # 主题
        # self.setWindowOpacity(0.85)  # 设置透明度
        icon = QIcon()
        icon.addPixmap(QPixmap('logo.jpg'))
        self.setStyleSheet("    background-color: rgb(255,255,255);\n")
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        genderCategory = ["男", "女"]
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("  添加患者")
        self.paNameLabel = QLabel("姓    名:")
        self.birthLabel = QLabel("出生日期:")
        self.genderLabel = QLabel("性    别:")
        self.IdLabel = QLabel("身份证号:")
        self.historyLabel = QLabel("病    史:")
        self.paImageLabel = QLabel("照    片:")

        # button控件
        self.addBtn = QPushButton("添 加")
        self.backBtn = QPushButton("返 回")

        # lineEdit控件
        self.paNameEdit = QLineEdit()
        self.IdEdit = QLineEdit()
        self.historyEdit = QLineEdit()
        self.genderComboBox = QComboBox()
        self.genderComboBox.addItems(genderCategory)
        self.paImageEdit = QLineEdit()
        self.paImageEdit.setText("请稍后在*查看*界面进行拍照")
        self.paImageEdit.setEnabled(False)
        self.birthTime = QDateTimeEdit()
        self.birthTime.setDisplayFormat("yyyy-MM-dd")
        # self.birthEdit = QLineEdit()

        self.paNameEdit.setMaxLength(10)
        self.IdEdit.setMaxLength(18)
        self.paImageEdit.setMaxLength(255)

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.paNameLabel, self.paNameEdit)
        self.layout.addRow(self.IdLabel, self.IdEdit)
        self.layout.addRow(self.historyLabel, self.historyEdit)
        self.layout.addRow(self.genderLabel, self.genderComboBox)
        self.layout.addRow(self.paImageLabel, self.paImageEdit)
        self.layout.addRow(self.birthLabel, self.birthTime)
        self.layout.addRow("", self.addBtn)
        self.layout.addRow("", self.backBtn)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)
        self.paNameLabel.setFont(font)
        self.IdLabel.setFont(font)
        self.historyLabel.setFont(font)
        self.genderLabel.setFont(font)
        self.paImageLabel.setFont(font)
        self.birthLabel.setFont(font)

        self.paNameEdit.setFont(font)
        self.IdEdit.setFont(font)
        self.historyEdit.setFont(font)
        self.paImageEdit.setFont(font)
        self.birthTime.setFont(font)
        self.genderComboBox.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.addBtn.setFont(font)
        self.addBtn.setFixedHeight(32)
        self.addBtn.setFixedWidth(140)
        self.backBtn.setFont(font)
        self.backBtn.setFixedHeight(32)
        self.backBtn.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.addBtn.clicked.connect(self.addBtnCicked)
        self.backBtn.clicked.connect(self.close)

        lab = [self.addBtn, self.backBtn]
        tb = [self.paNameEdit, self.IdEdit, self.historyEdit,self.genderComboBox, self.paImageEdit, self.birthTime
              ]
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

    def addBtnCicked(self):
        paName = self.paNameEdit.text()
        paId = self.IdEdit.text()
        history = self.historyEdit.text()
        genderCategory = self.genderComboBox.currentText()
        paImage = ""
        birthTime = self.birthTime.text()
        if (
                paName == "" or paId == "" or history == "" or genderCategory == "" or birthTime == ""):
            #print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
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

            self.messageBox.setText('有字段为空，添加失败')

            self.messageBox.setStandardButtons(QMessageBox.Yes)

            buttonY = self.messageBox.button(QMessageBox.Yes)

            buttonY.setText('确认')

            self.messageBox.exec_()

            return
        else:
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('database.db')
            db.open()
            query = QSqlQuery()
            # 如果已存在，则update Book表的现存量，剩余可借量，不存在，则insert Book表，同时insert buyordrop表
            sql = "SELECT * FROM patient WHERE pa_id='%s'" % (paId)
            query.exec_(sql)
            if (query.next()):
                # print(QMessageBox.warning(self, "警告", "该患者已存在", QMessageBox.Yes, QMessageBox.Yes))
                # return
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

                self.messageBox.setText('该患者已存在，无需添加')

                self.messageBox.setStandardButtons(QMessageBox.Yes)

                buttonY = self.messageBox.button(QMessageBox.Yes)

                buttonY.setText('确认')

                self.messageBox.exec_()

                return
                # 提示已存在
            else:
                sql = "INSERT INTO patient(pa_name,pa_id,pa_history,pa_gender,pa_photo,pa_age) VALUES ('%s','%s','%s','%s','%s','%s')" % (
                    paName, paId, history, genderCategory, paImage, birthTime)
            query.exec_(sql)
            db.commit()
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

            self.messageBox.setText('添加患者成功！')

            self.messageBox.setStandardButtons(QMessageBox.Yes)

            buttonY = self.messageBox.button(QMessageBox.Yes)

            buttonY.setText('确认')

            self.messageBox.exec_()
            # print(QMessageBox.information(self, "提示", "添加患者成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.add_pa_success_signal.emit()
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.paNameEdit.clear()
        self.IdEdit.clear()
        self.historyEdit.clear()
        self.paImageEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = addPaDialog()
    mainMindow.show()
    sys.exit(app.exec_())