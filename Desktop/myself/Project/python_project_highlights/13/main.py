# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

import pandas as pd
import jieba
from pyecharts.charts import Geo, Line, Bar
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

import sys
from os import path
import urllib.request
import collections
import json
import os
import imageio
import re

# 显示热力图，主要城市评论数_平均分页面
class Mainwindows(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(200, 200, 1250, 650)
        self.browser = QWebEngineView()

    def kk(self, title, hurl):
        self.setWindowTitle(title)
        url = d +  hurl
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)

# 显示词云图片页面
class MainWindowy(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(200, 200, 650, 650)
        self.browser = QLabel() # ? browser

    def kk(self, title, hurl):
        self.setWindowTitle(title)
        url = d +  hurl

        pixmap = QPixmap(url)
        scaredPixmap = pixmap.scaled(QSize(600, 600))
        self.browser.setPixmap(scaredPixmap)
        self.browser.show()
        self.setCentralWidget(self.browser)


# 主窗体
class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 206)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 20, 251, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        # self.comboBox.setGeometry(QtCore.QRect(83, 15, 120, 21))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 80, 235, 89))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.hide()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "开心麻花影视作品分析"))
        self.label.setText(_translate("Form", "选择电影："))
        self.comboBox.setItemText(0, _translate("Form", "夏洛特烦恼"))
        self.comboBox.setItemText(1, _translate("Form", "羞羞的铁拳"))
        self.comboBox.setItemText(2, _translate("Form", "西虹市首富"))
        self.pushButton.setText(_translate("Form", "分析"))
        self.label_2.setText(_translate("Form", "主要城市评论数及平均分"))
        self.pushButton_2.setText(_translate("Form", "查看"))
        self.label_3.setText(_translate("Form", "                 热力图"))
        self.pushButton_3.setText(_translate("Form", "查看"))
        self.label_4.setText(_translate("Form", "                   词云"))
        self.pushButton_4.setText(_translate("Form", "查看"))

        # 电影选择事件
        self.comboBox.activated[str].connect(self.itemchange)
        # 分析功能
        self.pushButton.clicked.connect(self.anal)
        # 判断是否有词云图片
        if not os.path.isfile(d +  '夏洛特烦恼词云.png'):
            self.pushButton.setText('分析')
            self.hide()
        else:
            self.pushButton.setText('完成重新分析')
            self.moveName = '夏洛特烦恼'
            self.moveId = '246082'
            self.show()
            self.btnclick()


    def itemchange(self, text):
        if text =='夏洛特烦恼':
            if not os.path.isfile(d + '夏洛特烦恼词云.png'):
                self.pushButton.setText('分析')
                self.hide()
            else:
                self.pushButton.setText('完成重新分析')
                self.moveName = '夏洛特烦恼'
                self.moveId = '245082'
                self.show()
                self.btnclick()
        if text =='羞羞的铁拳':
            if not os.path.isfile(d +  '羞羞的铁拳词云.png'):
                self.pushButton.setText('分析')
                self.hide()
            else:
                self.pushButton.setText('完成重新分析')
                self.moveName = '羞羞的铁拳'
                self.moveId = '1198214'
                self.show()
                self.btnclick()
        if text =='西虹市首富':
            if not os.path.isfile(d  +  '西虹市首富词云.png'):
                self.pushButton.setText('分析')
                self.hide()
            else:
                self.pushButton.setText('完成重新分析')
                self.moveName = '西虹市首富'
                self.moveId = '1212592'
                self.show()
                self.btnclick()
    # 隐藏查看内容
    def hide(self):
        self.pushButton_4.setVisible(False)
        self.label_4.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.label_3.setVisible(False)
        self.label_2.setVisible(False)
        self.pushButton_2.setVisible(False)

    # 显示查看内容
    def show(self):
        self.pushButton_4.setVisible(True)
        self.label_4.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.label_3.setVisible(True)
        self.label_2.setVisible(True)
        self.pushButton_2.setVisible(True)

    def btnclick(self):
        self.pushButton_2.clicked.connect(self.reli2)
        self.pushButton_3.clicked.connect(self.reli3)
        self.pushButton_4.clicked.connect(self.reli4)

    def reli2(self):
        win.kk(self.moveName + '主要城市平均评论数及平均风',
               self.moveName + '主要城市评论数_平均分.html')
        win.show()

    #  全国热力图查看按钮事件
    def reli3(self):
        win.kk(self.moveName + '全国热力图',
               self.moveName + '全国热力图.html')
        win.show()

    # 词云 查看按钮事件
    def reli4(self):
        winy.kk(self.moveName + '词云',
                self.moveName + '词云.png')
        winy.show()

    # 分析事件
    def anal(self):
        #  夏洛特烦恼 246082
        if self.comboBox.currentIndex() == 0:
            self.moveName ='夏洛特烦恼'
            self.moveId ='246082'
            self.getData()
        #  羞羞的铁拳 1198214
        if self.comboBox.currentIndex() == 1:
            self.moveName = '羞羞的铁拳'
            self.moveId = '1198214'
            self.getData()
        #  西虹市首富 1212592
        if self.comboBox.currentIndex() == 2:
            self.moveName = '西虹市首富'
            self.moveId = '1212592'
            self.getData()
        self.show()
        self.pushButton.setText('完成重新分析')
        self.btnclick()

    # 分析方法
    def getData(self):
        tomato = pd.DataFrame(columns=['date', 'score', 'city', 'comment', 'nick'])
        i = 1
        while True:
            print(i)
            try:
                url = 'http://m.maoyan.com/mmdb/comments/movie/'+self.moveId+'.json?_v_=yes&offset='+ str(i)
                html = urllib.request.urlopen(url)
                content = html.read()
                total = json.loads(content)['total']
                print(total)
                if total == 0:
                    break
                else:
                    data = json.loads(content)['cmts']
                    for item in data:
                        tomato = tomato.append(
                            {'date': item['time'].split(' ')[0],
                             'city': item['cityName'],
                             'score': item['score'],
                             'comment': item['content'],
                             'nick': item['nick']},
                            ignore_index=True
                        )
                    datah = json.loads(content)['hcmts']
                    for item in datah:
                        tomato = tomato.append(
                            {'date': item['time'].split(' ')[0], # 2019-09-09
                             'city': item['cityName'],
                             'score': item['score'],
                             'comment': item['content'],
                             'nick': item['nick']},
                            ignore_index=True
                        )
                i += 1
            except:
                i += 1
                # 跳出本次循环
                continue
        # 去掉重复数据
        tomato = tomato.drop_duplicates(
            subset=['date', 'score', 'city', 'comment', 'nick'],
            keep='first'
        )
        # 生成xlsx文件
        tomato.to_excel(self.moveName+'.xlsx', sheet_name='data')
        # 读取文件内容
        tomato_com = pd.read_excel(self.moveName+'.xlsx')
        grouped = tomato_com.groupby(['city'])
        grouped_pct = grouped['score']  # tip_pct列
        city_com = grouped_pct.agg(['mean', 'count'])
        # reset_index可以还原索引，从新变为默认的整型索引
        city_com.reset_index(inplace=True)
        # 返回浮点数 0.01 返回到后两位
        city_com['mean'] = round(city_com['mean'], 2)
        geo = Geo()
        flag = True
        data = [(city_com['city'][i], city_com['count'][i]) for i in range(0, city_com.shape[0])]
        while flag:
            # attr, value = geo.cast(data)  # cast属性被删除了
            attr = [i[0] for i in data]
            value = [i[1] for i in data]
            try:
                geo.add("", # 这很多参数都是低版本的pyecharts的，适配不了1.5.1版本
                        attr,  # data_pair
                        value,)
                flag = False
            except ValueError as e:
                e = str(e)
                e = e.split("No coordinate is specified for ")[1]  # 获取不支持的城市名
                for i in range(0, len(data)):
                    if e in list(data[i]):
                        del data[i]
                        break
                    flag = True
        # 生成全国热力图html文件
        geo.render(d + self.moveName + '全国热力图.html')  # 为什么没生成文件

        city_main = city_com.sort_values('count', ascending=False)[0:30]
        attr = city_main['city']
        v1 = city_main['count']
        v2 = city_main['mean']
        line = Line("主要城市评分")
        line.add("城市",
                 attr,
                 v2,
                 is_stack=True,
                 xaxis_rotate=30,
                 yaxis_min=0,
                 mark_point=['min', 'max'],
                 xaxis_interval=0,
                 line_color='lightblue',
                 line_width=4,
                 mark_point_textcolor='black',
                 mark_point_color='lightblue',
                 is_splitline_show=False)
        bar = Bar("主要城市评论数")
        bar.add("城市",
                attr,
                v1,
                is_stack=True,
                xaxis_rotate=30,
                yaxis_min=0,
                xaxis_interval=0,
                is_splitline_show=False)
        '''
        overlap = Overlap()
        # 默认不新增 x y 轴，并且 x y 轴的索引都为 0
        overlap.add(bar)
        overlap.add(line, yaxis_index=1, is_add_yaxis=True)
        # 生成主要城市评论数_平均分.html文件
        overlap.render(d + self.moveName+'主要城市评论数_平均分.html')
        '''
        line.overlap(bar)
        line.render(d + self.moveName+'主要城市评论数_平均分.html')
        print("主要城市评论：",d + self.moveName+'主要城市评论数_平均分.html')

        # 评论内容
        tomato_str = ' '.join(tomato_com['comment'])
        words_list = []
        # 分词
        word_generator = jieba.cut_for_search(tomato_str)
        for word in word_generator:
            words_list.append(word)
        words_list = [k for k in words_list if len(k) > 1]
        back_color = imageio.imread(d + '词云背景.jpg')  # 解析该图片
        wc = WordCloud(background_color='white',  # 背景颜色
                       max_words=200,  # 最大词数
                       mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                       max_font_size=300,  # 显示字体的最大值
                       font_path="STFANGSO.ttf",  # 字体
                       random_state=42,  # 为每个词返回一个PIL颜色
                       # width=1000,  # 图片的宽
                       # height=860  # 图片的长
                       )
        tomato_count = collections.Counter(words_list)
        wc.generate_from_frequencies(tomato_count)
        # 基于彩色图像生成相应彩色
        image_colors = ImageColorGenerator(back_color)
        # 绘制词云
        plt.figure()
        plt.imshow(wc.recolor(color_func=image_colors))
        # 去掉坐标轴
        plt.axis('off')
        # 保存词云图片
        wc.to_file(path.join(d,self.moveName + '词云.png'))
        pass

# 程序主方法
if __name__ == '__main__':
    # 获取当前文件路径
    # __file__ 为当前文件, 在ide中运行此行会报错,可改为
    # d = path.dirname(__file__)
    d = os.path.dirname(os.path.realpath(sys.argv[0])) + r"\\"  # 获取当前文件所在路径
    # d = re.sub(r'\\', '/', d)  # 将路径中的分隔符\替换为/
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # 显示热力图，主要城市评论数_平均分窗体
    win = Mainwindows()
    # 显示云图窗体
    winy = MainWindowy()
    # 初始化主窗体
    ui = Ui_Form()
    # 调用创建窗体方法
    ui.setupUi(MainWindow)
    # 显示主窗体
    MainWindow.show()
    sys.exit(app.exec_())
