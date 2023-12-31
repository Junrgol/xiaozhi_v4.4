# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import yaml

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(260, 470)
        setting_path='/'.join(sys.argv[0].replace("\\", '/').split('/')[:-1])+'/common/setting.yaml'
        with open(setting_path, 'r', encoding='UTF-8') as stream:
            setting_data = yaml.safe_load(stream)
        size=QtCore.QSize(setting_data['WindowSize'], setting_data['WindowSize'])
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 1200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("common/pic/robot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 0, 0, -1)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.toolButton_1_8 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_8.setMinimumSize(size)
        self.toolButton_1_8.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_8.setText("")
        self.toolButton_1_8.setIconSize(size)
        self.toolButton_1_8.setObjectName("toolButton_1_8")
        self.gridLayout_4.addWidget(self.toolButton_1_8, 2, 3, 1, 1)
        self.toolButton_1_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_3.setMinimumSize(size)
        self.toolButton_1_3.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_3.setText("")
        self.toolButton_1_3.setIconSize(size)
        self.toolButton_1_3.setObjectName("toolButton_1_3")
        self.gridLayout_4.addWidget(self.toolButton_1_3, 1, 2, 1, 1)
        self.toolButton_1_12 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_12.setMinimumSize(size)
        self.toolButton_1_12.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_12.setBaseSize(QtCore.QSize(0, 0))
        self.toolButton_1_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_12.setText("")
        self.toolButton_1_12.setIconSize(size)
        self.toolButton_1_12.setObjectName("toolButton_1_12")
        self.gridLayout_4.addWidget(self.toolButton_1_12, 4, 3, 1, 1)
        self.toolButton_1_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_6.setMinimumSize(size)
        self.toolButton_1_6.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_6.setBaseSize(QtCore.QSize(0, 0))
        self.toolButton_1_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_6.setText("")
        self.toolButton_1_6.setIconSize(size)
        self.toolButton_1_6.setObjectName("toolButton_1_6")
        self.gridLayout_4.addWidget(self.toolButton_1_6, 2, 1, 1, 1)
        self.toolButton_1_9 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_9.setMinimumSize(size)
        self.toolButton_1_9.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_9.setText("")
        self.toolButton_1_9.setIconSize(size)
        self.toolButton_1_9.setObjectName("toolButton_1_9")
        self.gridLayout_4.addWidget(self.toolButton_1_9, 4, 0, 1, 1)
        self.toolButton_1_11 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_11.setMinimumSize(size)
        self.toolButton_1_11.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_11.setText("")
        self.toolButton_1_11.setIconSize(size)
        self.toolButton_1_11.setObjectName("toolButton_1_11")
        self.gridLayout_4.addWidget(self.toolButton_1_11, 4, 2, 1, 1)
        self.toolButton_1_7 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_7.setMinimumSize(size)
        self.toolButton_1_7.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_7.setText("")
        self.toolButton_1_7.setIconSize(size)
        self.toolButton_1_7.setObjectName("toolButton_1_7")
        self.gridLayout_4.addWidget(self.toolButton_1_7, 2, 2, 1, 1)
        self.toolButton_1_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_4.setMinimumSize(size)
        self.toolButton_1_4.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_4.setBaseSize(QtCore.QSize(0, 0))
        self.toolButton_1_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_4.setText("")
        self.toolButton_1_4.setIconSize(size)
        self.toolButton_1_4.setObjectName("toolButton_1_4")
        self.gridLayout_4.addWidget(self.toolButton_1_4, 1, 3, 1, 1)
        self.toolButton_1_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_5.setMinimumSize(size)
        self.toolButton_1_5.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_5.setText("")
        self.toolButton_1_5.setIconSize(size)
        self.toolButton_1_5.setObjectName("toolButton_1_5")
        self.gridLayout_4.addWidget(self.toolButton_1_5, 2, 0, 1, 1)
        self.toolButton_1_10 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_10.setMinimumSize(size)
        self.toolButton_1_10.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_10.setText("")
        self.toolButton_1_10.setIconSize(size)
        self.toolButton_1_10.setObjectName("toolButton_1_10")
        self.gridLayout_4.addWidget(self.toolButton_1_10, 4, 1, 1, 1)
        self.toolButton_1_1 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_1.setMinimumSize(size)
        self.toolButton_1_1.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/ceshi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_1_1.setIcon(icon1)
        self.toolButton_1_1.setIconSize(size)
        self.toolButton_1_1.setCheckable(False)
        self.toolButton_1_1.setObjectName("toolButton_1_1")
        self.gridLayout_4.addWidget(self.toolButton_1_1, 1, 0, 1, 1)
        self.toolButton_1_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1_2.setMinimumSize(size)
        self.toolButton_1_2.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_1_2.setText("")
        self.toolButton_1_2.setIcon(icon1)
        self.toolButton_1_2.setIconSize(size)
        self.toolButton_1_2.setObjectName("toolButton_1_2")
        self.gridLayout_4.addWidget(self.toolButton_1_2, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 4, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolButton_0_8 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_8.setMinimumSize(size)
        self.toolButton_0_8.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_8.setText("")
        self.toolButton_0_8.setIconSize(size)
        self.toolButton_0_8.setObjectName("toolButton_0_8")
        self.gridLayout_3.addWidget(self.toolButton_0_8, 2, 3, 1, 1)
        self.toolButton_0_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_3.setMinimumSize(size)
        self.toolButton_0_3.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_3.setText("")
        self.toolButton_0_3.setIconSize(size)
        self.toolButton_0_3.setObjectName("toolButton_0_3")
        self.gridLayout_3.addWidget(self.toolButton_0_3, 1, 2, 1, 1)
        self.toolButton_0_12 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_12.setMinimumSize(size)
        self.toolButton_0_12.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_12.setBaseSize(QtCore.QSize(0, 0))
        self.toolButton_0_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_12.setText("")
        self.toolButton_0_12.setIconSize(size)
        self.toolButton_0_12.setObjectName("toolButton_0_12")
        self.gridLayout_3.addWidget(self.toolButton_0_12, 4, 3, 1, 1)
        self.toolButton_0_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_6.setMinimumSize(size)
        self.toolButton_0_6.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_6.setBaseSize(QtCore.QSize(0, 0))
        self.toolButton_0_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_6.setText("")
        self.toolButton_0_6.setIconSize(size)
        self.toolButton_0_6.setObjectName("toolButton_0_6")
        self.gridLayout_3.addWidget(self.toolButton_0_6, 2, 1, 1, 1)
        self.toolButton_0_9 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_9.setMinimumSize(size)
        self.toolButton_0_9.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_9.setText("")
        self.toolButton_0_9.setIconSize(size)
        self.toolButton_0_9.setObjectName("toolButton_0_9")
        self.gridLayout_3.addWidget(self.toolButton_0_9, 4, 0, 1, 1)
        self.toolButton_0_11 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_11.setMinimumSize(size)
        self.toolButton_0_11.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_11.setText("")
        self.toolButton_0_11.setIconSize(size)
        self.toolButton_0_11.setObjectName("toolButton_0_11")
        self.gridLayout_3.addWidget(self.toolButton_0_11, 4, 2, 1, 1)
        self.toolButton_0_7 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_7.setMinimumSize(size)
        self.toolButton_0_7.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_7.setText("")
        self.toolButton_0_7.setIconSize(size)
        self.toolButton_0_7.setObjectName("toolButton_0_7")
        self.gridLayout_3.addWidget(self.toolButton_0_7, 2, 2, 1, 1)
        self.toolButton_0_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_4.setMinimumSize(size)
        self.toolButton_0_4.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_4.setBaseSize(QtCore.QSize(0, 0))
        self.toolButton_0_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_4.setText("")
        self.toolButton_0_4.setIconSize(size)
        self.toolButton_0_4.setObjectName("toolButton_0_4")
        self.gridLayout_3.addWidget(self.toolButton_0_4, 1, 3, 1, 1)
        self.toolButton_0_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_2.setMinimumSize(size)
        self.toolButton_0_2.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_2.setText("")
        self.toolButton_0_2.setIconSize(size)
        self.toolButton_0_2.setObjectName("toolButton_0_2")
        self.gridLayout_3.addWidget(self.toolButton_0_2, 1, 1, 1, 1)
        self.toolButton_0_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_5.setMinimumSize(size)
        self.toolButton_0_5.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_5.setText("")
        self.toolButton_0_5.setIconSize(size)
        self.toolButton_0_5.setObjectName("toolButton_0_5")
        self.gridLayout_3.addWidget(self.toolButton_0_5, 2, 0, 1, 1)
        self.toolButton_0_10 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_10.setMinimumSize(size)
        self.toolButton_0_10.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_10.setText("")
        self.toolButton_0_10.setIconSize(size)
        self.toolButton_0_10.setObjectName("toolButton_0_10")
        self.gridLayout_3.addWidget(self.toolButton_0_10, 4, 1, 1, 1)
        self.toolButton_0_1 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_0_1.setMinimumSize(size)
        self.toolButton_0_1.setMaximumSize(QtCore.QSize(500, 500))
        self.toolButton_0_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_0_1.setText("")
        #self.toolButton_0_1.setStyleSheet("border-style:solid;border-color:red;border-width:1px;")
        #self.toolButton_0_2.setStyleSheet("border-style:solid;border-color:red;border-width:1px;")
        #print(self.toolButton_0_1.styleSheet()=="")
        self.toolButton_0_1.setIconSize(size)
        self.toolButton_0_1.setObjectName("toolButton_0_1")
        self.gridLayout_3.addWidget(self.toolButton_0_1, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(6)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_file = QtWidgets.QAction(MainWindow)
        self.actionopen_file.setObjectName("actionopen_file")
        self.startup = QtWidgets.QAction(MainWindow)
        self.startup.setObjectName("startup")
        self.menu.addAction(self.actionopen_file)
        self.menu.addAction(self.startup)
        self.setting = QtWidgets.QAction(MainWindow)
        self.setting.setObjectName("setting")
        self.menu.addAction(self.actionopen_file)
        self.menu.addAction(self.setting)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小智助手"))
        self.label.setText(_translate("MainWindow", "通用"))
        self.label_2.setText(_translate("MainWindow", "个性化"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionopen_file.setText(_translate("MainWindow", "open file"))
        self.startup.setText(_translate("MainWindow", "设置自启"))
        self.setting.setText(_translate("MainWindow", "参数设置"))
