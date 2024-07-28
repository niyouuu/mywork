import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
from PyQt5.QtSql import *


class addUserDialog(QDialog):
    add_user_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addUserDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("添加用户")

    def setUpUI(self):
        # self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  # 主题
        # self.setWindowOpacity(0.7)  # 设置透明度
        # self.setStyleSheet("    background-color: rgb(255,255,255);\n")
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        icon = QIcon()
        icon.addPixmap(QPixmap('logo.jpg'))
        self.setStyleSheet("    background-color: rgb(255,255,255);\n")
        permCategory = ["管理员", "普通用户"]
        self.resize(300, 300)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("添加用户")
        self.userNameLabel = QLabel("用 户 名:")
        self.permLabel = QLabel("权    限:")
        self.pwLabel = QLabel("密    码:")

        # button控件
        self.addBtn = QPushButton("添 加")
        self.backBtn = QPushButton("返 回")

        # lineEdit控件
        self.userNameEdit = QLineEdit()
        self.pwEdit = QLineEdit()
        self.historyEdit = QLineEdit()
        self.permComboBox = QComboBox()
        self.permComboBox.addItems(permCategory)
        self.userImageEdit = QLineEdit()

        self.userNameEdit.setMaxLength(10)
        self.pwEdit.setMaxLength(18)
        self.userImageEdit.setMaxLength(255)

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.userNameLabel, self.userNameEdit)
        self.layout.addRow(self.pwLabel, self.pwEdit)
        self.layout.addRow(self.permLabel, self.permComboBox)
        self.layout.addRow("", self.addBtn)
        self.layout.addRow("", self.backBtn)

        # 设置字体
        font = QFont()
        font.setPixelSize(22)
        self.titlelabel.setFont(font)
        font.setPixelSize(16)
        self.userNameLabel.setFont(font)
        self.pwLabel.setFont(font)
        self.permLabel.setFont(font)

        self.userNameEdit.setFont(font)
        self.pwEdit.setFont(font)
        self.permComboBox.setFont(font)

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
#        self.layout.setVerticalSusercing(10)

        self.addBtn.clicked.connect(self.addBtnCicked)
        self.backBtn.clicked.connect(self.close)

        lab = [self.addBtn,self.backBtn]
        tb = [self.userNameEdit, self.pwEdit, self.permComboBox
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
        userName = self.userNameEdit.text()
        userPw = self.pwEdit.text()
        if(self.permComboBox.currentText()=="管理员"):
            permCategory = 0
        elif(self.permComboBox.currentText()=="普通用户"):
            permCategory = 1

        if (
                userName == "" or userPw == "" or permCategory == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('database.db')
            db.open()
            query = QSqlQuery()
            # 如果已存在，则update Book表的现存量，剩余可借量，不存在，则insert Book表，同时insert buyordrop表
            sql = "SELECT * FROM users WHERE user_name='%s'" % (userName)
            query.exec_(sql)
            if (query.next()):
                print(QMessageBox.warning(self, "警告", "用户名已存在", QMessageBox.Yes, QMessageBox.Yes))
                return
                # 提示已存在
            else:
                sql = "INSERT INTO users(user_name,user_pw,user_perm) VALUES ('%s','%s','%s')" % (
                    userName, userPw,permCategory)
            query.exec_(sql)
            db.commit()
            print(QMessageBox.information(self, "提示", "添加用户成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.add_user_success_signal.emit()
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.userNameEdit.clear()
        self.pwEdit.clear()
        self.historyEdit.clear()
        self.userImageEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = addUserDialog()
    mainMindow.show()
    sys.exit(app.exec_())