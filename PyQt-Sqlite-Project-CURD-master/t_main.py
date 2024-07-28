import os
import sys
# sys.path.append('D:\python38\work\code_fo\PyQt-Sqlite-Project-CURD-master')
# sys.path.append('code_fo/Talking-Face_PC-AVS-main')
# sys.path.append('code_fo/MockingBird')
from datetime import time
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from tqdm import tk
# from untitled import *
from addDialog import addPaDialog
from alterDialog import alterPaDialog
# from untitled import Ui_MainWindow
import sys, sqlite3
from PyQt5.QtGui import QIcon, QPixmap
from indexres import *
from image import *


class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)
        self.m_flag = False
        self.resize(500, 434)  # 900,600
        self.setWindowTitle("欢迎登陆康复系统")
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.ui.pushButton_resize.clicked.connect(self.resize_win)
        icon = QIcon()
        icon.addPixmap(QPixmap('logo.jpg'))

        # icon = QIcon("./back.jpg")
        # self.setWindowIcon(icon)
        self.signUpLabel = QLabel("失语症康复训练系统")
        # self.label = MyQLabel(self.signUpLabel)
        # self.label.connect_customized_slot(self.change_text)
        self.signUpLabel.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.signUpLabel.setAlignment(Qt.AlignCenter)
        self.signUpLabel.setFixedWidth(400)
        self.signUpLabel.setFixedHeight(100)
        self.label = QLabel("")
        self.label.setGeometry(QtCore.QRect(0, 0, 789, 434))
        self.label.setPixmap(QPixmap('indexres/img_1.png'))  # 图片路径
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedWidth(500)
        self.label.setFixedHeight(250)

        # self.label.setStyleSheet("border-image: url(indexres/img_1.png);\n"
        #                          "border-top-left-radius:30px;\n"
        #                          "border-bottom-left-radius:30px\n"
        #                          "}\n"
        #                          );
        self.setStyleSheet("QDialog{\n"
                           "    border-radius:30px;\n"
                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"

                           "}\n"

                           " ");
        # 上面是设置背景颜色，下面是设置背景图片
        # self.setGeometry(QtCore.QRect(60, 40, 241, 311))
        # self.setStyleSheet("border-image: url(:/images/back.png);")

        font = QFont()
        font.setPixelSize(36)

        lineEditFont = QFont()
        lineEditFont.setPixelSize(16)
        self.signUpLabel.setFont(font)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label, Qt.AlignHCenter)
        self.layout.addWidget(self.signUpLabel, Qt.AlignHCenter)
        # self.layout_2 = QHBoxLayout()

        self.setLayout(self.layout)
        # self.setLayout(self.layout_2)
        # table
        self.formlayout = QFormLayout()
        font.setPixelSize(18)

        # row 1
        self.namelabel = QLabel("姓    名: ")
        self.namelabel.setFont(font)
        self.nameinput = QLineEdit()
        self.nameinput.setFixedWidth(180)
        self.nameinput.setFixedHeight(32)
        self.nameinput.setFont(lineEditFont)
        self.nameinput.setStyleSheet("border:2px solid rgb(186,186,186);\n"
                                     "border-radius:10px\n"
                                     "")
        self.namelabel.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.nameinput.setMaxLength(10)
        self.formlayout.addRow(self.namelabel, self.nameinput)
        # row 2
        self.passlabel = QLabel("密    码: ")
        self.passlabel.setFont(font)
        self.passinput = QLineEdit()
        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setFixedWidth(180)
        self.passinput.setFixedHeight(32)
        self.passinput.setFont(lineEditFont)
        self.passinput.setStyleSheet("border:2px solid rgb(186,186,186);\n"
                                     "border-radius:10px\n"
                                     "")
        self.passlabel.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.passinput.setMaxLength(20)
        self.formlayout.addRow(self.passlabel, self.passinput)

        self.checkBox_remeberpassword = QCheckBox()
        self.checkBox_remeberpassword.setText("记住密码")
        self.formlayout.addWidget(self.checkBox_remeberpassword)

        self.checkBox_autologin = QCheckBox()
        self.checkBox_autologin.setText("自动登录")
        self.formlayout.addWidget(self.checkBox_autologin)

        ####初始化登录信息
        self.init_login_info()

        ###自动登录
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.goto_autologin)
        # self.timer.timeout.connect(self.load)
        self.timer.setSingleShot(True)
        self.timer.start(1000)

        self.QBtn = QPushButton("登 录")
        self.QBtn.setFixedWidth(120)
        self.QBtn.setFixedHeight(30)
        self.QBtn.setFont(font)
        self.QBtn.setStyleSheet("QPushButton{\n"
                                "    background:orange;\n"
                                "    color:white;\n"
                                "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 8px;font-size:20px;font-family: 微软雅黑;\n"
                                "}\n"
                                "QPushButton:pressed{\n"
                                "    background:black;\n"
                                "}")
        self.QBtn.clicked.connect(self.login)
        self.formlayout.addRow("", self.QBtn)

        # self.QBtn = QPushButton("注 册")
        # self.QBtn.setFixedWidth(120)
        # self.QBtn.setFixedHeight(30)
        # self.QBtn.setFont(font)
        # self.QBtn.clicked.connect(self.BtnClick)
        # # self.QBtn.clicked.connect(self.user_register)
        # self.formlayout.addRow("", self.QBtn)

        # 增删改
        # self.layout.addLayout(self.pa_btns_laylout)
        self.addBtn = QPushButton("注 册")
        self.addBtn.setFixedWidth(120)
        self.addBtn.setFixedHeight(30)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("QPushButton{\n"
                                  "    background:orange;\n"
                                  "    color:white;\n"
                                  "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 8px;font-size:20px;font-family: 微软雅黑;\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "    background:black;\n"
                                  "}")
        # self.pa_btns_laylout.addWidget(self.addBtn)
        self.addBtn.clicked.connect(self.addBtnClicked)
        self.formlayout.addRow("", self.addBtn)

        title = QLabel("Login")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        widget = QWidget()
        widget.setLayout(self.formlayout)
        widget.setFixedHeight(250)
        widget.setFixedWidth(300)
        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(widget, Qt.AlignCenter)
        widget = QWidget()
        widget.setLayout(self.Hlayout)

        # widget2 = QWidget()
        # widget2.setLayout(self.formlayout)
        # widget2.setFixedHeight(150)
        # widget2.setFixedWidth(100)
        # self.Hlayout = QHBoxLayout()
        # self.Hlayout.addWidget(widget2, Qt.AlignCenter)
        # widget2 = QWidget()
        # widget2.setLayout(self.Hlayout)
        self.layout.addWidget(widget, Qt.AlignHCenter)
        # self.layout_2.addWidget(widget2, Qt.AlignHCenter)
        # layout.addWidget(title)
        # layout.addWidget(self.nameinput)
        # layout.addWidget(self.passinput)
        # layout.addWidget(self.QBtn)
        # self.setLayout(layout)
        # 自动登录
        # 保存登录信息

    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        settings.setValue("account", self.nameinput.text())
        settings.setValue("password", self.passinput.text())
        settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
        settings.setValue("autologin", self.checkBox_autologin.isChecked())

    def init_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        the_account = settings.value("account")
        the_password = settings.value("password")
        the_remeberpassword = settings.value("remeberpassword")
        the_autologin = settings.value("autologin")
        ########
        self.nameinput.setText(the_account)
        if the_remeberpassword == "true" or the_remeberpassword == True:
            self.checkBox_remeberpassword.setChecked(True)
            self.passinput.setText(the_password)

        if the_autologin == "true" or the_autologin == True:
            self.checkBox_autologin.setChecked(True)

    def goto_autologin(self):
        if self.checkBox_autologin.isChecked() == True:
            self.login_2()

    def addBtnClicked(self):
        from adduser2 import addUserDialog
        addDialog = addUserDialog(self)
        # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()
        return LoginDialog

    def load(self):
        # from loading import SampleBar
        import time
        from loading import LoadingWidget
        load_widget = LoadingWidget()
        load_widget.show()
        QThread.sleep(3000)
        # time.sleep(1000)
        load_widget.exec_()

    def show_message_box(self):
        from loading import LoadingWidget
        self.load_widget = LoadingWidget()
        self.load_widget.show()
        # LoginDialog.close()
        # 开启对话框
        # self.msg_box_hint = QMessageBox()
        # self.msg_box_hint.setIcon(QMessageBox.Information)
        # self.msg_box_hint.setWindowTitle('正在登录')
        # # 标题自己设置
        # self.msg_box_hint.setText('正在处理中，请稍后...')
        # self.msg_box_hint.show()
        # # self.msg_box_hint.setIcon(QMessageBox.Information)
        # # 标题自己设置
        QApplication.processEvents()

    def close_message_box(self):
        # 关闭对话框
        # from loading import LoadingWidget
        # load_widget = LoadingWidget()
        self.load_widget.close()
        # self.msg_box_hint.close()

        #
        # loadDialog = SampleBar(self)
        # # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
        # loadDialog.show()
        # time.sleep(5)
        # loadDialog.exec_()
        # return IndexWindow

    def login(self):
        username = ""
        username = self.nameinput.text()
        password = ""
        password = self.passinput.text()
        exist = 0
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from users WHERE user_name=? AND user_pw=?", (username, password))
            row = result.fetchone()
            # print(row)
            if not row is None:
                # try:
                self.show_message_box()
                #
                ####### 保存登录信息
                self.save_login_info()
                QThread.sleep(3)
                self.accept()
                # LoginDialog.exec_()

                # QThread.sleep(5)
                # self.accept()
                #
                self.close_message_box()

            # self.accept()
            # self.show_message_box()
            else:
                QMessageBox.warning(QMessageBox(), '警告', '没有找到登录信息.')
            # os.system("pause")
            self.conn.commit()
            self.c.close()
            self.conn.close()

        except Exception:
            return

    def login_2(self):
        username = ""
        username = self.nameinput.text()
        password = ""
        password = self.passinput.text()
        exist = 0
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from users WHERE user_name=? AND user_pw=?", (username, password))
            row = result.fetchone()
            # print(row)
            if not row is None:
                # try:
                self.show_message_box()
                #
                ####### 保存登录信息
                self.save_login_info()
                QThread.sleep(3)
                self.accept()
                #
                self.close_message_box()

            # self.accept()
            # self.show_message_box()
            else:
                QMessageBox.warning(QMessageBox(), '提示', '请勾选记住密码')
            # os.system("pause")
            self.conn.commit()
            self.c.close()
            self.conn.close()

        except Exception:
            return

    # def resize_win(self):
    #     if self.isMaximized():
    #         self.showNormal()
    #         self.ui.pushButton_resize.setIcon(QtGui.QIcon(":/icons/fullscreen-expand.png"))
    #     else:
    #         self.showMaximized()
    #         self.ui.pushButton_resize.setIcon(QtGui.QIcon(":/icons/fullscreen-shrink.png"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_position)
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    # def change_text(self, flag):
    #     if flag % 2 == 1:
    #         _translate = QtCore.QCoreApplication.translate
    #         font = QtGui.QFont()
    #         font.setFamily("微软雅黑")
    #         font.setPointSize(18)
    #         self.label.setFont(font)
    #         self.label.setText(_translate("MainWindow", "Design By LJK"))
    #     else:
    #         _translate = QtCore.QCoreApplication.translate
    #         font = QtGui.QFont()
    #         font.setFamily("微软雅黑")
    #         font.setPointSize(35)
    #         font.setBold(False)
    #         font.setItalic(False)
    #         font.setWeight(9)
    #         self.label.setFont(font)
    #         self.label.setText(_translate("MainWindow", "APMH 2022"))


