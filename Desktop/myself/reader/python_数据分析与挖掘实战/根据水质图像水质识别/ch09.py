# -*- coding: utf-8 -*-
"""
创建时间 Fri Sep 21 11:19:46 2018
描述:
作者:PM.liugang
review:180308
遗留：为什么原始数据要放大30倍？
"""
import sys
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn import svm
#from random import shuffle
from sklearn.cross_validation import train_test_split
#from sklearn.metrics import confusion_matrix

sys.path.append(r"C:\Users\Administrator\Desktop\myself")
from cmPlot import cmPlot

'''准备数据'''
ifile = 'moment.csv'
data = pd.read_csv(ifile, encoding='gbk')
data = data.values
data_train, data_test, label_train, label_test = train_test_split(
        data[:,2:], data[:,0],
        test_size=0.2, 
        random_state=0)
'''数据处理'''
data_train = data_train * 30
data_test = data_test * 30
data_train_small = data_train / 30
data_test_small = data_test / 30
label_train = label_train.astype(int) # np.float->int
label_test = label_test.astype(int)
'''支持向量机模型建立'''
model = svm.SVC()
model.fit(data_train, label_train) 
'''混淆矩阵'''
cm_train = metrics.confusion_matrix(label_train,model.predict(data_train))
cm_test = metrics.confusion_matrix(label_test,model.predict(data_test))
cm_train_small = metrics.confusion_matrix(label_train,model.predict(data_train_small))
cm_train_small = metrics.confusion_matrix(label_test,model.predict(data_test_small))
'''可视化混淆矩阵'''
print('{:↓^40}'.format('混淆矩阵---训练数据集(放大30倍)'))
cmPlot(label_train,model.predict(data_train))
print('{:↓^40}'.format('混淆矩阵---测试数据集(放大30倍)'))
cmPlot(label_test,model.predict(data_test))
print('{:↓^40}'.format('混淆矩阵---原始数据集(不放大)'))
cmPlot(label_train,model.predict(data_train_small))
cmPlot(label_test,model.predict(data_test_small))