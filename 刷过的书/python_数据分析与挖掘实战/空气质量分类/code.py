# -*- coding: utf-8 -*-
"""
创建时间 Fri Sep 21 14:10:32 2018
描述:根据空气中SO2，NO，NO2，NOx，PM10，PM2.5的含量对空气质量进行分类评价
作者:PM.liugang
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans


def cmPlot(yTrue, yPred):
    '''
    param yTrue
    param yPred
    return
    '''
    cm = confusion_matrix(yTrue, yPred)  # 生成混淆矩阵
    plt.matshow(cm, cmap=plt.cm.Greens)  # 画混淆矩阵图，配色风格使用cm.Greens
    plt.colorbar()  # 颜色标签
    for x in range(len(cm)):  # 数据标签
        for y in range(len(cm)):
            plt.annotate(cm[x, y],
                         xy=(x, y),
                         horizontalalignment='center',
                         verticalalignment='center')
    plt.ylabel('True label')  # 坐标轴标签
    plt.xlabel('Predicted label')  # 坐标轴标签
    return plt
'''决策树模型'''
tree = DecisionTreeClassifier()

data = pd.read_excel('data.xls')
data = data.values

p=0.8
x_train = data[:int(p*len(data)),:]
y_test = data[int(p*len(data)):,:]

tree.fit(x_train[:,:-1],x_train[:,-1])

treePredict = tree.predict(y_test[:,:-1])

cmPlot(y_test[:,-1],treePredict) 

'''KMeans'''
km = KMeans(n_clusters=5,random_state=0)
# km.cluster_centers_
# km.labels_
km.fit(x_train[:,:-1])
kmPred = km.predict(y_test[:,:-1])

yPred = pd.Series(kmPred).value_counts()
yTrue = pd.Series(y_test[:,-1]).value_counts()
print(yPred,'\n',yTrue)

from sklearn.manifold import TSNE
tsne = TSNE()
tsne.fit_transform(y_test[:,:-1]) #
tsne = pd.DataFrame(tsne.embedding_)#转换数据格式

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#不同类别用不同颜色和样式绘图
d = tsne[y_test[:,-1] == 'II']
plt.plot(d[0], d[1], 'r')
d = tsne[y_test[:,-1] == 'I']
plt.plot(d[0], d[1], 'g')
d = tsne[y_test[:,-1] == 'VI']
plt.plot(d[0], d[1], 'y')
d = tsne[y_test[:,-1] == 'III']
plt.plot(d[0], d[1], 'b')
d = tsne[y_test[:,-1] == 'V']
plt.plot(d[0], d[1], 'o')


plt.show()