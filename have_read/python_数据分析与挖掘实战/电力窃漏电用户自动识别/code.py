# -*- coding: utf-8 -*-
"""
创建时间 Tue Sep 18 14:03:02 2018
描述:见note
作者:PM.liugang
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
#from sklearn.cross_validation import train_test_split
from random import shuffle
from scipy.interpolate import lagrange
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.metrics import confusion_matrix, roc_curve
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.externals import joblib


netfile = 'net.model'
inputFile = 'missing_data.xls'
outpufFile = 'missing_data_processed.xls'

data = pd.read_excel(inputFile, header=None)


def ployInterpColumn(s, n, k=5):
    '''
    param s 
    param n 被插值的元素位置等价于索引
    param k 缺失值的参考取值范围
    return
    '''
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


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


def cmRoc(testData, res):
    predictResult = res.predict(testData[:, :3]).reshape(len(testData))
    if res == net:
        fpr, tpr, thresholds = roc_curve(testData[:, 3],
                                         predictResult,
                                         pos_label=1)
        plt.plot(fpr,tpr,linewidth=2,label='神经网路模型')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.xlim(0, 1.05)
        plt.ylim(0, 1.05)
        plt.legend(loc=4)
        plt.show()        
    elif res == tree:
        fpr, tpr, thresholds = roc_curve(testData[:, 3],
                                         res.predict_proba(
                                             testData[:, :3])[:, 1],
                                         pos_label=1)
        plt.plot(fpr,tpr,linewidth=2,label='CART决策树模型')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.xlim(0, 1.05)
        plt.ylim(0, 1.05)
        plt.legend(loc=4)
        plt.show()


for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployInterpColumn(data[i], j)

# data.to_excel(outpufFile,header=None,index=False)

dataFile = 'model.xls'
data = pd.read_excel(dataFile)
data = data.values
shuffle(data)

p = 0.8
train = data[:int(len(data)*p), :]
test = data[int(len(data)*p):, :]

# X_train,X_test,y_train,y_test = train_test_split(data)
'''建立一个简单的神经网络模型'''
net = Sequential()  # 神经网络实例化
# net.add(Dense(3, 10)) in book error
net.add(Dense(input_dim=3, units=10))  # 添加输入层 3节点 隐藏层 10
net.add(Activation('relu'))  # 隐藏层使用relu激活函数
net.add(Dense(input_dim=10, units=1))  # 隐藏层 10 输出层 1
net.add(Activation('sigmoid'))  # 输出层使用sigmoid激活函数
net.compile(loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])  # class_mode = 'binary' in book error
net.fit(train[:, :3],
        train[:, 3],
        epochs=1000,
        batch_size=1,
        verbose=2)  # default verbose=1
net.save_weights(netfile)

predict_result = net.predict_classes(train[:, :3]).\
    reshape(len(train))
cmPlot(train[:, 3], predict_result).show()

'''建议CART决策树模型'''
treefile = 'tree.pkl'
tree = dtc()  # 树模型的常用参数？
tree.fit(train[:, :3], train[:, 3])
joblib.dump(tree, treefile)

cmPlot(train[:, 3], tree.predict(train[:, :3])).show()
cmRoc(test, net)
cmRoc(test, tree)
# 213/232 9/159=6% 神经网络更优
# 213/232 11/163=7%
