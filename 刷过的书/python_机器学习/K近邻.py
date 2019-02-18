# -*- coding: utf-8 -*-
"""
创建时间 Wed Jan 23 10:57:12 2019
作者:PM.liugang
描述:
1.确定k大小和距离度量
2.对于测试集中的一个样本，找到训练集中和它最近的k个样本
3.将这k个样本的投票结果作为测试样本的类别
通常欧氏距离用于实数域的数据集，此时一定要对特征进行标准化，每一维度特征的重要性等同
遗留：
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('C:\\Users\\Administrator\\Desktop\\myself')

from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from plotClassifierRegions import plot_decision_regions


## 准备数据
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
print('=======标签共有几类========')
print(np.unique(y))
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,
                                                  random_state=0)
print('=' * 30)
## 数据标准化
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std,X_test_std))
y_combined = np.hstack((y_train,y_test))

knn = KNeighborsClassifier(n_neighbors=5, # 最近的5个样本
                           p=2, # p=2退化为欧氏距离 p=1 退化为曼哈顿距离
                           metric='minkowski') # 距离度量方式
knn.fit(X_train_std,y_train)
plot_decision_regions(X_combined_std,
                      y_combined,
                      classifier=knn,
                      test_idx=range(105,150))
plt.xlabel('Petal Length [Standardized]')
plt.ylabel('Petal Width [Standardized]')
plt.show()
