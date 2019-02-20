# -*- coding: utf-8 -*-
"""
创建时间：Sat Feb 16 10:28:39 2019
描述：展示如何利用PCA做数据降维
作者: PM.LiuGang
Review:
遗留：
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def generateData(n):
    '''
    随机生成训练数据
    '''
    np.random.seed(1001)
    x = np.linspace(-4, 4, n)
    error = np.random.randn(n)
    y = 1 * x + error
    data = np.c_[x, y]
    return data


def visualize(data, model):
    '''
    将模型结果可视化
    '''
    fig = plt.figure(figsize=(12, 6), dpi=80)
    #
    ax = fig.add_subplot(121)
    ax.scatter(data[:, 0], data[:, 1], alpha=0.8)
    ax.set_xlim([-6, 6])
    ax.set_ylim([-6, 6])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # 模拟结果
    ax = fig.add_subplot(122)
    ax.scatter(data[:, 0], data[:, 1], alpha=0.8)
    m = model.mean_  # ? array([ 0., -0.04144356])
    for v, l in zip(model.components_, model.explained_variance_):
        # model.components.shape = (2,2)
        # model.explained_variance_.shape = (2,2)
        start, end = m, m + 1.5 * np.sqrt(l) * v
        ax.annotate('', # 文本内容
                    xy=end, # 箭头坐标
                    xytext=start, # 文本坐标
                    arrowprops=dict(facecolor='k', width=2.0)) # 箭头要求
    ax.set_xlim([-6, 6])
    ax.set_ylim([-6, 6])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()


def trainModel(data):
    '''

    '''
    model = PCA(n_components=2)
    model.fit(data)
    return model


if __name__ == '__main__':
    data = generateData(200)
    model = trainModel(data)
    visualize(data, model)
