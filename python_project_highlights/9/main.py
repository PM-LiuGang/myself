# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 600)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontianjiashuiyin = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("G:/F盘/例图/图标/16×16(像素）/ICO/图标 (23).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontianjiashuiyin.setIcon(icon)
        self.actiontianjiashuiyin.setObjectName("actiontianjiashuiyin")
        self.actionpiliangchongmingming = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("G:/F盘/例图/图标/16×16(像素）/ICO/图标 (217).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpiliangchongmingming.setIcon(icon1)
        self.actionpiliangchongmingming.setObjectName("actionpiliangchongmingming")
        self.menu.addAction(self.actiontianjiashuiyin)
        self.menu.addAction(self.actionpiliangchongmingming)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片批量处理器"))
        self.menu.setTitle(_translate("MainWindow", "主菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "|| 关于"))
        self.actiontianjiashuiyin.setText(_translate("MainWindow", "添加水印"))
        self.actionpiliangchongmingming.setText(_translate("MainWindow", "批量重命名"))
