# -*- coding: utf-8 -*-
"""
创建时间 Tue Sep 11 10:26:39 2018
描述:
作者:PM.liugang
"""

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
# from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier


def plot_decision_regions(X,
                          y,
                          classifier,
                          test_idx=None,
                          resolution=0.02):
    '''
    param X 数据集，无标签
    param y 标签
    param classifier 使用的分类器
    param test_idx 选取的数据索引数
    param resolution 画等高线时，用于np meshgrid 
    return 等高线的分类图
    '''
    
    '''
    画等高线
    '''
    marker = list('sxo^v')
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1 
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    # np arange(支持负数和非整数)
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    # 根绝值确定 分割 数目，画出等高线
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap) # 还是没明白z xx1 xx2的关系
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    '''
    按照标签画数据集两个特征的散点图，每种标签对应一种颜色
    '''
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=marker[idx],
                    label=cl)
    '''
    画原数据集指定范围的散点
    '''
    if test_idx:
        x_test = X[test_idx, :]
        plt.scatter(x_test[:, 0],
                    x_test[:, 1],
                    c='yellow',
                    alpha=1.0,
                    linewidths=1,
                    marker='v',
                    s=55,
                    label='test set')
    plt.xlabel('Petal length [standardized]')
    plt.ylabel('Petal width [standardized]')
    plt.legend(loc='upper left')
    # plt.show()


'''构建数据集和KNN模型'''

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]  # X.shape = 150,4
y = iris.target  # y.shape = 150,
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=0)
sc = StandardScaler()  # [0,1]
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
knn = KNeighborsClassifier(n_neighbors=2,
                           p=2,
                           metric='minkowski')  # 欧几里得距离 p=2
# knn说明中 不是说不需要训练的步骤么？
# 用标准化的数据进行训练
knn.fit(X_train_std, y_train)
# X != np.vstack((X_train, X_test))
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))
X_combined_std = sc.transform(X)
# 也是用标准化的数据进行分类
plot_decision_regions(X_combined_std,
                      y,
                      classifier=knn,
                      test_idx=range(105, 150)) # classifier 实例化模型名称
plt.xlabel('Petal length [Standardized]')
plt.xlabel('Petal width [Standardized]')
plt.show()
