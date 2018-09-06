# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:14:11 2018
@author: 刘刚
来源 《python运营》
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, auc, confusion_matrix,\
 f1_score, precision_score, recall_score, roc_curve  # 导入分类的指标库
import prettytable
import pydotplus  # 打印表格，将dot文件转换本地文件保存
import matplotlib.pyplot as plt

file = 'classification.csv'
raw_data = np.loadtxt(file, delimiter=',', skiprows=1)
x = raw_data[:, :-1]
y = raw_data[:, -1]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0)  # test size=0.3 train=0.7 test=0.3
model_tree = tree.DecisionTreeClassifier(random_state=0)
model_tree.fit(x_train, y_train)
pre_y = model_tree.predict(x_test)

n_samples, n_features = x.shape  # (21927, 4)
print('samples: %d \t features: %d ' % (n_samples, n_features))
print(70 * '-' + '\n')
confusion_m = confusion_matrix(y_test, pre_y)  # confusion_m ?
confusion_matrix_table = prettytable.PrettyTable()
confusion_matrix_table.add_row(confusion_m[0, :])
confusion_matrix_table.add_row(confusion_m[1, :])
print('TITLE:CONFUSION MATRIX')
print(confusion_matrix_table)
print(70 * '-' + '\n')

y_score = model_tree.predict_proba(x_test)  # y_score.shape (6579,2)
fpr, tpr, thresholds = roc_curve(y_test, y_score[:, 1])
auc_s = auc(fpr, tpr)
accuracy_s = accuracy_score(y_test, pre_y)  # 准确率 TP+TN/TP+FN+FP+TN 0-1 越大越好
# 精确度，分类模型的预测结果中将正例预测为正例的比例 TP/TP+FP 0-1
precision_s = precision_score(y_test, pre_y)
# 召回率 分类模型的预测结果被正确预测为正例占总的正例的比例 TP/TP+FN
recall_s = recall_score(y_test, pre_y)
f1_s = f1_score(y_test, pre_y)  # F1得分，准确率和召回率的调和均值，2*(P*R)/P+R 0-1

core_metrics = prettytable.PrettyTable()
core_metrics.field_names = ['auc', 'accuracy_s', 'precision', 'recall', 'f1']
core_metrics.add_row([auc_s, accuracy_s, precision_s, recall_s, f1_s])
print('TITLE METRICS')
print(core_metrics)
print(70 * '-' + '\n')

names_list = ['age', 'gender', 'income', 'rfm_score']
color_list = list('rcbg')
feature_importance = model_tree.feature_importances_  # 特征1+2+3+4 = 100%
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(fpr, tpr, label='ROC')
plt.plot([0, 1], [0, 1], linestyle='--', color='k',
         label='RANDOM CHANCE')  # (0,0),(1,1)两个点之间画条直线
plt.title('ROC')
plt.xlabel('fales positive rate')
plt.ylabel('true positive rate')
plt.legend(loc=0)

plt.subplot(1, 2, 2)
plt.bar(np.arange(feature_importance.shape[0]), feature_importance,
        tick_label=names_list, color=color_list)  # feature_importance ?
plt.title('Feature importance')
plt.xlabel('feature')
plt.ylabel('importance')
plt.suptitle('classification result')
plt.tight_layout()
plt.show()

dot_data = tree.export_graphviz(
    model_tree, out_file=None, max_depth=5, feature_names=names_list, filled=True, rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('tree.pdf')

'''
阅读pdf
当income 小于等于55654时，总样本量为15348，其中负例样本和正例样本分别为13700,1648；
当income 小于等于55654时，且rfm score 小于等于7.8375时，总样本量有14581，其中负例样本和正例样本分别为13700和881，依次类推
'''
'''
Confusion Matrix
+---------+---------+
| Field 1 | Field 2 |
+---------+---------+
|   5617  |   282   |
|   321   |   359   |
+---------+---------+
Core Metrics
+--------------------+-------------------+--------------------+--------------------+--------------------+
|        auc         |     accuracay     |     precision      |       recall       |         f1         |
+--------------------+-------------------+--------------------+--------------------+--------------------+
| 0.7500443744203904 | 0.908344733242134 | 0.5600624024960998 | 0.5279411764705882 | 0.5435276305828918 |
+--------------------+-------------------+--------------------+--------------------+--------------------+
classification prediction
classification for 1 record is: 0
classification for 2 record is: 0
classification for 3 record is: 1
'''
'''
fpr,tpr,thresholds
Out[21]:
(array([0.        , 0.04780471, 0.06153585, 0.06187489, 1.        ]),
array([0.        , 0.52794118, 0.55441176, 0.55588235, 1.        ]),
array([2.        , 1.        , 0.5       , 0.33333333, 0.        ]))
'''
