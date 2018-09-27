# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 22:24:18 2018
@author: 刘刚
python分类分析
"""
import numpy as np
import prettytable
import pydotplus
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, auc, confusion_matrix
from sklearn.metrics import f1_score, roc_curve
from sklearn.metrics import precision_score,recall_score

'''准备数据'''
raw_data = np.loadtxt('classification.csv', delimiter=',', skiprows=1)
x = raw_data[:, :-1]
y = raw_data[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, 
                                                    y, 
                                                    test_size=0.3, 
                                                    random_state=0)

'''建立模型'''
model_tree = tree.DecisionTreeClassifier(random_state=0)
model_tree.fit(x_train, y_train)
pre_y = model_tree.predict(x_test)
# model_tree.tree_.children_left
# model_tree.tree_.children_right
# model_tree.tree_.feature
# model_tree.tree_.threshold
# model_tree.tree_.value

'''输出模型概况'''
n_samples, n_features = x.shape
print('Sample: %d\tFeatures: %d' % (n_samples, n_features))
print('{:*^60}'.format('分割线'))

'''混淆矩阵'''
confusion_m = confusion_matrix(y_test, pre_y)
confusion_matrix_table = prettytable.PrettyTable()
confusion_matrix_table.add_row(confusion_m[0, :])
confusion_matrix_table.add_row(confusion_m[1, :])
print('{:*^60}'.format('Confusion Matrix'))
print(confusion_matrix_table)

'''核心评估指标'''
y_score = model_tree.predict_proba(x_test)

fpr, tpr, thresholds = roc_curve(y_test, y_score[:, 1])
auc_s = auc(fpr, tpr) # ROC曲线下的面积

accuracy_s = accuracy_score(y_test, pre_y) # 准确率
precision_s = precision_score(y_test, pre_y) # 精确度
recall_s = recall_score(y_test, pre_y) # 召回率
f1_s = f1_score(y_test, pre_y) # F1得分

#混淆矩阵
core_metrics = prettytable.PrettyTable()
core_metrics.field_names = ['auc', 'accuracay', 'precision', 'recall', 'f1']
core_metrics.add_row([auc_s, accuracy_s, precision_s, recall_s, f1_s])
print('{:*^60}'.format('Core Metric'))
print(core_metrics)

'''模型可视化'''
# ROC曲线
names_list = ['Age', 'Gender', 'InCome', 'RfmScore']
color_list = list('rcbg')
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(fpr, 
         tpr, 
         label='ROC')
plt.plot([0, 1], 
         [0, 1], 
         linestyle='--', 
         color='k', 
         label='Random Chance')
plt.title('ROC')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc=0)

# 指标重要性
feature_importance = model_tree.feature_importances_
plt.subplot(1, 2, 2)
plt.bar(np.arange(feature_importance.shape[0]),
        feature_importance, 
        tick_label=names_list, 
        color=color_list)
plt.title('Feature Importance')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.suptitle('Classification Result')
plt.show()

'''保存决策树规则图为PDF文件'''
# feature_names number = n_features number
dot_data = tree.export_graphviz(model_tree, 
                                out_file=None, # 控制不生成dot文件
                                max_depth=5, # 分类规则的最大深度
                                feature_names=names_list, # 决策树规则每个变量的名称
                                filled=True,  # 控制填充
                                rounded=True)  # 控制字体样式
graph = pydotplus.graph_from_dot_data(dot_data)  # 通过pydotplus将决策树规则解析为图形
graph.write_pdf("classificationTree.pdf")  # 将决策树规则保存为PDF文件

'''模型应用'''
X_new = [[40, 0, 55616, 0], 
         [17, 0, 55568, 0], 
         [55, 1, 55932, 1]]
print('classification prediction')
for i, data in enumerate(X_new):
    y_pre_new = model_tree.predict([data])
    print('classification for %d record is: %d' % (i + 1, y_pre_new))
