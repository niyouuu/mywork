import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
from PyQt5.QtSql import *
class alterUserDialog(QDialog):
    add_user_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(alterUserDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("用户信息")

    def setUpUI(self):
        icon = QIcon()
        icon.addPixmap(QPixmap('logo.jpg'))
        # self.setStyleSheet("    background-color: rgb(255,255,255);\n")
        permCategory = ["管理员", "普通用户"]
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("查看修改用户")
        self.userNameLabel = QLabel("用户名:")
        self.permLabel = QLabel("权    限:")
        self.pwLabel = QLabel("密    码:")

        # button控件
        self.alterBtn = QPushButton("修 改")

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
        self.layout.addRow("", self.alterBtn)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)
        self.userNameLabel.setFont(font)
        self.pwLabel.setFont(font)
        self.permLabel.setFont(font)

        self.userNameEdit.setFont(font)
        self.pwEdit.setFont(font)
        self.permComboBox.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.alterBtn.setFont(font)
        self.alterBtn.setFixedHeight(32)
        self.alterBtn.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        #        self.layout.setVerticalSusercing(10)

        self.alterBtn.clicked.connect(self.alterBtnCicked)

        lab = [self.alterBtn]
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

    # 展示原本的用户信息
    def fillContent(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('database.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM users WHERE user_no='%s'" % (self.temp_alter_no)
        print(self.temp_alter_no)
        query.exec_(sql)
        if (query.next()):
            print("打印："+query.value(1))
            self.userNameEdit.setText(query.value(1))
            self.pwEdit.setText(query.value(2))
            self.permComboBox.setCurrentText(str(query.value(3)))
            return
            # 提示已存在
        else:
            print(QMessageBox.warning(self, "警告", "该用户不存在", QMessageBox.Yes, QMessageBox.Yes))
        # query.exec_(sql)
        db.commit()
    def setNo(self,no_value):
        self.temp_alter_no=str(no_value)
    def alterBtnCicked(self):
        userName = self.userNameEdit.text()
        userPw = self.pwEdit.text()
        if (self.permComboBox.currentText() == "管理员"):
            permCategory = 0
        elif (self.permComboBox.currentText() == "普通用户"):
            permCategory = 1
        if (
                userName == "" or userPw == "" or permCategory == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，修改失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('database.db')
            db.open()
            query = QSqlQuery()

            sql = "UPDATE users SET user_name='%s',user_pw='%s',user_perm='%s' WHERE user_no='%s'" % (
                userName, userPw, permCategory,self.temp_alter_no)
            if not query.exec_(sql):
                print(QMessageBox.warning(self, "警告", "用户名与其他用户重复!", QMessageBox.Yes, QMessageBox.Yes))
                return
            db.commit()
            print(QMessageBox.information(self, "提示", "修改成功!", QMessageBox.Yes, QMessageBox.Yes))
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
    mainMindow = alterUserDialog()
    mainMindow.show()
    sys.exit(app.exec_())