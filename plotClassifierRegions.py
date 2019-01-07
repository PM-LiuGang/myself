# -*- coding: utf-8 -*-
"""
创建时间 Sat Sep 22 19:55:53 2018
描述:分类可视化模块，参数中包含训练好的模型
作者:PM.liugang
"""
import numpy as np 
import matplotlib.pyplot as plt
import sys

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap

plt.rcParams['font.sans-serif'] = ['SimHei'] #输出中文
plt.rcParams['axes.unicode_minus'] = False#正负轴显示

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    '''
    常用分类可视化函数
    param X 训练集
    param y 标签
    param classifier 已fit好的分类器
    test_idx 训练集的输入变量范围
    resolution 等高线 高度
    return 等高线 
    '''
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
