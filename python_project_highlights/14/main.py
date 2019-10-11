# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import qApp,QFileDialog

import sys
import pandas as pd
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

# root = ""
root = r'C:\Users\admin\Desktop\myself\python_project_highlights\14\XS1'
fileNum = 0
myrow = 0


#自定义函数SaveExcel用于保存数据到Excel
def SaveExcel(df,isChecked):
    # 将提取后的数据保存到Excel
    if (isChecked):
        writer = pd.ExcelWriter('mycell.xls')
    else:
        # global temproot  # dataEXCEL undefined
        writer = pd.ExcelWriter('mycell.xls')
        # writer = pd.ExcelWriter(temproot + '\mycell.xls') # dataEXCEL
    df.to_excel(writer, 'sheet1')
    writer.save()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 647)
        ###########################
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        ##########################
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list1 = QtWidgets.QListView(self.centralwidget)
        self.list1.setGeometry(QtCore.QRect(0, 10, 191, 471))
        self.list1.setObjectName("list1")
        '''
        dataEXCEL 
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text1.sizePolicy().hasHeightForWidth())
        '''
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 10, 481, 471))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.text2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(138, 539, 461, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.text2.setFont(font)
        self.text2.setObjectName("text2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(10, 490, 54, 12))
        self.label.setObjectName("label")
        self.rButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rButton1.setGeometry(QtCore.QRect(10, 512, 131, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.rButton1.setFont(font)
        self.rButton1.setObjectName("rButton1")
        self.rButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rButton2.setGeometry(QtCore.QRect(10, 540, 101, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.rButton2.setFont(font)
        self.rButton2.setObjectName("rButton2")
        self.viewButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(610, 537, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.viewButton.setFont(font)
        self.viewButton.setObjectName("viewButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.button1 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/图标-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button1.setIcon(icon)
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/图标-02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button2.setIcon(icon1)
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/图标-03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button3.setIcon(icon2)
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/图标-04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button4.setIcon(icon3)
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/图标-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button5.setIcon(icon4)
        self.button5.setObjectName("button5")
        self.button6 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/图标-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button6.setIcon(icon5)
        self.button6.setObjectName("button6")
        self.button7 = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/图标-07.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button7.setIcon(icon6)
        self.button7.setObjectName("button7")
        self.toolBar.addAction(self.button1)
        self.toolBar.addAction(self.button2)
        self.toolBar.addAction(self.button3)
        self.toolBar.addAction(self.button4)
        self.toolBar.addAction(self.button5)
        self.toolBar.addAction(self.button6)
        self.toolBar.addAction(self.button7)

        self.button7.triggered.connect(qApp.quit)
        # 单击工具栏按钮触发自定义槽函数
        self.button1.triggered.connect(self.click1)
        self.button2.triggered.connect(self.click2)
        self.button3.triggered.connect(self.click3)
        self.button4.triggered.connect(self.click4)
        self.button5.triggered.connect(self.click5)
        self.button6.triggered.connect(self.click6)
        #单击"浏览"按钮，选择文件存储路径
        self.viewButton.clicked.connect(self.viewButton_click)
        # 单击QListView列表触发自定义的槽函数
        self.list1.clicked.connect(self.clicked)
        # 设置Dataframe对象显示所有列
        pd.set_option('display.max_columns', None)
        # 设置Dataframe对象列宽为200，默认为50
        pd.set_option('max_colwidth', 200)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "输出选项"))
        self.rButton1.setText(_translate("MainWindow", "保存在源文件夹内："))
        self.rButton2.setText(_translate("MainWindow", "自定义文件夹："))
        self.viewButton.setText(_translate("MainWindow", "浏览"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.button1.setText(_translate("MainWindow", "导入excel"))
        self.button1.setToolTip(_translate("MainWindow", "导入excel"))
        self.button2.setText(_translate("MainWindow", "多表导入"))
        self.button2.setToolTip(_translate("MainWindow", "多表导入"))
        self.button3.setText(_translate("MainWindow", "多表汇总"))
        self.button3.setToolTip(_translate("MainWindow", "多表汇总"))
        self.button4.setText(_translate("MainWindow", "多表分组统计"))
        self.button4.setToolTip(_translate("MainWindow", "多表分组统计"))
        self.button5.setText(_translate("MainWindow", "多表数据排行"))
        self.button5.setToolTip(_translate("MainWindow", "多表数据排行"))
        self.button6.setText(_translate("MainWindow", "生成图表"))
        self.button6.setToolTip(_translate("MainWindow", "生成图表"))
        self.button7.setText(_translate("MainWindow", "退出"))
        self.button7.setToolTip(_translate("MainWindow", "退出"))

    def click1(self):
        global root
        root = QFileDialog.getExistingDirectory(self, '选择文件夹', '/')
        mylist = []
        for dirpath, dirnames, filenames in os.walk(root):
            for filepath in filenames:
                mylist.append(os.path.join(filepath)) # 这还能单独使用
        self.model = QtCore.QStringListModel()
        self.model.setStringList(mylist)  # ?
        self.list1.setModel(self.model)
        self.list1 = mylist

    # 单击左侧目录右侧表格显示数据
    def clicked(self, qModelIndex):
        global root
        global myrow
        myrow=qModelIndex.row()  # ?
        # 获取当前选中行的数据
        a = root + r'\\n' + str(self.list1[qModelIndex.row()])
        df = pd.DataFrame(pd.read_excel(a))
        self.textEdit.setText(str(df))

    #提取列数据
    def click2(self):
        global root
        global myrow
        # 获取当前选中行的数据
        a = root + r'\\' + str(self.list1[myrow])
        df = pd.DataFrame(pd.read_excel(a))
        #显示指定列数据
        df1 = df[['买家会员名', '收货人姓名', '联系手机','宝贝标题']]
        self.textEdit.setText(str(df1)) # ? 这不是返回一大串字符串
        #调用SaveExcel函数，保存数据到Excel
        SaveExcel(df1,self.rButton2.isChecked())

    #定向筛选
    def click3(self):
        global root
        global myrow
        #合并Excel表格
        filearray = []
        filelocation = glob.glob(root + "\*.xls")
        for filename in filelocation:
            filearray.append(filename)
        res = pd.read_excel(filearray[0])
        for i in range(1, len(filearray)):
            A = pd.read_excel(filearray[i])
            res = pd.concat([res, A], ignore_index=False, sort=True)
        # 显示指定列数据
        df1 = res[['买家会员名', '收货人姓名', '联系手机','宝贝标题']]
        df2 = df1.loc[df1['宝贝标题'] == '零基础学Python']
        self.textEdit.setText(str(df2)) #
        #调用SaveExcel函数，保存定向筛选结果到Excel
        SaveExcel(df2,self.rButton2.isChecked())

    #多表合并
    def click4(self):
        global root
        # 合并指定文件夹下的所有Excel表
        filearray = []
        filelocation = glob.glob(root+"\*.xls")
        for filename in filelocation:
            filearray.append(filename)
        res = pd.read_excel(filearray[0])
        for i in range(1, len(filearray)):
            A = pd.read_excel(filearray[i])
            res = pd.concat([res, A], ignore_index=False, sort=True)

        self.textEdit.setText(str(res.index))
        # 调用SaveExcel函数，将合并后的数据保存到Excel
        SaveExcel(res, self.rButton2.isChecked())

    #多表统计排行
    def click5(self):
        global root
        # 合并Excel表格
        filearray = []
        filelocation = glob.glob(root + "\*.xls")
        for filename in filelocation:
            filearray.append(filename)
        res = pd.read_excel(filearray[0])
        for i in range(1, len(filearray)):
            A = pd.read_excel(filearray[i])
            res = pd.concat([res, A], ignore_index=False, sort=True)
        # 分组统计排序
        # 通过reset_index()函数将groupby()的分组结果转成DataFrame对象
        df = res.groupby(["宝贝标题"])["宝贝总数量"].sum().reset_index()
        df1 = df.sort_values(by='宝贝总数量', ascending=False)
        self.textEdit.setText(str(df1))
        # 调用SaveExcel函数，将统计排行结果保存到Excel
        SaveExcel(df1, self.rButton2.isChecked())

    def click6(self):
        global root
        # 合并Excel表格
        filearray = []
        filelocation = glob.glob(root + "\*.xls")
        for filename in filelocation:
            filearray.append(filename)
        res = pd.read_excel(filearray[0])
        for i in range(1, len(filearray)):
            A = pd.read_excel(filearray[i])
            res = pd.concat([res, A], ignore_index=False, sort=True)
        # 分组统计排序
        # 通过reset_index()函数将groupby()的分组结果转成DataFrame对象
        df=res[(res.类别=='全彩系列')]
        df1 = df.groupby(["图书编号"])["买家实际支付金额"].sum().reset_index()
        df1 = df1.set_index('图书编号')  # 设置索引
        df1 = df1[u'买家实际支付金额'].copy()
        df2=df1.sort_values(ascending=False)  # 排序
        SaveExcel(df2, self.rButton2.isChecked())
        # 图表字体为华文细黑，字号为12
        plt.rc('font', family='SimHei', size=10) # ?
        #plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        # plt.figure("贡献度分析")  # ?
        df2.plot(kind='bar')
        plt.ylabel(u'销售收入（元）')
        p = 1.0 * df2.cumsum() / df2.sum()
        print(p)
        p.plot(color='r',
               secondary_y=True,
               style='-o',
               linewidth=0.5)
        #plt.title("图书贡献度分析")
        plt.annotate(format(p[9], '.4%'),
                     xy=(9, p[9]),
                     xytext=(9 * 0.9, p[9] * 0.9),
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.1"))  # 添加标记，并指定箭头样式。
        plt.ylabel(u'收入（比例）')  # 第二Y轴
        plt.show()

    #单击“浏览”按钮选择文件存储路径
    def viewButton_click(self):
        global temproot
        temproot = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        self.text1.setText(temproot)




# 定义载入主窗体的方法
def show_MainWindow():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
        show_MainWindow()
        path=root
        # visitDir(path)
