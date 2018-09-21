# -*- coding: utf-8 -*-
"""
创建时间 Fri Sep 21 11:19:46 2018
描述:
作者:PM.liugang
"""

import pandas as pd

from sklearn import metrics
from sklearn import svm
from random import shuffle
#from sklearn.cross_validation import train_test_split
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

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

'''数据抽样代码'''
ifile = 'moment.csv'
data = pd.read_csv(ifile, encoding='gbk')
data = data.values
'''扰乱数据'''
shuffle(data)
data_train = data[:int(0.8*len(data)), :]
data_test = data[int(0.8*len(data)):, :]
'''支持向量机模型代码'''
x_train = data_train[:, 2:] * 30 # .shape (162,9)
y_train = data_train[:, 0].astype(int) # .shape(1,162)
x_test = data_test[:, 2:] * 30 # .shape(41,9)
y_test = data_test[:, 0].astype(int) # .shape(1,41)
#x_train,y_train,x_test,y_test = train_test_split(data)
model = svm.SVC()
model.fit(x_train, y_train) 

cm_train = metrics.confusion_matrix(y_train,
                                    model.predict(x_train)) # 4,4
cm_test = metrics.confusion_matrix(y_test,
                                   model.predict(x_test)) # 3,3
'''
pd.DataFrame(cm_train,
             index=range(1, 6),
             columns=range(1, 6)).to_excel('ofile_train.csv')
pd.DataFrame(cm_test,
             index=range(1, 6),
             columns=range(1, 6)).to_excel('ofile_test.csv')
'''

cmPlot(y_train,model.predict(x_train))
cmPlot(y_test,model.predict(x_test))
