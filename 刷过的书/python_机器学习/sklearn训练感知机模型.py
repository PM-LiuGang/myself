# -*- coding: utf-8 -*-
"""
创建时间 Fri Jan  4 09:54:01 2019
作者:PM.liugang
描述:
StandardScaler对训练集中每一维度特征计算出样本平均值和标准差，然后调用transform方法
对数据集进行标准化，注意我们用相同的标准化参数对待训练集和测试集
逻辑斯谛回归对类别概率建模：如果数据不能完全线性分割，算法永远不会收敛，我们实际上很少
真正使用感知器模型
遗留：
"""

import numpy as np 
import matplotlib.pyplot as plt
import sys

from plotClassifierRegions import plot_decision_regions
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap

sys.path.append('C:\\Users\\Administrator\\Desktop\\myself')

# 准备数据
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
print('=======标签共有几类========')
print(np.unique(y))
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,
                                                  random_state=0)
# 数据标准化
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
# 感知器模型
ppn = Perceptron(max_iter=40,eta0=0.1,random_state=0)
ppn.fit(X_train_std,y_train)
y_pred = ppn.predict(X_test_std)

print('预测的样本数量为: %d' % (y_test.shape[0]))
print('感知器误分类样本数量为： %d' % (y_test != y_pred).sum())
print('准确率: %.2f' % accuracy_score(y_test, y_pred))
print('===============')

X_combined_std = np.vstack((X_train_std,X_test_std))
y_combined = np.hstack((y_train,y_test))
plot_decision_regions(X=X_combined_std,
                      y=y_combined,classifier=ppn,
                      test_idx = range(105,150))
plt.xlabel('花瓣长度（标准化后）')
plt.ylabel('花瓣宽度（标准化后）')
plt.legend(loc='upper left')
plt.show()