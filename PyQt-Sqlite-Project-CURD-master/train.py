from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtPrintSupport import *
import sys, sqlite3, time
import os
import sys

# sys.path.append('D:\python38\work\code_fo\Talking-Face_PC-AVS-main')
sys.path.append('..\ASRT')
# import sys
# sys.path.append('code_fo/ASRT')
from ASRT.speech_model_zoo import SpeechModel251BN
from qtpy import QtGui

from addDialog import addPaDialog
from alterDialog import alterPaDialog
from adduser import addUserDialog
from alteruser import alterUserDialog

class TrainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(TrainWindow, self).__init__(*args, **kwargs)
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
        self.pageRecord = 10
        # 当前用户名字
        self.temp_username = ""
        # 当前用户编号
        self.temp_userno = ""
        # 当前患者编号
        self.temp_pano = "0"
        #随机
        self.is_random=0 # 正序
        #自动
        self.is_auto=0 # 自动
        # 类型计数
        self.i = 0
        self.task_type_edit = QLineEdit()
        # 初始化修改窗口
        self.alterDialog = alterUserDialog()
        self.setUpUI()

    def setUpUI(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        # 添加sql语句
        self.c.close()
        self.setFixedSize(960, 700)

        # 选择用户
        self.layout = QVBoxLayout()
        self.indexlayout = QHBoxLayout()
        self.pa_layout = QHBoxLayout()
        self.pa_btns_laylout = QHBoxLayout()

        # 导航栏
        # self.index_widget = QtWidgets.QWidget()  # 创建左侧部件
        # self.index_widget.setObjectName('index_widget')
        # self.index_widget.setLayout(self.indexlayout) # 设置左侧部件布局为网格

        self.titlelabel = QLabel("康复训练")
        font = self.titlelabel.font()
        font.setPointSize(25)
        font.setBold(1)
        font.setFamily("黑体")
        self.titlelabel.setFont(font)
        index_btn_len = 150
        self.IndexBtn = QtWidgets.QPushButton("首页")
        self.IndexBtn.setObjectName('index_button')
        self.IndexBtn.move(250, 100)
        self.IndexBtn.setFixedSize(150, 50)
        self.IndexBtn.setIcon(QIcon(QPixmap("indexres/shouye.png")))
        # self.IndexBtn.setStyleSheet("QPushButton{\n"
        #                               "    background:orange;\n"
        #                               "    color:white;\n"
        #                               "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
        #                               "}\n"
        #                               "QPushButton:pressed{\n"
        #                               "    background:black;\n"
        #                               "}")

        # self.IndexBtn.setFixedWidth(index_btn_len)

        # button_open_img = QPushButton(self)
        # button_open_img.setText("打开图片")
        # button_open_img.move(250, 100)
        # button_open_img.setFixedSize(150, 50)
        # button_open_img.setStyleSheet("QPushButton{\n"
        #                               "    background:orange;\n"
        #                               "    color:white;\n"
        #                               "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
        #                               "}\n"
        #                               "QPushButton:pressed{\n"
        #                               "    background:black;\n"
        #                               "}")

        self.trainMissionBtn = QtWidgets.QPushButton("训练任务")
        self.trainMissionBtn.setObjectName('index_button')
        self.trainMissionBtn.setObjectName('index_button')
        self.trainMissionBtn.move(250, 100)
        self.trainMissionBtn.setFixedSize(150, 50)
        self.trainMissionBtn.setStyleSheet("QPushButton{\n"
                                    "    background:rgb(81, 71, 81);\n"
                                    "    color: white;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        self.trainMissionBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        # self.trainMissionBtn.setFixedWidth(index_btn_len)

        self.user_manage_btn = QtWidgets.QPushButton("用户管理")
        self.user_manage_btn.setObjectName('index_button')
        self.user_manage_btn.setObjectName('index_button')
        self.user_manage_btn.move(250, 100)
        self.user_manage_btn.setFixedSize(150, 50)

        # self.user_manage_btn.setFixedWidth(index_btn_len)

        self.sys_manage_btn = QtWidgets.QPushButton("系统管理")
        self.sys_manage_btn.setObjectName('index_button')
        self.sys_manage_btn.move(250, 100)
        self.sys_manage_btn.setFixedSize(150, 50)

        self.sys_manage_btn.setObjectName('index_button')
        self.studyBtn = QtWidgets.QPushButton("教 程")
        self.studyBtn.setObjectName('index_button')
        self.studyBtn.move(250, 100)
        self.studyBtn.setFixedSize(150, 50)
        #
        self.studyBtn.setFixedWidth(index_btn_len)

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
        # 导航栏按钮
        self.IndexBtn.clicked.connect(self.IndexBtnClick)
        self.exitBtn.clicked.connect(self.exitBtnClick)
        self.user_manage_btn.clicked.connect(self.userManageBtnClicked)
        self.sys_manage_btn.clicked.connect(self.sysManageBtnClicked)
        self.studyBtn.clicked.connect(self.studyBtnClicked)

        # 当前已选择用户

        self.selected_pa_label = QLabel("当前选择的患者为：无")
        self.pa_layout.addWidget(self.selected_pa_label)

        # 训练类型
        self.trainPackLayout = QHBoxLayout()
        self.train_mid_layout = QVBoxLayout()
        self.train_pic = QLabel()
        self.task_type_combo = QComboBox()
        self.searchCondision = ['元音训练', '词语训练', '配对训练', '连词成句训练']
        self.task_type_combo.setFixedHeight(50)
        self.task_type_combo.setFont(font)
        self.task_type_combo.addItems(self.searchCondision)
        self.task_type_combo.currentIndexChanged.connect(self.missionchange)
        self.task_type_combo.currentIndexChanged.connect(self.taskComboClick)
        self.changeTask()
        self.train_mid_layout.addWidget(self.train_pic)
        self.train_mid_layout.addWidget(self.task_type_combo)

        self.leftBtn = QPushButton("<<")#上一项
        self.rightBtn = QPushButton(">>")#下一项
        self.leftBtn.setFixedSize(300, 300)
        self.rightBtn.setFixedSize(300, 300)
        # self.leftBtn.setIcon(QIcon(QPixmap("indexres/upon.png")))
        # self.rightBtn.setIcon(QIcon(QPixmap("indexres/next.png")))
        # self.leftBtn.setIconSize(QSize(200, 200))  # 太小了，大一点
        # self.rightBtn.setIconSize(QSize(200, 200))
        self.leftBtn.clicked.connect(self.leftBtnClick)
        self.rightBtn.clicked.connect(self.rightBtnClick)

        self.trainPackLayout.addWidget(self.leftBtn)
        self.trainPackLayout.addLayout(self.train_mid_layout)
        self.trainPackLayout.addWidget(self.rightBtn)
        self.trainPackLayout.setAlignment(Qt.AlignCenter)
        # self.IndexBtn.setIcon(QIcon(QPixmap("indexres/shouye.png")))
        self.trainMissionBtn.setIcon(QIcon(QPixmap("indexres/yinpin.png")))
        self.user_manage_btn.setIcon(QIcon(QPixmap("indexres/yonghu.png")))
        self.sys_manage_btn.setIcon(QIcon(QPixmap("indexres/shezhi.png")))
        self.studyBtn.setIcon(QIcon(QPixmap("indexres/dianji.png")))
        self.exitBtn.setIcon(QIcon(QPixmap("indexres/tuichu.png")))
        # self.searchButton.setIcon(QIcon(QPixmap("indexres/sousuo.png")))

        # 训练方案
        self.task_content_layout = QHBoxLayout()
        self.task_titleLabel = QLabel("训练方案")
        # self.task_titleLabel.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        #                              "border-radius:10px\n"
        #                              "")
        self.task_titleLabel.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.task_titleLabel.setFont(font)
        # 训练类型
        self.task_type_layout = QVBoxLayout()
        self.task_type_label = QLabel("目前训练类型：")
        self.task_type_label.setFont(font)
        self.task_type_edit.setFixedWidth(400)
        self.task_type_edit.setFixedHeight(50)
        self.task_type_label.setStyleSheet("border:2px solid rgb(186,186,186);\n"
                                           "border-radius:10px\n"
                                           "")
        self.task_type_edit.setText(self.task_type_combo.currentText())
        self.task_type_edit.setEnabled(False)
        self.task_type_edit.setFont(font)
        self.task_type_layout.addWidget(self.task_type_label)
        self.task_type_layout.addWidget(self.task_type_edit)
        # 题目数量
        from zidingyi import Ui_Form
        self.audiorecorder2 = Ui_Form()

        self.quest_num_layout = QVBoxLayout()
        self.quest_num_label = QLabel("题目数量")
        self.quest_num_label.setFont(font)
        self.quest_num_edit = QLineEdit("5")
        self.quest_num_edit.setFont(font)
        self.quest_num_edit.setFixedWidth(200)
        self.quest_num_edit.setFixedHeight(50)
        self.quest_num_edit.setValidator(QtGui.QIntValidator())

        self.quest_num_layout.addWidget(self.quest_num_label)
        self.quest_num_layout.addWidget(self.audiorecorder2)
        self.quest_num_layout.addWidget(self.quest_num_edit)
        # 题目顺序
        self.quest_order_layout = QVBoxLayout()
        self.quest_order_label = QLabel("题目顺序")
        self.quest_order_label.setFont(font)
        self.quest_order_combo = QComboBox()
        self.quest_order_combo.setFont(font)
        self.questCondision = ['正序', '乱序']
        self.quest_order_combo.setFixedHeight(50)
        self.quest_order_combo.addItems(self.questCondision)
        self.quest_order_layout.addWidget(self.quest_order_label)
        self.quest_order_layout.addWidget(self.quest_order_combo)
        # 操作方式
        self.mode_layout = QVBoxLayout()
        self.mode_label = QLabel("操作方式")
        self.mode_label.setFont(font)
        self.mode_combo = QComboBox()
        self.mode_combo.setFont(font)

        self.modeCondision = ['自动', '手动']
        self.mode_combo.setFixedHeight(50)
        self.mode_combo.addItems(self.modeCondision)
        self.mode_combo.currentIndexChanged.connect(self.modeComboClick)
        self.mode_layout.addWidget(self.mode_label)
        self.mode_layout.addWidget(self.mode_combo)
        # 复述次数
        self.repet_layout = QVBoxLayout()
        self.repet_label = QLabel("复述次数")
        self.repet_label.setFont(font)
        self.repet_num_edit = QLineEdit("3")
        self.repet_num_edit.setFont(font)
        self.repet_num_edit.setFixedWidth(200)
        self.repet_num_edit.setFixedHeight(50)
        self.repet_num_edit.setValidator(QtGui.QIntValidator())
        self.repet_layout.addWidget(self.repet_label)
        self.repet_layout.addWidget(self.repet_num_edit)
        self.missionchange()
        # 进入训练
        self.trainBtn = QPushButton("开始训练")
        font = QtGui.QFont()
        font.setPointSize(20)  # 括号里的数字可以设置成自己想要的字体大小
        # font.setFamily("SimHei")  # 黑体
        font.setFamily("SimSun")  # 宋体
        self.trainBtn.setFixedHeight(100)
        self.trainBtn.setFont(font)
        self.trainBtn.clicked.connect(self.trainBtnClick)
        self.trainBtn.setStyleSheet("QPushButton{\n"
                            "     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));\n"
                              "    color: rgb(81, 71, 81);\n"
                            "    box-shadow: 1px 1px 3px;font-size:30px;border-radius: 24px;font-family: 微软雅黑;\n"
                            "}\n"
                            "QPushButton:pressed{\n"
                            "    background:black;\n"
                            "}")
        self.trainBtn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        # 加入排版
        self.task_content_layout.addWidget(self.task_titleLabel)
        self.task_content_layout.addLayout(self.task_type_layout)
        self.task_content_layout.addLayout(self.quest_num_layout)
        self.task_content_layout.addLayout(self.quest_order_layout)
        self.task_content_layout.addLayout(self.mode_layout)
        self.task_content_layout.addLayout(self.repet_layout)
        self.task_content_layout.addWidget(self.trainBtn)
        self.task_content_layout.setAlignment(Qt.AlignLeft)

        #初始化提示
        self.init_label=QLabel("训练初始化中...")
        self.init_label.hide()
        palette = QPalette()
        palette.setColor(QPalette.WindowText, Qt.red)  # 设置字体颜色为红色
        self.init_label.setPalette(palette)
        self.init_label.setFont(font)

        self.layout.addLayout(self.indexlayout)
        self.layout.addLayout(self.pa_layout)
        self.layout.addLayout(self.trainPackLayout)
        self.layout.addLayout(self.task_content_layout)
        self.layout.addWidget(self.init_label)
        self.layout.setAlignment(Qt.AlignTop)
        # self.layout.addLayout(self.Hlayout1)
        # self.layout.addWidget(self.tableView)
        # self.layout.addLayout(self.pa_btns_laylout)
        # self.layout.addLayout(self.Hlayout2)
        self.setLayout(self.layout)

        lab = [self.leftBtn, self.rightBtn]
        tb = [self.exitBtn, self.sys_manage_btn, self.studyBtn, self.user_manage_btn,
              self.IndexBtn]
        # yb = [self.jumpToLabel, self.pageEdit,
        #       self.jumpToButton, self.prevButton, self.backButton]
        font = QtGui.QFont()
        font.setPointSize(15)  # 括号里的数字可以设置成自己想要的字体大小
        # font.setFamily("SimHei")  # 黑体
        font.setFamily("SimSun")  # 宋体
        for i in lab:
            # i.setGraphicsEffect(
            #     QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
            i.setStyleSheet("QPushButton{\n"
                            "    border:none;\n"
                            "    color:rgb(106,106,106);font-size:150px;\n"
                            "}\n"
                            "QPushButton:focus{\n"
                            "    color:rgb(186,186,186);font-size:150px;\n"
                            "}\n"
                             "QPushButton:pressed{\n"
                            "    color:rgba(202, 232, 164, 202);font-size:150px;\n"
                            "}\n"
                            "")

            i.setFont(font)
        for i in tb:
            i.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
            i.setStyleSheet("QPushButton{\n"
                            "    background:rgb(244, 183, 0);\n"
                            "    color: rgb(81, 71, 81);\n"
                            "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                            "}\n"
                            "QPushButton:pressed{\n"
                            "    background:black;\n"
                            "}")
            i.setFont(font)
        # for i in yb:
        #     font = QtGui.QFont()
        #     font.setPointSize(10)  # 括号里的数字可以设置成自己想要的字体大小
        #     i.setFont(font)
    def IndexBtnClick(self):
        from t_main import IndexWindow
        self.mainwindow = IndexWindow()
        self.mainwindow.showFullScreen()
        self.mainwindow.searchButtonClicked()
        self.close()

    def sysManageBtnClicked(self):
        from sys_management import SysManageWindow
        self.sysManageWindow=SysManageWindow()
        self.sysManageWindow.searchButtonClicked()
        self.sysManageWindow.showFullScreen()
        self.close()

    def studyBtnClicked(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://book.yunzhan365.com/vdogo/wpil/mobile/index.html'))

    def taskComboClick(self):
        self.i = self.task_type_combo.currentIndex()
        self.changeTask()

    def modeComboClick(self):

        conditionChoice = self.mode_combo.currentText()
        if (conditionChoice == "自动"):
            self.repet_label.show()
            self.repet_num_edit.show()
        else:
            self.repet_label.hide()
            self.repet_num_edit.hide()
    def missionchange(self):
        if  (self.task_type_combo.currentText() == "配对训练"):
            for i in range(self.repet_layout.count()):
                self.repet_layout.itemAt(i).widget().hide()
            for i in range(self.mode_layout.count()):
                self.mode_layout.itemAt(i).widget().hide()
        else:
            for i in range(self.repet_layout.count()):
                self.repet_layout.itemAt(i).widget().show()
            for i in range(self.mode_layout.count()):
                self.mode_layout.itemAt(i).widget().show()
            self.modeCondision = ['自动','手动']
    def leftBtnClick(self):
        if self.i > 0:
            self.i -= 1
            self.task_type_combo.setCurrentIndex(self.i)
            self.changeTask()

    def rightBtnClick(self):
        if self.i < len(self.searchCondision) - 1:
            self.i += 1
            self.task_type_combo.setCurrentIndex(self.i)
        elif self.i == len(self.searchCondision) - 1:
            self.i = 0
            self.task_type_combo.setCurrentIndex(self.i)
            self.changeTask()

    def changeTask(self):
        image_path = "icon/" + self.task_type_combo.currentText() + ".jpg"
        temp_pic = QtGui.QPixmap(image_path)
        # w = temp_pic.width()
        # h = temp_pic.height()
        # if not w == 0:
        #     if (w / h > 1):
        #         temp_pic = temp_pic.scaledToWidth(800)
        #     else:
        temp_pic = temp_pic.scaledToHeight(700)
        self.train_pic.setPixmap(temp_pic)
        self.train_pic.setFixedWidth(700)
        self.train_pic.setStyleSheet("border:2px solid rgb(186,186,186);\n"
                        "border-radius:10px\n"
                        "")
        self.train_pic.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.train_pic.setScaledContents(True)
        self.task_type_edit.setText(self.task_type_combo.currentText())

    def trainBtnClick(self):
        if (self.quest_num_edit.text() == ""):
            print(QMessageBox.warning(self, '警告', '请输入一个数字', QMessageBox.Yes, QMessageBox.Yes))
            return

        conditionChoice = self.quest_order_combo.currentText()
        if (conditionChoice == "正序"):
            self.is_random = 0
        elif (conditionChoice == "乱序"):
            self.is_random = 1
        conditionChoice = self.mode_combo.currentText()
        if (conditionChoice == "自动"):
            self.is_auto = 0
        elif (conditionChoice == "手动"):
            self.is_auto = 1



        if (self.task_type_combo.currentText() == "元音训练"):
          if (int(self.quest_num_edit.text()) >= 64):
                print(QMessageBox.warning(self, '警告', '目前没有这么多题，请去系统界面增加', QMessageBox.Yes,
                                      QMessageBox.Yes))
                return
          elif (int(self.quest_num_edit.text()) <= 0):
                print(QMessageBox.warning(self, '警告', '请输入一个正数', QMessageBox.Yes,
                                      QMessageBox.Yes))
                return
          else:
            from preCamera import PreCameraWindow
            prewindow = PreCameraWindow()
            prewindow.setModal(True)  # Set the dialog as modal
            prewindow.set_main_window(self)
            prewindow.exec_()  # Display the dialog modally
            self.init_label.show()
            from vowel import VowelWindow
            self.vowelwindow = VowelWindow()
            self.vowelwindow.setTaskNum(self.temp_pano, int(self.quest_num_edit.text()),self.is_random,self.is_auto,int(self.repet_num_edit.text()))
            self.vowelwindow.AssignVowel()
            self.vowelwindow.AssignBtns()
            self.init_label.hide()
            self.vowelwindow.showFullScreen()
            self.close()
        elif (self.task_type_combo.currentText() == "词语训练"):
         if (int(self.quest_num_edit.text()) >= 34):
                print(QMessageBox.warning(self, '警告', '目前没有这么多题，请去系统界面增加', QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
         elif (int(self.quest_num_edit.text()) <= 0):
                print(QMessageBox.warning(self, '警告', '请输入一个正数', QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
         else:
            from preCamera import PreCameraWindow
            prewindow = PreCameraWindow()
            prewindow.setModal(True)  # Set the dialog as modal
            prewindow.set_main_window(self)
            prewindow.exec_()  # Display the dialog modally
            self.init_label.show()
            from word import WordWindow
            self.wordwindow = WordWindow()
            self.wordwindow.setTaskNum(self.temp_pano, int(self.quest_num_edit.text()),self.is_random,self.is_auto,int(self.repet_num_edit.text()))
            self.wordwindow.AssignWord()
            self.wordwindow.AssignBtns()
            self.init_label.hide()
            self.wordwindow.showFullScreen()
            self.close()
        elif (self.task_type_combo.currentText() == "连词成句训练"):
         if (int(self.quest_num_edit.text()) >= 20):
                print(QMessageBox.warning(self, '警告', '目前没有这么多题，请去系统界面增加', QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
         elif (int(self.quest_num_edit.text()) <= 0):
                print(QMessageBox.warning(self, '警告', '请输入一个正数', QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
         else:
            from preCamera import PreCameraWindow
            prewindow = PreCameraWindow()
            prewindow.setModal(True)  # Set the dialog as modal
            prewindow.set_main_window(self)
            prewindow.exec_()  # Display the dialog modally
            self.init_label.show()
            from wordsentence import WSWindow
            self.wswindow = WSWindow()
            self.wswindow.setTaskNum(self.temp_pano, int(self.quest_num_edit.text()),self.is_random,self.is_auto,int(self.repet_num_edit.text()))
            self.wswindow.AssignSentence()
            self.wswindow.AssignBtns()
            self.init_label.hide()
            self.wswindow.showFullScreen()
            self.close()
        elif (self.task_type_combo.currentText() == "配对训练"):
         if (int(self.quest_num_edit.text()) >= 12):
                print(QMessageBox.warning(self, '警告', '目前没有这么多题，请去系统界面增加', QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
         elif (int(self.quest_num_edit.text()) <= 0):
                print(QMessageBox.warning(self, '警告', '请输入一个正数', QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
         else:
            self.is_auto = 1
            self.init_label.show()
            from peidui import PdWindow
            self.pdwindow = PdWindow()
            self.pdwindow.setTaskNum(self.temp_pano, int(self.quest_num_edit.text()),self.is_random,self.is_auto,int(self.repet_num_edit.text()))
            self.pdwindow.AssignWord()
            self.pdwindow.chooseBtns()
            self.init_label.hide()
            self.pdwindow.showFullScreen()
            self.close()

    def userManageBtnClicked(self):
        from user_management import ManageWindow
        self.userManageWindow = ManageWindow()
        self.userManageWindow.showFullScreen()
        self.userManageWindow.searchButtonClicked()
        self.close()

    def setNo(self, no_value):
        self.temp_pano = str(no_value)
        self.selected_pa_label.setText("欢迎"+self.temp_pano)

    def exitBtnClick(self):
        ret = QMessageBox.information(self, "提示", "是否退出系统?", QMessageBox.Yes, QMessageBox.No)
        if (ret == QMessageBox.Yes):
            sys.exit(app.exec_())
        else:
            return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    mainWindow = TrainWindow()
    mainWindow.showFullScreen()
    # mainWindow.show()
    sys.exit(app.exec_())