# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:14:11 2018
@author: 刘刚
来源 《python运营》
Review 180922
"""
import numpy as np
import prettytable
import pydotplus
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import auc, roc_curve

'''读取数据 分割数据'''
# data.head()?
# data.index
# data.columns
file = 'classification.csv'
raw_data = np.loadtxt(file,
                      delimiter=',',
                      skiprows=1)
x = raw_data[:, :-1]
y = raw_data[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=0)

'''构建决策树'''
model_tree = tree.DecisionTreeClassifier(random_state=0)
model_tree.fit(x_train, y_train)
pre_y = model_tree.predict(x_test)

n_samples, n_features = x.shape  # (21927, 4)
print('samples: %d \t features: %d ' % (n_samples, n_features))

'''混淆矩阵可视化结果'''
confusion_m = confusion_matrix(y_test, pre_y)  # shape(2,2)
confusion_matrix_table = prettytable.PrettyTable()
confusion_matrix_table.add_row(confusion_m[0, :])
confusion_matrix_table.add_row(confusion_m[1, :])
print('TITLE:CONFUSION MATRIX')
print(confusion_matrix_table)

'''模型指标评估'''
y_score = model_tree.predict_proba(x_test)
# y_shape=(6579,2) y_score.[:,5] ?
fpr, tpr, thresholds = roc_curve(y_test, y_score[:, 1])
auc_s = auc(fpr, tpr)  # AUC曲线

#精准率、准确率、召回率，F1调和均值
accuracy_s = accuracy_score(y_test, pre_y)
precision_s = precision_score(y_test, pre_y)
recall_s = recall_score(y_test, pre_y)
f1_s = f1_score(y_test, pre_y)
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
names_list = ['age', 'gender', 'income', 'RFM_score']
color_list = list('rcbg')
feature_importance = model_tree.feature_importances_
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
        tick_label=names_list,
        color=color_list)  # feature_importance ?
plt.title('Feature importance')
plt.xlabel('feature')
plt.ylabel('importance')
plt.suptitle('classification result')
plt.tight_layout()

plt.show()

'''可视化决策树'''
dot_data = tree.export_graphviz(model_tree,
                                out_file=None,
                                max_depth=5,
                                feature_names=names_list,
                                filled=True, rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('tree.pdf')

'''
[out]
阅读pdf
当income 小于等于55654时，总样本量为15348，其中负例样本和正例样本分别为13700,1648；
当income 小于等于55654时，且rfm score 小于等于7.8375时，总样本量有14581，其中负例样本和正例样本分别为13700和881，依次类推

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

fpr,tpr,thresholds
Out[21]:
(array([0.        , 0.04780471, 0.06153585, 0.06187489, 1.        ]),
array([0.        , 0.52794118, 0.55441176, 0.55588235, 1.        ]),
array([2.        , 1.        , 0.5       , 0.33333333, 0.        ]))
'''
