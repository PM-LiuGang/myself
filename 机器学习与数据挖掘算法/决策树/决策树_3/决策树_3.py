# -*- coding: utf-8 -*-
"""
创建时间 Mon Sep 10 14:10:39 2018
描述:
作者:PM.liugang
"""

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    marker = list('sxo^v')
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=cmap(idx),
                    marker=marker[idx],
                    label=cl)
    if test_idx:
        x_test = X[test_idx, :]
        plt.scatter(x_test[:, 0], x_test[:, 1], c='yellow', alpha=1.0,
                    linewidths=1, marker='v', s=55, label='test set')
    plt.xlabel('Petal length [standardized]')
    plt.ylabel('Petal width [standardized]')
    plt.legend(loc='upper left')
    # plt.show()

'''构建决策树'''

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=0)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

tree = DecisionTreeClassifier(criterion='entropy',
                              max_depth=3,
                              random_state=0)
tree.fit(X_train, y_train)
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X_combined,
                      y_combined,
                      classifier=tree,
                      test_idx=range(105, 150   ))
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.legend(loc='upper left')
plt.show()

from sklearn.tree import export_graphviz
export_graphviz(tree,
                out_file='tree.dot',
                feature_names=['petal length','petal width'])

'''
通过随机森林将弱分类器集成为强分类器
'''

from sklearn.ensemble import RandomForestClassifier
# n_estimators 使用的决策树的数量
# n_jobs 设定训练过程中需要的同时处理器内核的数量
# criterion 熵
# random state 初始随机种子
forest = RandomForestClassifier(criterion='entropy',
                                n_estimators=10,
                                random_state=1,
                                n_jobs=2)

forest.fit(X_train,y_train)
plot_decision_regions(X_combined,
                      y_combined,
                      classifier=forest,
                      test_idx=range(105,150))
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc='upper left')
plt.show()
