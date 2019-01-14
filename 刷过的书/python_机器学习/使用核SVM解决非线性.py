# -*- coding: utf-8 -*-
"""
创建时间 Mon Jan 14 15:32:15 2019
作者:PM.liugang
描述:使用核SVM解决非线性
遗留：
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

from sklearn.svm import SVC
from plotClassifierRegions import plot_decision_regions
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

sys.path.append('C:\\Users\\Administrator\\Desktop\\myself')

np.random.seed(0)
x_xor = np.random.randn(200, 2)
y_xor = np.logical_xor(x_xor[:, 0] > 0, x_xor[:, 1] > 0) # bool
y_xor = np.where(y_xor, 1, -1)

plt.scatter(x_xor[y_xor == 1, 0],
            x_xor[y_xor == 1, 1],
            c='b',
            marker='x',
            label='1')

plt.scatter(x_xor[y_xor == -1, 0],
            x_xor[y_xor == -1, 1],
            c='r',
            marker='s',
            label='-1')
plt.ylim(-3.0)
plt.legend()
plt.show()

svm = SVC(kernel='rbf',
          random_state=0,
          gamma=1.0,  # 高斯球面的阶段参数，增大，会产生更加柔软的决策界
          C=10.0)
svm.fit(x_xor,y_xor)
plot_decision_regions(x_xor,y_xor,classifier=svm)
plt.legend(loc='upper left')
plt.show()

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

svm = SVC(kernel='rbf',
          random_state=0,
          gamma=0.2,  # gamma值比较小，所有决策边界比较soft
          C=1.0)
svm.fit(X_train_std,y_train)
plot_decision_regions(X_combined_std,
                      y_combined,
                      classifier=svm,
                      test_idx=range(105,150))
plt.xlabel('Petal length [Standardized]')
plt.ylabel('Petal Width [Standardized')
plt.legend(loc='upper left')
plt.show()

svm = SVC(kernel='rbf',
          random_state=0,
          gamma=100,  # 增大gamma值
          C=1.0)
svm.fit(X_train_std,y_train)
plot_decision_regions(X_combined_std,
                      y_combined,
                      classifier=svm,
                      test_idx=range(105,150))
plt.xlabel('Petal length [Standardized]')
plt.ylabel('Petal Width [Standardized')
plt.legend(loc='upper left')
plt.show()