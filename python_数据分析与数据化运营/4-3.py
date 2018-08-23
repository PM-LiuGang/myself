# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:14:11 2018

@author: 刘刚
"""

import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import tree
#导入分类的指标库
from sklearn.metrics import accuracy_score,auc,confusion_matrix,f1_score,precision_score,\
recall_score,roc_curve
#将分类树的属性结构通过pdf打印出来
import prettytable,pydotplus
import matplotlib.pyplot as plt

file = 'classification.csv'
raw_data = np.loadtxt(file,delimiter=',',skiprows=1)
x = raw_data[:,:-1]
y = raw_data[:,-1]
#一定注意 test size 0.3,37分
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
#决策树在树的方法中
model_tree = tree.DecisionTreeClassifier(random_state=0)
model_tree.fit(x_train,y_train)
pre_y = model_tree.predict(x_test)

n_samples,n_features = x.shape
print('samples: %d \t features: %d ' % (n_samples,n_features))
print(70 * '-' + '\n')
#获得混淆矩阵的参数是测试集，预测集
confusion_m = confusion_matrix(y_test,pre_y)
#创建表格实例
confusion_matrix_table = prettytable.PrettyTable()
#添加第一行和第二行到可是图标里，这个图标没有之前的漂亮
confusion_matrix_table.add_row(confusion_m[0,:])
confusion_matrix_table.add_row(confusion_m[1,:])
print('TITLE:CONFUSION MATRIX')
print(confusion_matrix_table)
print(70 * '-' + '\n')

y_score = model_tree.predict_proba(x_test)
#fpr,tpr,thresholds含义？
fpr,tpr,thresholds = roc_curve(y_test,y_score[:,1])
#ROC曲线下的面积，0.5-1，越大越好
auc_s = auc(fpr,tpr)
#准确率 TP+TN/TP+FN+FP+TN 0-1 越大越好
accuracy_s = accuracy_score(y_test,pre_y)
#精确度，分类模型的预测结果中将正例预测为正例的比例 TP/TP+FP 0-1
precision_s = precision_score(y_test,pre_y)
#召回率 分类模型的预测结果被正确预测为正例占总的正例的比例 TP/TP+FN
recall_s = recall_score(y_test,pre_y)
#F1得分，准确率和召回率的调和均值，2*(P*R)/P+R 0-1
f1_s = f1_score(y_test,pre_y)
core_metrics = prettytable.PrettyTable()
core_metrics.field_names = ['auc','accuracy_s','precision','recall','f1']
core_metrics.add_row([auc_s,accuracy_s,precision_s,recall_s,f1_s])
print('TITLE METRICS')
print(core_metrics)
print(70 * '-' + '\n')

names_list = ['age','gender','income','rfm_score']
color_list = list('rcbg')
#特征1+2+3+4 = 100%
feature_importance = model_tree.feature_importances_
plt.figure()
plt.subplot(1,2,1)
plt.plot(fpr,tpr,label='ROC')
#45度方向一条直线
plt.plot([0,1],[0,1],linestyle='--',color='k',label='RANDOM CHANCE')
plt.title('ROC')
plt.xlabel('fales positive rate')
plt.ylabel('true positive rate')
plt.legend(loc=0)
plt.subplot(1,2,2)
#np.arange(feature_importance.shape[0]) 技巧
plt.bar(np.arange(feature_importance.shape[0]),feature_importance,tick_label=names_list,\
        color=color_list)
plt.title('Feature importance')
plt.xlabel('feature')
plt.ylabel('importance')
plt.suptitle('classification result')
#调整子图间距
plt.tight_layout()
plt.show()
#生成dot对象
dot_data = tree.export_graphviz(model_tree,out_file=None,max_depth=5,feature_names\
                                =names_list,filled=True,rounded=True)
#解析dot对象为图形
graph = pydotplus.graph_from_dot_data(dot_data)
#将图形对象写到pdf里
graph.write_pdf('tree.pdf')

'''
当income 小于等于55654时，总样本量为15348，其中负例样本和正例样本分别为13700,1648；
当income 小于等于55654时，且rfm score 小于等于7.8375时，总样本量有14581，其中负例样本和正例样本分别为13700和881，依次类推
'''