class MyQLabel(QtWidgets.QLabel):
    # 自定义信号, 注意信号必须为类属性
    button_clicked_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)
        self.i = 0

    def mouseReleaseEvent(self, QMouseEvent):
        self.i += 1
        self.button_clicked_signal.emit(self.i)

    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)


class IndexWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(IndexWindow, self).__init__(*args, **kwargs)
        self.resize(700, 500)
        self.setWindowTitle("欢迎使用康复训练系统")
        icon = QIcon()
        icon.addPixmap(QPixmap('logo.jpg'))
        # icon = QIcon("./back.jpg")
        self.setWindowIcon(icon)
        # 查询模型
        self.queryModel = None
        # 数据表
        self.tableView = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecord = 0
        # 每页数据数
        self.pageRecord = 20
        # 当前患者名字
        self.temp_paname = ""
        # 当前患者编号
        self.temp_pano = ""
        # 初始化修改窗口
        from alterDialog import alterPaDialog
        self.alterDialog = alterPaDialog()
        # self.alterDialog = Ui_MainWindow()
        from user_management import ManageWindow
        self.userManageWindow = ManageWindow()
        from train import TrainWindow
        self.trainWindow = TrainWindow()
        self.setUpUI()

    def setUpUI(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        # 添加sql语句
        self.c.close()
        self.setFixedSize(960, 700)

        # 选择患者
        self.layout = QVBoxLayout()
        self.indexlayout = QHBoxLayout()
        self.pa_layout = QHBoxLayout()
        self.Hlayout1 = QHBoxLayout()
        self.pa_btns_laylout = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

        self.titlelabel = QLabel("康复训练")
        font = self.titlelabel.font()
        font.setPointSize(25)
        font.setBold(1)
        font.setFamily("黑体")
        self.titlelabel.setFont(font)
        index_btn_len = 125
        index_btn_len_2 = 150

        self.IndexBtn = QtWidgets.QPushButton("首页")
        self.IndexBtn.setObjectName('index_button')
        self.IndexBtn.move(250, 100)
        self.IndexBtn.setFixedSize(150, 50)
        self.IndexBtn.setStyleSheet("QPushButton{\n"
                                    "    background:rgb(81, 71, 81);\n"
                                    "    color: white;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        self.IndexBtn.setIcon(QIcon(QPixmap("indexres/shouye.png")))

        self.trainMissionBtn = QtWidgets.QPushButton("训练任务")
        self.trainMissionBtn.setObjectName('index_button')
        self.trainMissionBtn.setObjectName('index_button')
        self.trainMissionBtn.move(250, 100)
        self.trainMissionBtn.setFixedSize(150, 50)
        self.trainMissionBtn.setIcon(QIcon(QPixmap("indexres/yinpin.png")))

        # self.trainMissionBtn.setFixedWidth(index_btn_len)

        self.user_manage_btn = QtWidgets.QPushButton("用户管理")
        self.user_manage_btn.setObjectName('index_button')
        self.user_manage_btn.setObjectName('index_button')
        self.user_manage_btn.move(250, 100)
        self.user_manage_btn.setFixedSize(150, 50)
        self.user_manage_btn.setIcon(QIcon(QPixmap("indexres/yonghu.png")))

        # self.user_manage_btn.setFixedWidth(index_btn_len)

        self.sys_manage_btn = QtWidgets.QPushButton("系统管理")
        self.sys_manage_btn.setObjectName('index_button')
        self.sys_manage_btn.move(250, 100)
        self.sys_manage_btn.setFixedSize(150, 50)

        self.sys_manage_btn.setObjectName('index_button')
        self.sys_manage_btn.setIcon(QIcon(QPixmap("indexres/shezhi.png")))
        # self.sys_manage_btn.setFixedWidth(index_btn_len)

        self.studyBtn = QtWidgets.QPushButton("教 程")
        self.studyBtn.setObjectName('index_button')
        self.studyBtn.move(250, 100)
        self.studyBtn.setFixedSize(150, 50)
        self.studyBtn.setIcon(QIcon(QPixmap("indexres/dianji.png")))
        #
        # self.studyBtn.setFixedWidth(index_btn_len)

        self.jumpToLabel_5 = QLabel("        ")
        self.jumpToLabel_5.setFixedWidth(50)
        self.jumpToLabel_6 = QLabel("  ")
        self.jumpToLabel_6.setFixedWidth(60)

        self.indexlayout.addWidget(self.titlelabel)
        # self.indexlayout.addWidget(self.jumpToLabel_6)
        self.indexlayout.addWidget(self.IndexBtn)
        self.indexlayout.addWidget(self.jumpToLabel_5)
        self.indexlayout.addWidget(self.trainMissionBtn)
        self.indexlayout.addWidget(self.jumpToLabel_5)
        self.indexlayout.addWidget(self.user_manage_btn)
        self.indexlayout.addWidget(self.jumpToLabel_5)
        self.indexlayout.addWidget(self.sys_manage_btn)
        self.indexlayout.addWidget(self.jumpToLabel_5)
        self.indexlayout.addWidget(self.studyBtn)

        self.exitBtn = QtWidgets.QPushButton("退出系统")
        self.exitBtn.setObjectName('index_button')
        self.exitBtn.move(250, 100)
        self.exitBtn.setFixedSize(150, 50)
        self.exitBtn.setStyleSheet("QPushButton{\n"
                                   "    background:orange;\n"
                                   "    color:white;\n"
                                   "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "    background:black;\n"
                                   "}")
        self.exitBtn.setIcon(QIcon(QPixmap("indexres/tuichu.png")))

        self.indexlayout.addWidget(self.jumpToLabel_5)
        # self.indexlayout.addWidget(self.exitBtn)
        # self.exitBtn.setFixedWidth(index_btn_len)
        self.indexlayout.addWidget(self.titlelabel)
        # self.indexlayout.addWidget(self.IndexBtn)
        # self.indexlayout.addWidget(self.trainMissionBtn)
        # self.indexlayout.addWidget(self.user_manage_btn)
        # self.indexlayout.addWidget(self.sys_manage_btn)
        # self.indexlayout.addWidget(self.studyBtn)
        self.indexlayout.addWidget(self.exitBtn)
        # 导航栏按钮
        self.exitBtn.clicked.connect(self.exitBtnClick)
        self.trainMissionBtn.clicked.connect(self.trainMissionBtnClick)
        self.sys_manage_btn.clicked.connect(self.sysManageBtnClicked)
        self.studyBtn.clicked.connect(self.studyBtnClicked)

        # 添加导航栏按钮功能
        self.user_manage_btn.clicked.connect(self.userManageBtnClicked)
        # 当前已选择患者

        self.selected_pa_label = QLabel("当前选择的患者为：无")
        self.pa_layout.addWidget(self.selected_pa_label)
        # Hlayout1，查询功能
        self.searchEdit = QLineEdit()
        self.searchEdit.setFixedHeight(50)
        self.searchEdit.setFixedWidth(1500)
        font = QFont()
        font.setPixelSize(15)
        self.searchEdit.setFont(font)

        self.searchButton = QPushButton("查询患者")
        self.searchButton.setFixedHeight(50)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton{\n"
                                        "    background:rgb(244, 183, 100);\n"
                                        "    color: rgb(81, 71, 81);\n"
                                        "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-size:20px;font-family: 微软雅黑;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background:black;\n"
                                        "}")
        self.searchButton.setIcon(QIcon(QPixmap("indexres/sousuo.png")))

        from zidingyi import Ui_Form
        self.audiorecorder = Ui_Form()
        self.condisionComboBox = QComboBox(objectName="comboboxObj")
        # self.condisionComboBox = QComboBox()
        searchCondision = ['按姓名查询', '按身份证号查询']
        self.condisionComboBox.setFont(QFont('宋体', 15, QFont.Black))
        # self.condisionComboBox.setForeground(QBrush(QColor(106,106,106)))
        self.condisionComboBox.setFixedHeight(50)
        # self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)

        # self.condisionComboBox.setStyleSheet("""
        # #comboBox{
        #     background-color: rgb(178,200,187);
        #     border: 1px solid rgb(200, 200, 200);
        #     color: rgb(7,99,109);
        #     font-weight: bold;
        # }
        # #comboboxObj QAbstractItemView::item{
        #     height:20px;
        # }
        # #comboboxObj::drop-down{
        #     border: 0px;
        # }
        # #comboboxObj::down-arrow{
        #     image:url("combobox/more.png");
        #     width: 15px;
        #     height:15px;
        # }
        # """)
        # # 最后需设置一下listView
        # self.condisionComboBox.setView(QListView())

        self.condisionComboBox.setStyleSheet("#comboBox{\n"
                                             "    border-radius:11px;\n"
                                             "    \n"
                                             "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"
                                             # "    color: rgb(56,56,56);\n"
                                             "    font: 15pt \"微软雅黑\";\n"
                                             "    font-size: 20px ;\n"
                                             "    color:rgb(106,106,106) ;\n"
                                             "    font-weight:bold;\n"
                                             "}\n"
                                             "#comboBox:hover{\n"
                                             "    border-radius:0px;\n"
                                             "    \n"
                                             "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(156, 232, 60, 202), stop:1 rgba(250, 221, 7, 169));\n"
                                             "    border-top-left-radius:10px;\n"
                                             "    border-top-right-radius:10px;\n"
                                             "    border-bottom-right-radius:10px;\n"
                                             "    color: rgb(56,56,56);\n"
                                             "}\n"
                                             "#comboBox::drop-down{\n"
                                             "    border-top-right-radius:5px;\n"
                                             "    border-bottom-right-radius:5px;\n"
                                             "    \n"
                                             "    color: rgb(40,40,40);\n"
                                             "    min-width:30px;\n"
                                             "}\n"
                                             "#comboBox::down-arrow{\n"
                                             "    \n"
                                             "    image: url(indexres/xia.png);\n"
                                             "    height:18px;\n"
                                             "    width:18px;\n"
                                             "}\n"
                                             "#comboBox::QAbstractItemView{\n"
                                             "    font: 15pt \"微软雅黑\";\n"
                                             "    font-weight:bold;\n"
                                             "}\n"
                                             "#comboBox::QAbstractItemView::item{\n"
                                             "    color: rgb(40, 40, 40);\n"
                                             "    height:30px;\n"
                                             "    selection-color: rgb(186,186,186);\n"
                                             "    background-color:rgb(80, 80, 80);\n"
                                             "}\n"
                                             "")
        self.condisionComboBox.setObjectName("comboBox")

        self.Hlayout1.addWidget(self.searchEdit)
        self.Hlayout1.addWidget(self.searchButton)
        # self.scrollArea =QFormLayout()
        # self.scrollWidget = QWidget()
        # self.scrollArea.setWidget(self.scrollWidget)
        # self.formlayout = QFormLayout()
        # self.scrollWidget.setLayout(self.formlayout)
        # self.Hlayout1.addWidget(self.audiorecorder)
        self.Hlayout1.addWidget(self.condisionComboBox)

        # 增删改
        self.addBtn = QPushButton("增加患者")
        self.addBtn.setStyleSheet("QPushButton{\n"
                                  "    border:none;\n"
                                  "    color:rgb(106,106,106);\n"
                                  "}\n"
                                  "QPushButton:focus{\n"
                                  "    color:rgb(186,186,186);\n"
                                  "}\n"
                                  "")
        self.deleteBtn = QPushButton("删除患者")
        self.deleteBtn.setStyleSheet("QPushButton{\n"
                                     "    border:none;\n"
                                     "    color:rgb(106,106,106);\n"
                                     "}\n"
                                     "QPushButton:focus{\n"
                                     "    color:rgb(186,186,186);\n"
                                     "}\n"
                                     "")
        self.alterBtn = QPushButton("查看患者")
        self.alterBtn.setStyleSheet("QPushButton{\n"
                                    "    border:none;\n"
                                    "    color:rgb(106,106,106);\n"
                                    "}\n"
                                    "QPushButton:focus{\n"
                                    "    color:rgb(186,186,186);\n"
                                    "}\n"
                                    "")
        self.generateBtn = QPushButton("生成患者训练视频")
        self.generateBtn.setStyleSheet("QPushButton{\n"
                                       "    border:none;\n"
                                       "    color:rgb(106,106,106);\n"
                                       "}\n"
                                       "QPushButton:focus{\n"
                                       "    color:rgb(186,186,186);\n"
                                       "}\n"
                                       "")
        self.alterBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.generateBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.addBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.deleteBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.exitBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.sys_manage_btn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.studyBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.user_manage_btn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.trainMissionBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.IndexBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.pa_btns_laylout.addWidget(self.addBtn)
        self.pa_btns_laylout.addWidget(self.deleteBtn)
        self.pa_btns_laylout.addWidget(self.alterBtn)
        self.pa_btns_laylout.addWidget(self.generateBtn)
        self.addBtn.clicked.connect(self.addBtnClicked)
        self.deleteBtn.clicked.connect(self.deleteBtnClicked)
        self.alterBtn.clicked.connect(self.boby1)
        self.generateBtn.clicked.connect(self.generateBtnClicked)

        # Hlayout2初始化，翻页功能
        self.jumpToLabel = QLabel("跳转到第")
        self.jumpToLabel.setFixedWidth(300)
        self.jumpToLabel_2 = QLabel(" ")
        self.jumpToLabel_2.setFixedWidth(5)
        self.pageEdit = QLineEdit()
        self.pageEdit.setFixedWidth(40)
        s = "/" + str(self.totalPage) + "页"
        self.pageLabel = QLabel(s)
        self.jumpToLabel_4 = QLabel(" ")
        self.jumpToLabel_4.setFixedWidth(5)
        self.jumpToButton = QPushButton("跳转")
        self.prevButton = QPushButton("前一页")
        self.prevButton.setFixedWidth(80)
        self.jumpToLabel_3 = QLabel(" ")
        self.jumpToLabel_3.setFixedWidth(5)
        self.backButton = QPushButton("后一页")
        self.backButton.setFixedWidth(80)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.jumpToLabel)
        Hlayout.addWidget(self.jumpToLabel_2)
        Hlayout.addWidget(self.pageEdit)
        Hlayout.addWidget(self.pageLabel)
        Hlayout.addWidget(self.jumpToLabel_4)
        Hlayout.addWidget(self.jumpToButton)
        Hlayout.addWidget(self.jumpToLabel_4)
        Hlayout.addWidget(self.prevButton)
        Hlayout.addWidget(self.jumpToLabel_3)
        Hlayout.addWidget(self.backButton)
        widget = QWidget()
        widget.setLayout(Hlayout)
        widget.setFixedWidth(500)
        self.Hlayout2.addWidget(widget)

        lab = [self.addBtn, self.deleteBtn, self.generateBtn, self.alterBtn]
        tb = [self.exitBtn, self.sys_manage_btn, self.studyBtn, self.user_manage_btn, self.trainMissionBtn,
              ]
        yb = [self.jumpToLabel, self.pageEdit,
              self.jumpToButton, self.prevButton, self.backButton]
        font = QtGui.QFont()
        font.setPointSize(15)  # 括号里的数字可以设置成自己想要的字体大小
        # font.setFamily("SimHei")  # 黑体
        font.setFamily("SimSun")  # 宋体
        for i in lab:
            i.setFont(font)
        for i in tb:
            # i.setStyleSheet("QPushButton{font: 75 16pt \"微软雅黑\";\n"
            #                                "color: rgb(255,255,255);    \n"
            #                                "padding-left:0px;\n"
            #                                "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(251,102,102, 200), stop:1 rgba(20,196,188, 210));\n"
            #                                "border:2px solid rgb(20,196,188);\n"
            #                                "border-radius:15px;}"
            #                                "QToolButton::hover{background:rgba(251,102,102, 200);}")

            i.setStyleSheet("QPushButton{\n"
                            "    background:rgb(244, 183, 0);\n"
                            "    color: rgb(81, 71, 81);\n"
                            "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                            "}\n"
                            "QPushButton:pressed{\n"
                            "    background:black;\n"
                            "}")
            i.setFont(font)
        for i in yb:
            font = QtGui.QFont()
            font.setPointSize(10)  # 括号里的数字可以设置成自己想要的字体大小
            i.setFont(font)

        # tableView
        # 患者信息

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('database.db')
        self.db.open()
        self.tableView = QTableView()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        self.func_mappingSignal()

        self.tableView.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));font: '宋体';color: black;padding-left: 5px;border-left:0px solid #000;border-right:1px solid lightgreen;border-top:0px solid #000;}")

        # "QHeaderView::section{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));font:11pt '宋体';color: black;};")
        self.tableView.setStyleSheet("selection-background-color:lightblue;")
        hearder = self.tableView.verticalHeader()
        hearder.hide()
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.showPaImage()
        index = self.tableView.currentIndex()  # 取得当前选中行的index
        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)
        self.model = QStandardItemModel(5, 3)  # 创建一个标准的数据源model
        self.model.setHorizontalHeaderLabels(["id", "姓名", "年龄"])  # 设置表格的表头名称
        model = self.tableView.model()
        print(model.itemData(model.index(index.row(), 0)))

        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.queryModel = QSqlQueryModel()
        self.tableView.setModel(self.queryModel)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "姓名")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "性别")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "年龄")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "身份证号")

        self.layout.addLayout(self.indexlayout)
        self.layout.addLayout(self.pa_layout)
        self.layout.addLayout(self.Hlayout1)
        self.layout.addWidget(self.tableView)
        self.layout.addLayout(self.pa_btns_laylout)
        self.layout.addLayout(self.Hlayout2)
        self.setLayout(self.layout)
        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.backButton.clicked.connect(self.backButtonClicked)
        self.jumpToButton.clicked.connect(self.jumpToButtonClicked)
        self.searchEdit.returnPressed.connect(self.searchButtonClicked)

    def userManageBtnClicked(self):
        self.userManageWindow.showFullScreen()
        self.userManageWindow.searchButtonClicked()
        self.close()

    def studyBtnClicked(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://book.yunzhan365.com/vdogo/wpil/mobile/index.html'))

    def trainMissionBtnClick(self):
        if not (self.temp_pano == ""):
            self.trainWindow.showFullScreen()
            self.trainWindow.setNo(self.temp_pano)
            self.close()
        else:

            print(QMessageBox.warning(self, "警告", "请选择一名患者", QMessageBox.Yes, QMessageBox.Yes))

    def sysManageBtnClicked(self):
        from sys_management import SysManageWindow
        self.sysManageWindow = SysManageWindow()
        self.sysManageWindow.searchButtonClicked()
        self.sysManageWindow.showFullScreen()
        self.close()

    def func_mappingSignal(self):
        self.tableView.clicked.connect(self.func_test)
        self.tableView.doubleClicked.connect(self.boby1)

    # def double_click_table_view_item(self):
    #fine和v应付应付预付

    def func_test(self, item):
        # http://www.python-forum.org/viewtopic.php?f=11&t=16817
        cellContent = item.data()
        print(cellContent)  # test
        sf = ",您选择了第 {1}位患者".format(item.column(), item.row() + 1)
        # rt = "您好{0},".format(item.column(), item.row()+1)
        print(sf)
        # 获取患者名字
        NewIndex = self.tableView.currentIndex().siblingAtColumn(1)
        Name = NewIndex.data()
        self.selected_pa_label.setText("当前选择的患者为：" + Name + sf)
        # self.selected_pa_label_2.setText(sf)
        self.temp_paname = Name
        # 获取患者编号
        pa_no_index = self.tableView.currentIndex().siblingAtColumn(0)
        self.temp_pano = pa_no_index.data()

    def addBtnClicked(self):
        addDialog = addPaDialog(self)
        # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()
        self.searchButtonClicked()

    def deleteBtnClicked(self):
        if (self.temp_pano == ""):
            print(QMessageBox.warning(self, "警告", "请选择一名患者", QMessageBox.Yes, QMessageBox.Yes))
        else:
            ret = QMessageBox.information(self, "提示", "是否删除患者" + self.temp_paname, QMessageBox.Yes,
                                          QMessageBox.No)
            if (ret == QMessageBox.Yes):
                db = QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName('database.db')
                db.open()
                query = QSqlQuery()
                # 如果已存在，则update Book表的现存量，剩余可借量，不存在，则insert Book表，同时insert buyordrop表
                sql = "SELECT * FROM patient WHERE pa_no='%s'" % (self.temp_pano)
                query.exec_(sql)
                # 提示不存在
                if not (query.next()):
                    print(QMessageBox.warning(self, "警告", "该患者不存在", QMessageBox.Yes, QMessageBox.Yes))
                    return
                else:
                    sql = "DELETE FROM patient WHERE pa_no='%s'" % (self.temp_pano)
                    query.exec_(sql)
                    db.commit()
                    print(QMessageBox.information(self, "提示", "删除成功，患者" + self.temp_paname + "已删除",
                                                  QMessageBox.Yes,
                                                  QMessageBox.Yes))
                    self.temp_pano = ""
                    self.temp_paname = ""
                    self.selected_pa_label.setText("当前选择的患者为：")
        self.searchButtonClicked()

    def boby1(self):
        self.alterDialog.setNo(self.temp_pano)
        self.alterDialog.fillContent()
        # self.alterDialog.hide()
        self.alterDialog.show()
        self.alterDialog.exec_()
        self.searchButtonClicked()
        # import untitled
        # from untitled import Ui_MainWindow
        # self.one =untitled.Ui_MainWindow()
        # self.one.show()
        # # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)

    # def boby2(self):

    def generateBtnClicked(self):
        try:
            if (self.temp_pano == ""):
                print(QMessageBox.warning(self, "警告", "请选择一名患者", QMessageBox.Yes, QMessageBox.Yes))
            else:
                from generate import GenerateWindow
                generate_window = GenerateWindow(self, self.temp_pano)
                # 获取屏幕分辨率
                screen_size = QDesktopWidget().screenGeometry()
                # 计算窗口大小
                width = screen_size.width()
                height = screen_size.height() / 2
                generate_window.resize(width, height)
                # 计算窗口位置
                x = 0
                y = 0
                generate_window.move(x, y)
                generate_window.show()
                self.hide()
        except Exception as e:
            print(f'Error14: {e}')

    # 查询
    def recordQuery(self, index):
        queryCondition = ""
        conditionChoice = self.condisionComboBox.currentText()
        if (conditionChoice == "按姓名查询"):
            conditionChoice = 'pa_name'
        elif (conditionChoice == "按身份证号查询"):
            conditionChoice = 'pa_id'

        if (self.searchEdit.text() == ""):
            queryCondition = "select * from patient"
            self.queryModel.setQuery(queryCondition)
            self.totalRecord = self.queryModel.rowCount()
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
            queryCondition = (
                    "select * from patient ORDER BY %s  limit %d,%d " % (conditionChoice, index, self.pageRecord))
            self.queryModel.setQuery(queryCondition)
            self.setButtonStatus()
            return

        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = ("SELECT * FROM patient WHERE %s LIKE '%s' ORDER BY %s " % (
            conditionChoice, s, conditionChoice))
        self.queryModel.setQuery(queryCondition)
        self.totalRecord = self.queryModel.rowCount()
        # 当查询无记录时的操作
        if (self.totalRecord == 0):
            print(QMessageBox.information(self, "提醒", "查询无记录", QMessageBox.Yes, QMessageBox.Yes))
            queryCondition = "select * from patient"
            self.queryModel.setQuery(queryCondition)
            self.totalRecord = self.queryModel.rowCount()
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
            queryCondition = (
                    "select * from patient ORDER BY %s  limit %d,%d " % (conditionChoice, index, self.pageRecord))
            self.queryModel.setQuery(queryCondition)
            self.setButtonStatus()
            return
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        label = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(label)
        queryCondition = ("SELECT * FROM patient WHERE %s LIKE '%s' ORDER BY %s LIMIT %d,%d " % (
            conditionChoice, s, conditionChoice, index, self.pageRecord))
        self.queryModel.setQuery(queryCondition)
        self.setButtonStatus()
        return

    def setButtonStatus(self):
        if (self.currentPage == self.totalPage):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(False)
        if (self.currentPage == 1):
            self.backButton.setEnabled(True)
            self.prevButton.setEnabled(False)
        if (self.currentPage < self.totalPage and self.currentPage > 1):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(True)

    # 得到记录数
    def getTotalRecordCount(self):
        self.queryModel.setQuery("SELECT * FROM patient")
        self.totalRecord = self.queryModel.rowCount()
        return

    # 得到总页数
    def getPageCount(self):
        self.getTotalRecordCount()
        # 上取整
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        return

    # 点击查询
    def searchButtonClicked(self):
        self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        self.getPageCount()
        s = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(s)
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

        # 向前翻页

    def prevButtonClicked(self):
        self.currentPage -= 1
        if (self.currentPage <= 1):
            self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

        # 向后翻页

    def backButtonClicked(self):
        self.currentPage += 1
        if (self.currentPage >= int(self.totalPage)):
            self.currentPage = int(self.totalPage)
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

        # 点击跳转

    def jumpToButtonClicked(self):
        if (self.pageEdit.text().isdigit()):
            self.currentPage = int(self.pageEdit.text())
            if (self.currentPage > self.totalPage):
                self.currentPage = self.totalPage
            if (self.currentPage <= 1):
                self.currentPage = 1
        else:
            self.currentPage = 1
        index = (self.currentPage - 1) * self.pageRecord
        self.pageEdit.setText(str(self.currentPage))
        self.recordQuery(index)
        return

    def exitBtnClick(self):
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
        font.setPixelSize(23)
        self.messageBox.setFont(font)

        self.messageBox.setText('是否要退出系统')

        self.messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        buttonY = self.messageBox.button(QMessageBox.Yes)

        buttonY.setText('是')

        buttonN = self.messageBox.button(QMessageBox.No)

        buttonN.setText('否')

        self.messageBox.exec_()

        if self.messageBox.clickedButton() == buttonY:
            app = QApplication(sys.argv)
            sys.exit(app.exec_())
        else:
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IndexWindow()
    window.showFullScreen()
    window.searchButtonClicked()
    sys.exit(app.exec_())
# window = WordWindow()
# window.showFullScreen()
# sys.exit(app.exec_())