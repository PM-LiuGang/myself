# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb 12 19:39:23 2019
描述：展示如何选择KMeans里面的类别个数K
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs


def generateData(n):
    '''
    生成随机的无标签聚类数据
    '''
    centers = [[1, 1], [-1, 1], [1, -1]]
    X, _ = make_blobs(n_samples=n,  # 样本总数目 _ feature.shape
                      centers=centers,
                      cluster_std=.5)  # 标准差
    return X


def trainModel(data, clusterNum):
    '''
    使用KMeans对数据进行聚类
    '''
    model = KMeans(n_clusters=clusterNum)
    model.fit(data)
    return model


def computeSSE(model, data):
    '''
    计算聚类结果的误差平方和
    '''
    wdist = model.transform(data).min(axis=1)  # transform ? min ?
    sse = np.sum(wdist ** 2)
    return sse


def visualizeSSE(sse, clusterNum):
    '''
    不同聚类个数的误差平方和
    '''
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.plot(clusterNum,  # shape = 4 ? 3 ?
            sse,  # shape
            'k--',
            marker='o',
            markerfacecolor='r',
            markeredgecolor='k')
    ax.set_xlim([min(clusterNum) - 1, max(clusterNum) + 1])


def _visualize(ax, data, labels, centers):
    '''
    将聚类结果可视化
    '''
    colors = ["#BAE7FC", "#3CAFFA", "#82CCFC", "#0C5FFA", "k"]
    ax.scatter(data[:, 0],
               data[:, 1],
               c=[colors[i] for i in labels],
               marker='o',
               alpha=.8)
    ax.scatter(centers[:, 0],
               centers[:, 1],
               marker='*',
               c=colors,
               edgecolors='white',
               s=600,
               linewidths=2)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


def run(data):
    '''
    主程序
    '''
    fig = plt.figure(figsize=(8, 8), dpi=80)
    sse = []
    for i in range(2, 6):
        ax = fig.add_subplot(2, 2, i - 1)
        model = trainModel(data, i)  # 聚类中心数目从2逐渐递增
        sse.append(computeSSE(model, data))
        _visualize(ax,
                   data,
                   model.labels_,
                   model.cluster_centers_)
    visualizeSSE(sse, range(2, 6))  # range(2,6)
    plt.show()


if __name__ == '__main__':
    np.random.seed(13003)
    data = generateData(1000)
    run(data)
