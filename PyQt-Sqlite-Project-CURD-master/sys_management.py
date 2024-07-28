import os

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,sqlite3



class SysManageWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(SysManageWindow, self).__init__(*args, **kwargs)
        self.resize(700, 500)
        self.setWindowTitle("欢迎使用康复训练系统")
        icon = QIcon()
        icon.addPixmap(QPixmap('logo.jpg'))
        # icon = QIcon("./back.jpg")
        self.setWindowIcon(icon)
        self.currentTable = "words"
        self.name="word_name"
        self.no="word_no"
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
        # 当前数据名字
        self.temp_dataname = ""
        # 当前数据编号
        self.temp_datano = ""
        self.setUpUI()

    def setUpUI(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        # 添加sql语句
        self.c.close()
        self.setFixedSize(960, 700)

        # 选择数据
        self.layout = QVBoxLayout()
        self.indexlayout = QHBoxLayout()
        self.pa_layout = QHBoxLayout()
        self.Hlayout1 = QHBoxLayout()
        self.pa_btns_laylout = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

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
        self.IndexBtn.setStyleSheet("QPushButton{\n"
                                    "    background:orange;\n"
                                    "    color:white;\n"
                                    "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:black;\n"
                                    "}")
        self.IndexBtn.setFixedWidth(index_btn_len)
        self.IndexBtn.setIcon(QIcon(QPixmap("indexres/shouye.png")))

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
                                           "    background:orange;\n"
                                           "    color:white;\n"
                                           "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                                           "}\n"
                                           "QPushButton:pressed{\n"
                                           "    background:black;\n"
                                           "}")
        self.trainMissionBtn.setFixedWidth(index_btn_len)

        self.user_manage_btn = QtWidgets.QPushButton("用户管理")
        self.user_manage_btn.setObjectName('index_button')
        self.user_manage_btn.setObjectName('index_button')
        self.user_manage_btn.move(250, 100)
        self.user_manage_btn.setFixedSize(150, 50)
        self.user_manage_btn.setStyleSheet("QPushButton{\n"
                                           "    background:orange;\n"
                                           "    color:white;\n"
                                           "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                                           "}\n"
                                           "QPushButton:pressed{\n"
                                           "    background:black;\n"
                                           "}")
        self.user_manage_btn.setFixedWidth(index_btn_len)

        self.sys_manage_btn = QtWidgets.QPushButton("系统管理")
        self.sys_manage_btn.setObjectName('index_button')
        self.sys_manage_btn.move(250, 100)
        self.sys_manage_btn.setFixedSize(150, 50)
        self.sys_manage_btn.setStyleSheet("QPushButton{\n"
                                          "    background:orange;\n"
                                          "    color:white;\n"
                                          "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "    background:black;\n"
                                          "}")
        self.sys_manage_btn.setObjectName('index_button')
        self.sys_manage_btn.setFixedWidth(index_btn_len)
        self.sys_manage_btn.setStyleSheet("QPushButton{\n"
                                           "    background:rgb(81, 71, 81);\n"
                                           "    color: white;\n"
                                           "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-family: 微软雅黑;\n"
                                           "}\n"
                                           "QPushButton:pressed{\n"
                                           "    background:black;\n"
                                           "}")
        self.sys_manage_btn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.studyBtn = QtWidgets.QPushButton("教 程")
        self.studyBtn.setObjectName('index_button')
        self.studyBtn.move(250, 100)
        self.studyBtn.setFixedSize(150, 50)
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

        # 导航栏按钮
        self.IndexBtn.clicked.connect(self.IndexBtnClick)
        self.trainMissionBtn.clicked.connect(self.trainMissionBtnClick)
        self.user_manage_btn.clicked.connect(self.userManageBtnClicked)
        self.exitBtn.clicked.connect(self.exitBtnClick)

        # 当前已选择数据

        self.selected_pa_label = QLabel("当前选择的数据为：无")
        self.pa_layout.addWidget(self.selected_pa_label)

        # Hlayout1，查询功能
        self.searchEdit = QLineEdit()
        self.searchEdit.setFixedHeight(32)
        font = QFont()
        font.setPixelSize(15)
        self.searchEdit.setFont(font)

        self.searchButton = QPushButton("查询")
        self.searchButton.setFixedHeight(50)
        self.searchButton.setFixedWidth(150)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton{\n"
                                        "    background:rgb(244, 183, 100);\n"
                                        "    color: rgb(81, 71, 81);\n"
                                        "    box-shadow: 1px 1px 3px;font-size:18px;border-radius: 24px;font-size:20px;font-family: 微软雅黑;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background:black;\n"
                                        "}")
        self.searchButton.setIcon(QIcon(QPixmap("indexres/deng.png")))

        self.condisionComboBox = QComboBox()
        searchCondision = ['按词语查询','按句子查询','按连词成句查询','配对词语查询']
        self.condisionComboBox.setFixedHeight(52)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)
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
        self.condisionComboBox.currentIndexChanged.connect(self.onConditionComboBoxChanged)

        # self.Hlayout1.addWidget(self.searchEdit)
        # self.Hlayout1.addWidget(self.searchButton)
        # self.Hlayout1.addWidget(self.condisionComboBox)
        self.trainMissionBtn.setIcon(QIcon(QPixmap("indexres/yinpin.png")))
        self.user_manage_btn.setIcon(QIcon(QPixmap("indexres/yonghu.png")))
        self.sys_manage_btn.setIcon(QIcon(QPixmap("indexres/shezhi.png")))
        self.studyBtn.setIcon(QIcon(QPixmap("indexres/dianji.png")))
        self.exitBtn.setIcon(QIcon(QPixmap("indexres/tuichu.png")))
        self.searchButton.setIcon(QIcon(QPixmap("indexres/sousuo.png")))
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

        # 增删改
        self.addBtn = QPushButton("增加")
        self.deleteBtn = QPushButton("删除")
        self.alterBtn = QPushButton("修改查看")
        self.pa_btns_laylout.addWidget(self.addBtn)
        self.pa_btns_laylout.addWidget(self.deleteBtn)
        self.pa_btns_laylout.addWidget(self.alterBtn)
        self.addBtn.clicked.connect(self.addBtnClicked)
        self.deleteBtn.clicked.connect(self.deleteBtnClicked)
        self.alterBtn.clicked.connect(self.alterBtnClicked)
        self.studyBtn.clicked.connect(self.studyBtnClicked)

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

        # tableView
        # 数据信息
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('database.db')
        self.db.open()
        self.tableView = QTableView()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        self.func_mappingSignal()
        # self.showPaImage()
        index = self.tableView.currentIndex()  # 取得当前选中行的index
        self.tableView.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 232, 164, 202), stop:1 rgba(255, 238, 112, 169));font: '宋体';color: black;padding-left: 5px;border-left:0px solid #000;border-right:1px solid lightgreen;border-top:0px solid #000;}")

        self.tableView.setStyleSheet("selection-background-color:lightblue;")

        hearder = self.tableView.verticalHeader()
        hearder.hide()
        # self.model = QStandardItemModel()
        # self.tableView.setModel(self.model)
        # self.model = QStandardItemModel(5, 3)  # 创建一个标准的数据源model
        # self.model.setHorizontalHeaderLabels(["id", "姓名", "年龄"])  # 设置表格的表头名称
        # model=self.tableView.model()
        # print(model.itemData(model.index(index.row(), 0)))
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

        lab = [self.addBtn, self.deleteBtn,  self.alterBtn]
        tb = [self.exitBtn, self.studyBtn, self.user_manage_btn, self.trainMissionBtn,
              self.IndexBtn]
        yb = [self.jumpToLabel, self.pageEdit,
              self.jumpToButton, self.prevButton, self.backButton]
        font = QtGui.QFont()
        font.setPointSize(15)  # 括号里的数字可以设置成自己想要的字体大小
        # font.setFamily("SimHei")  # 黑体
        font.setFamily("SimSun")  # 宋体
        for i in lab:
            i.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
            i.setStyleSheet("QPushButton{\n"
                                        "    border:none;\n"
                                        "    color:rgb(106,106,106);\n"
                                        "}\n"
                                        "QPushButton:focus{\n"
                                        "    color:rgb(186,186,186);\n"
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
        for i in yb:
            font = QtGui.QFont()
            font.setPointSize(10)  # 括号里的数字可以设置成自己想要的字体大小
            i.setFont(font)

        # lab = [self.addBtn, self.deleteBtn, self.generateBtn, self.alterBtn]
        # tb = [self.exitBtn, self.sys_manage_btn, self.studyBtn, self.user_manage_btn, self.trainMissionBtn,
        #       self.IndexBtn]
        # yb = [self.jumpToLabel, self.pageEdit,
        #       self.jumpToButton, self.prevButton, self.backButton]
        # font = QtGui.QFont()
        # font.setPointSize(15)  # 括号里的数字可以设置成自己想要的字体大小
        # # font.setFamily("SimHei")  # 黑体
        # font.setFamily("SimSun")  # 宋体
        # for i in lab:
        #     i.setFont(font)
        # for i in tb:
        #     i.setFont(font)
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

    def userManageBtnClicked(self):
        from user_management import ManageWindow
        self.userManageWindow = ManageWindow()
        self.userManageWindow.showFullScreen()
        self.userManageWindow.searchButtonClicked()
        self.close()

    def func_mappingSignal(self):
        self.tableView.clicked.connect(self.func_test)
    def trainMissionBtnClick(self):
        print(QMessageBox.warning(self, "提示", "请点击“首页”选择患者后点击“训练任务”", QMessageBox.Yes, QMessageBox.Yes))


    def func_test(self, item):
        # http://www.python-forum.org/viewtopic.php?f=11&t=16817
        cellContent = item.data()
        print(cellContent)  # test
        sf = "You clicked on {0}x{1}".format(item.column(), item.row())
        print(sf)
        if not self.currentTable == "sentence_word":
            # 获取数据名字
            NewIndex = self.tableView.currentIndex().siblingAtColumn(1)
            Name = NewIndex.data()
            self.selected_pa_label.setText("当前选择的数据为：" + Name)
            self.temp_dataname = Name
            # 获取数据编号
            user_no_index = self.tableView.currentIndex().siblingAtColumn(0)
            self.temp_datano = user_no_index.data()
        else:
            # 获取数据名字
            NewIndex = self.tableView.currentIndex().siblingAtColumn(3)
            Name = NewIndex.data()
            self.selected_pa_label.setText("当前选择的数据为：" + Name)
            self.temp_dataname = Name
            # 获取数据编号
            user_no_index = self.tableView.currentIndex().siblingAtColumn(2)
            self.temp_datano = user_no_index.data()

    def addBtnClicked(self):
        try:
            if self.currentTable=="words":
                from addword import addwordDialog
                addDialog = addwordDialog(self)
                # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
                addDialog.show()
                addDialog.exec_()
            elif self.currentTable == "pdwords":
                from addpdwords import addwordDialog
                addDialog = addwordDialog(self)
                # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
                addDialog.show()
                addDialog.exec_()
            elif self.currentTable == "sentence":
                from addsentence import addsentenceDialog
                addDialog = addsentenceDialog(self)
                # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
                addDialog.show()
                addDialog.exec_()
            elif self.currentTable == "sentence_word":
                from addsw import addswDialog
                addDialog = addswDialog(self)
                # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
                addDialog.show()
                addDialog.exec_()
            self.searchButtonClicked()
        except Exception as e:
            print(f'Error: {e}')
    def deleteBtnClicked(self):
        try:
            if (self.temp_datano == ""):
                print(QMessageBox.warning(self, "警告", "请选择一条数据", QMessageBox.Yes, QMessageBox.Yes))
            else:
                ret = QMessageBox.information(self, "提示", "是否删除数据" + self.temp_dataname, QMessageBox.Yes, QMessageBox.No)
                if (ret == QMessageBox.Yes):
                    db = QSqlDatabase.addDatabase("QSQLITE")
                    db.setDatabaseName('database.db')
                    db.open()
                    query = QSqlQuery()
                    # 如果已存在，则update Book表的现存量，剩余可借量，不存在，则insert Book表，同时insert buyordrop表
                    sql = "SELECT * FROM %s WHERE %s ='%s'" % (self.currentTable,self.no,self.temp_datano)
                    query.exec_(sql)
                    # 提示不存在
                    if not (query.next()):
                        print(QMessageBox.warning(self, "警告", "该数据不存在", QMessageBox.Yes, QMessageBox.Yes))
                        return
                    else:
                        sql = "DELETE FROM %s WHERE %s='%s'" % (self.currentTable,self.no,self.temp_datano)
                        query.exec_(sql)
                        db.commit()
                        if self.currentTable=="words":
                            temp_path="word"
                            os.remove("audio/" + temp_path + "/" + str(self.temp_datano) + ".mp3")
                            temp_image_path="image/"+self.temp_dataname+".jpg"
                            if os.path.exists(temp_image_path):
                                os.remove(temp_image_path)
                        elif self.currentTable == "sentence":
                            temp_path="sentence"
                            os.remove("audio/"+temp_path+"/"+str(self.temp_datano)+".mp3")
                    print(QMessageBox.information(self, "提示", "删除成功，数据" + self.temp_dataname + "已删除", QMessageBox.Yes,
                                                  QMessageBox.Yes))
                    self.temp_datano = ""
                    self.temp_dataname = ""
                    self.selected_pa_label.setText("当前选择的数据为：")
            self.searchButtonClicked()
        except Exception as e:
            print(f'Error: {e}')

    def studyBtnClicked(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://book.yunzhan365.com/vdogo/wpil/mobile/index.html'))

    def alterBtnClicked(self):
        try:
            if (self.temp_datano == ""):
                print(QMessageBox.warning(self, "警告", "请选择一条数据", QMessageBox.Yes, QMessageBox.Yes))
            else:
                if self.currentTable=="words":
                    # 初始化修改窗口
                    from alterword import alterWordDialog
                    self.alterDialog = alterWordDialog()
                    self.alterDialog.setNo(self.temp_datano)
                    # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
                    self.alterDialog.fillContent()
                    self.alterDialog.show()
                    self.alterDialog.exec_()
                elif self.currentTable=="pdwords":
                    # 初始化修改窗口
                    from alterpdwords import alterWordDialog
                    self.alterDialog = alterWordDialog()
                    self.alterDialog.setNo(self.temp_datano)
                    # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
                    self.alterDialog.fillContent()
                    self.alterDialog.show()
                    self.alterDialog.exec_()
                elif self.currentTable == "sentence":
                    from altersentence import altersentenceDialog
                    self.alterDialog = altersentenceDialog()
                    self.alterDialog.setNo(self.temp_datano)
                    # addDialog.add_pa_success_signal.connect(self.window.searchButtonClicked)
                    self.alterDialog.fillContent()
                    self.alterDialog.show()
                    self.alterDialog.exec_()
                self.searchButtonClicked()
        except Exception as e:
            print(f'Error: {e}')

    # 展示图片
    # def showPaImage(self):
    #     # imageItem = QStandardItem(QIcon("pa_head/pa_0"))
    #     image_path="pa_head/pa_0"
    #     imageItem = QtGui.QPixmap(image_path).scaled(300, 300)
    #     img = mping.imread('path')  # 相对路径
    #     self.tableView.setItem(0, 6, imageItem)
    # 查询
    def recordQuery(self, index):
        try:
            queryCondition = ""
            conditionChoice = self.condisionComboBox.currentText()
            if (conditionChoice == "按词语查询"):
                conditionChoice = 'word_no'
                self.name="word_name"
                self.no = "word_no"
                self.currentTable="words"
                self.alterBtn.show()
                self.selected_pa_label.setText("当前选择的数据为：")
                self.temp_dataname = ""
                self.temp_datano =""
            elif (conditionChoice == "按句子查询"):
                conditionChoice = 'sentence_no'
                self.name = "sentence_name"
                self.no = "sentence_no"
                self.currentTable = "sentence"
                self.alterBtn.show()
                self.selected_pa_label.setText("当前选择的数据为：")
                self.temp_dataname = ""
                self.temp_datano = ""
            elif (conditionChoice == "按连词成句查询"):
                conditionChoice = 'sw_no'
                self.name = "sentence_name"
                self.no = "sentence_no"
                self.currentTable = "sentence_word"
                self.alterBtn.hide()
                self.selected_pa_label.setText("当前选择的数据为：")
                self.temp_dataname = ""
                self.temp_datano = ""
            elif (conditionChoice == "配对词语查询"):
                conditionChoice = 'pdword_no'
                self.name = "pdword_name"
                self.no = "pdword_no"
                self.currentTable = "pdwords"
                # self.alterBtn.hide()
                self.alterBtn.show()
                self.selected_pa_label.setText("当前选择的数据为：")
                self.temp_dataname = ""
                self.temp_datano = ""

            if (self.searchEdit.text() == ""):
                queryCondition = "select * from "+self.currentTable
                self.queryModel.setQuery(queryCondition)
                self.totalRecord = self.queryModel.rowCount()
                self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
                label = "/" + str(int(self.totalPage)) + "页"
                self.pageLabel.setText(label)
                queryCondition = (
                        "select * from %s ORDER BY %s  limit %d,%d " % (self.currentTable,conditionChoice, index, self.pageRecord))
                self.queryModel.setQuery(queryCondition)
                self.setButtonStatus()
                return

            # 得到模糊查询条件
            temp = self.searchEdit.text()
            s = '%'
            for i in range(0, len(temp)):
                s = s + temp[i] + "%"
            queryCondition = ("SELECT * FROM %s WHERE %s LIKE '%s' ORDER BY %s " % (
                self.currentTable, self.name, s, conditionChoice))
            self.queryModel.setQuery(queryCondition)
            self.totalRecord = self.queryModel.rowCount()
            # 当查询无记录时的操作
            if (self.totalRecord == 0):
                print(QMessageBox.information(self, "提醒", "查询无记录", QMessageBox.Yes, QMessageBox.Yes))
                queryCondition = ("select * from %s " % (self.currentTable))
                self.queryModel.setQuery(queryCondition)
                self.totalRecord = self.queryModel.rowCount()
                self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
                label = "/" + str(int(self.totalPage)) + "页"
                self.pageLabel.setText(label)
                queryCondition = (
                        "select * from %s ORDER BY %s  limit %d,%d " % (self.currentTable,conditionChoice, index, self.pageRecord))
                self.queryModel.setQuery(queryCondition)
                self.setButtonStatus()
                return
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
            queryCondition = ("SELECT * FROM %s WHERE %s LIKE '%s' ORDER BY %s LIMIT %d,%d " % (
                self.currentTable,self.name, s, conditionChoice, index, self.pageRecord))
            self.queryModel.setQuery(queryCondition)
            self.setButtonStatus()
            return
        except Exception as e:
            print(f'Error: {e}')
    def onConditionComboBoxChanged(self):
        self.searchButtonClicked()

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
        self.queryModel.setQuery("SELECT * FROM "+self.currentTable)
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
        ret = QMessageBox.information(self, "提示", "是否退出系统?", QMessageBox.Yes, QMessageBox.No)
        if (ret == QMessageBox.Yes):
            sys.exit(app.exec_())
        else:
            return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SysManageWindow()
    window.showFullScreen()
    window.searchButtonClicked()
    sys.exit(app.exec_())