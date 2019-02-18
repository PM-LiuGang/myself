# -*- coding: utf-8 -*-
"""
创建时间：Sat Feb 16 11:18:00 2019
描述：展示如何利用核函数对非线性数据进行降维
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.decomposition import PCA, KernelPCA

plt.rcParams["font.sans-serif"] = ["SimHei"]

def generateData(n):
    """
    随机生成训练数据
    """
    x = np.linspace(-5, 5, n)
    error = np.random.randn(n)
    y = 1 * x + error
    linear = np.c_[x, y]
    noLinear, _ = make_moons(n_samples=n, noise=0.05) # noLinear.shape = (n,2) _->labels
    return linear, noLinear


def trainKernelPCA(data):
    """
    使用带有核函数的主成分分析对数据进行降维
    """
    model = KernelPCA(n_components=2, kernel='rbf', gamma=25)
    model.fit(data)
    return model


def trainPCA(data):
    '''

    '''
    model = PCA(n_components=2)
    model.fit(data)
    return model


def visualize(ax, data, model):
    '''

    '''
    ax.scatter(data[:, 0], data[:, 1], alpha=0.8)
    m = model.mean_
    v = model.components_[0]
    l = data[:, 0].max() - data[:, 0].min()
    start, end = m, m + .5 * l * v / np.linalg.norm(v)
    ax.annotate('',
                xy=end,
                xytext=start,
                arrowprops=dict(facecolor='k', width=2.0))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
#    plt.show()


def visualizeKernelPCA(ax, data, labels):
    '''

    '''
    colors = ['#82CCFC', 'k']
    markers = ['^', 'o']
    for i in range(len(colors)):
        ax.scatter(data[labels == i, 0],
                   data[labels == i, 1],
                   color=colors[i],
                   s=50,
                   marker=markers[i])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


def runPCA(linear, noLinear):
    '''

    '''
    fig = plt.figure(figsize=(12, 6), dpi=80)
    ax = fig.add_subplot(121)
    model = trainPCA(linear)
    visualize(ax, linear, model)
    ax.text(0,0,'对于线性数据，损失的信息很少',size=12,color='r')

    ax1 = fig.add_subplot(122)
    model = trainPCA(noLinear)
    visualize(ax1, noLinear, model)
    ax1.text(0,0,'对于非线性数据，损失的信息很多',size=12,color='r')
    plt.show()


def runKernelPCA():
    '''

    '''
    data, labels = make_moons(n_samples=100, noise=0.05)
    fig = plt.figure(figsize=(10, 10), dpi=80)

    ax = fig.add_subplot(221)
    visualizeKernelPCA(ax, data, labels)
    ax.text(0,0,'原始数据',size=12,color='r')
    #
    ax1 = fig.add_subplot(222)
    model = trainPCA(data)
    x = model.transform(data)[:, 0]
    visualizeKernelPCA(ax1, np.c_[x, [0] * len(x)], labels)
    ax1.text(0,0,'利用linear PCA将数据降到一维',size=12,color='r')
    #
    ax2 = fig.add_subplot(223)
    model = trainKernelPCA(data)
    x = model.transform(data)[:, 0]
    visualizeKernelPCA(ax2, np.c_[x, [0] * len(x)], labels)
    ax2.text(0,0,'利用RBF kernel PCA将数据降到一维',size=12,color='r')
    #
    ax3 = fig.add_subplot(224)
    visualizeKernelPCA(ax3, model.transform(data), labels)
    ax3.text(0,0,'利用RBF kernel PCA将数据降到二维',size=12,color='r')
    plt.show()


if __name__ == '__main__':
    np.random.seed(20001)
    linear, noLinear = generateData(200)
    runPCA(linear, noLinear)
    runKernelPCA()
