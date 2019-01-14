# -*- coding: utf-8 -*-
"""
创建时间 Mon Jan 14 12:06:05 2019
作者:PM.liugang
描述:
支持向量机，松弛变量C，通过调整C控制间隔的宽度，在偏差和方差之间寻找某周平衡
C越大，间隔越小；C越小，间隔越大；增大C的值会增加偏差而减小模型的方差
遗留：
"""
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('C:\\Users\\Administrator\\Desktop\\myself')

from plotClassifierRegions import plot_decision_regions
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

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

svn = SVC(kernel='linear',C=1.0,random_state=0)
svn.fit(X_train_std,y_train)
plot_decision_regions(X_combined_std,
                      y_combined,
                      classifier=svn,
                      test_idx=range(105,150))
plt.xlabel('Petal Length [S]')
plt.ylabel('Petal Width [S]')
plt.legend(loc='upper left')
plt.show()

from sklearn.linear_model import SGDClassifier # 针对数据集很大，不能一次读入内存
ppn = SGDClassifier(loss='perceptron')
lr = SGDClassifier(loss='log')
svm = SGDClassifier(loss='hinge')
