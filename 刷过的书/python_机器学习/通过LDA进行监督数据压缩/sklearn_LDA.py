# -*- coding: utf-8 -*-
"""
创建时间 Sat Dec 29 11:58:26 2018
描述:来源python机器 P125
作者:PM.liugang
遗留：标准化后，出现了问题，数据与书中样本数据不一致
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# from sklearn.lda import LDA 原文->error
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap


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

# 准备数据
dfWine = pd.read_csv('wine_data.csv')  # 原文是heared=None->error
x, y = dfWine.iloc[:, 1:].values, dfWine.iloc[:, 0].values
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=0)
# 数据标准化处理
sc = StandardScaler()
xTrainStd = sc.fit_transform(x_train)
xTestStd = sc.fit_transform(x_test)

'''调用sklearn中的LDA'''
lda = LDA(n_components=2)
xTrainLda = lda.fit_transform(xTrainStd, y_train) # error Negative values
'''逻辑斯谛回归建模'''
lr = LogisticRegression()
lr = lr.fit(xTrainLda, y_train)
plot_decision_regions(xTrainLda, y_train, classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.legend(loc='upper left')
plt.show()
