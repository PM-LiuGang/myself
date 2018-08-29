# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 22:24:18 2018
@author: 刘刚
分类
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score,auc,confusion_matrix,f1_score,precision_score,recall_score,roc_curve
import os
os.chdir(r'D:\python\python_数据分析与数据化运营\chapter4')
import prettytable
import pydotplus
import matplotlib.pyplot as plt

raw_data = np.loadtxt('classification.csv',delimiter=',',skiprows=1)
x = raw_data[:,:-1]
y = raw_data[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

model_tree = tree.DecisionTreeClassifier(random_state=0)
model_tree.fit(x_train,y_train)
pre_y = model_tree.predict(x_test)

n_samples,n_features = x.shape
print('sample: %d     features: %d' % (n_samples,n_features))
print(70 * '-')

confusion_m = confusion_matrix(y_test,pre_y)
confusion_matrix_table = prettytable.PrettyTable()
confusion_matrix_table.add_row(confusion_m[0,:])
confusion_matrix_table.add_row(confusion_m[1,:])
print('Confusion Matrix')
print(confusion_matrix_table)
#predict proda 预测每个一行归属哪个标签的概率是多大
y_score = model_tree.predict_proba(x_test)
fpr,tpr,thresholds = roc_curve(y_test,y_score[:,1])
auc_s = auc(fpr,tpr)
accuracy_s = accuracy_score(y_test,pre_y)
precision_s = precision_score(y_test,pre_y)
recall_s = recall_score(y_test,pre_y)
f1_s = f1_score(y_test,pre_y)
core_metrics = prettytable.PrettyTable()
core_metrics.field_names = ['auc','accuracay','precision','recall','f1']
core_metrics.add_row([auc_s,accuracy_s,precision_s,recall_s,f1_s])
print('Core Metrics')
print(core_metrics)

names_list = ['age','gender','income','rfm_score']
color_list = list('rcbg')
plt.figure()
plt.subplot(1,2,1)
plt.plot(fpr,tpr,label='ROC')
plt.plot([0,1],[0,1],linestyle='--',color='k',label='random chance')
plt.title('ROC')
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.legend(loc=0)

feature_importance = model_tree.feature_importances_
plt.subplot(1,2,2)
plt.bar(np.arange(feature_importance.shape[0]),feature_importance,tick_label=names_list,color=color_list)
plt.title('feature importance')
plt.xlabel('features')
plt.ylabel('importance')
plt.suptitle('Classification Result')
plt.show()

dot_data = tree.export_graphviz(model_tree, out_file=None, max_depth=5, feature_names=names_list, filled=True,rounded=True)  # 将决策树规则生成dot对象
graph = pydotplus.graph_from_dot_data(dot_data)  # 通过pydotplus将决策树规则解析为图形
graph.write_pdf("4-3-1-tree.pdf")  # 将决策树规则保存为PDF文件

# 模型应用
X_new = [[40, 0, 55616, 0], [17, 0, 55568, 0], [55, 1, 55932, 1]]
print ('classification prediction')
for i, data in enumerate(X_new):
    y_pre_new = model_tree.predict([data])
    print ('classification for %d record is: %d' % (i + 1, y_pre_new))

