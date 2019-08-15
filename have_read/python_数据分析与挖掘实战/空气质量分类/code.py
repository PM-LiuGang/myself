# -*- coding: utf-8 -*-
"""
创建时间 Fri Sep 21 14:10:32 2018
描述:根据空气中SO2，NO，NO2，NOx，PM10，PM2.5的含量对空气质量进行分类评价
作者:PM.liugang
遗留问题：有个标签没有分类
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import prettytable
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import auc, roc_curve


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
tree = DecisionTreeClassifier(criterion='entropy',random_state=0)
'''准备数据集'''
datadf = pd.read_excel('data.xls')
datadf.drop(248,axis=0,inplace=True)
datadf['空气等级'].replace('II','2',inplace=True)
datadf['空气等级'].replace('III','3',inplace=True)
datadf['空气等级'].replace('I','1',inplace=True)
datadf['空气等级'].replace('IV','4',inplace=True)
datadf['空气等级'].replace('V','5',inplace=True)
datadf['空气等级'].replace('VI','6',inplace=True)
data = datadf.values
p = 0.8
x_train = data[:int(p*len(data)), :]
y_test = data[int(p*len(data)):, :]

'''决策树模型'''
tree = DecisionTreeClassifier(criterion='entropy',random_state=0)
tree.fit(x_train[:, :-1], x_train[:, -1])
treePredict = tree.predict(y_test[:, :-1])
y_score = tree.predict_proba(y_test[:,:-1])
# y_shape=(6579,2) y_score.[:,5] ?
# ↓ error 不支持多类格式

'''模型评估'''
fpr, tpr, thresholds = roc_curve(y_test[:,-1], y_score[:, 1])
auc_s = auc(fpr, tpr)  # AUC曲线

#精准率、准确率、召回率，F1调和均值
accuracy_s = accuracy_score(y_test[:,-1], treePredict)
precision_s = precision_score(y_test[:,-1], treePredict)
recall_s = recall_score(y_test[:,-1], treePredict)
f1_s = f1_score(y_test[:,-1], treePredict)
# 可视化指标
core_metrics = prettytable.PrettyTable()
core_metrics.field_names = ['auc',
                            'accuracy_s',
                            'precision',
                            'recall',
                            'f1']
core_metrics.add_row([auc_s,
                      accuracy_s,
                      precision_s,
                      recall_s,
                      f1_s])
print('TITLE METRICS')
print(core_metrics)
print()

'''可视化ROC曲线'''
feature_importance = tree.feature_importances_
color_list = list('rcbg')
# ROC曲线
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(fpr, tpr, label='ROC')
plt.plot([0, 1],
         [0, 1],
         linestyle='--',
         color='k',
         label='RANDOM CHANCE')  # 完全随机曲线
plt.title('ROC')
plt.xlabel('Fales Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc=0)
# 特征直方图
plt.subplot(1, 2, 2)
plt.bar(np.arange(feature_importance.shape[0]),
        feature_importance,
        color=color_list)  # feature_importance ?
plt.title('Feature importance')
plt.xlabel('feature')
plt.ylabel('importance')
plt.suptitle('classification result')
plt.tight_layout()

plt.show()
# roc_curve(y_test[:,-1],treePredict)
# 如何求准确率 多类的
# cmPlot(y_test[:, -1], treePredict)
'''
confusion_m = confusion_matrix(y_test[:,-1], treePredict)  # confusion_m ?
confusion_matrix_table = prettytable.PrettyTable()
confusion_matrix_table.add_row(confusion_m[0, :])
confusion_matrix_table.add_row(confusion_m[1, :])
print(confusion_matrix_table)
'''
