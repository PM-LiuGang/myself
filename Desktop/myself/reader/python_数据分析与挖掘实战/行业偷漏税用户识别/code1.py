# -*- coding: utf-8 -*-
"""
创建时间 Thu Sep 20 10:30:31 2018
描述:
作者:PM.liugang
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']

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

ifile = 'data.xls'
data = pd.read_excel(ifile,index_col=0)
t = pd.DataFrame(data.groupby([data['销售模式'],
                               data['输出']]).size()).unstack()[0]
t['异常比率'] = t['异常']/t.sum(axis=1)
t.sort_values('异常比率',ascending=False)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.bar(range(len(t.index)),t['异常比率'],tick_label=t.index)
plt.xticks(rotation=90)
plt.show()

data['输出'] = data['输出'].replace('正常',1) # KeyError
data['输出'] = data['输出'].replace('异常',0)

for m,n in enumerate(set(data['销售类型'])):
    data['销售类型'] = data['销售类型'].replace(n,m+1)

for m,n in enumerate(set(data['销售模式'])):
    data['销售模式'] = data['销售模式'].replace(n,m+1)

from random import shuffle
data = data.values
shuffle(data)
p=0.8
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

from keras.models import Sequential
from keras.layers.core import Dense,Activation

net = Sequential()
net.add(Dense(input_dim=14,units=10)) # 14->12 
#net.add(Dense(input_dim=14,units=10),'relu')
net.add(Activation('relu'))
net.add(Dense(input_dim=10,units=1))
#net.add(Dense(input_dim=10,units=1),'sigmod')
net.add(Activation('sigmoid'))
net.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
hist = net.fit(train[:,:14],train[:,14],epochs=10,batch_size=1)
net.save_weights('ch06model.h5')

predict_result = net.predict_classes(train[:,:14]).reshape(len(train))
predict_result_test = net.predict_classes(test[:,:14]).reshape(len(test))

cmPlot(train[:,14],predict_result).show()
cmPlot(test[:,14],predict_result_test).show()

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(train[:,:14],train[:,14])

cmPlot(train[:,14],tree.predict(train[:,:14])).show()
cmPlot(test[:,14],tree.predict(test[:,:14])).show()

from sklearn.metrics import roc_curve

predict_result_test = net.predict(test[:,:14]).reshape(len(test))
fpr1,tpr1,thresholds1 = roc_curve(test[:,14],
                                  predict_result_test,
                                  pos_label=1)
plt.plot(fpr1,tpr1,linewidth=2,label='ROC OF LM')
# CART模型
predict_result_test = tree.predict_proba(test[:, :14])[:, 1]
fpr, tpr, thresholds = roc_curve(test[:, 14], predict_result_test, pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC OF CART')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.ylim(0, 1.05)
plt.xlim(0, 1.05)
plt.legend(loc=4)
plt.show()