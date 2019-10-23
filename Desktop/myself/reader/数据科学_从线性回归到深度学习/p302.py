# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb 12 21:15:02 2019
描述：
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.mixture import GaussianMixture
from sklearn.datasets.samples_generator import make_blobs


def generateData(n):
    '''
    随机生成内部方差不相同的数据
    '''
    centers = [[-2, 0], [0, 2], [2, 4]]
    std = [.1, 1, .2]
    data, _ = make_blobs(n_samples=n,  # 样本总数目 _ feature.shape
                         centers=centers,
                         cluster_std=std)  # 标准差
    return data


def trainModel(data, clusterNum, covType):
    '''
    使用混合高斯训练模型
    '''
    model = GaussianMixture(n_components=clusterNum,
                            covariance_type=covType)  # 不同类别的协方差矩阵是不同的
    model.fit(data)
    return model


def visualizeResult(ax, data, labels, centers):
    '''
    将聚类结果可视化
    '''
    colors = ["#82CCFC", "k", "#0C5FFA", "#BAE7FC", "#3CAFFA"]
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


def visualizeBIC(ax, re, covTypes, colors):
    '''
    将聚类结果的BIC指标可视化
    re:DataFrame
    '''
    for i, j in enumerate(covTypes):
        re[j].plot(kind='bar',
                   color=colors[i],
                   ax=ax,
                   position=i - 1,
                   width=.2,
                   label=j)
    plt.legend(loc='best', shadow=True)
    ax.set_xlim([-1, 5])


def run():
    '''

    '''
    np.random.seed(12031)
    data = generateData(1200)
    covTypes = ["spherical", "tied", "diag", "full"]
    colors = ["#BAE7FC", "#82CCFC", "#0C5FFA", "k"]
    re = []
    bestBIC = np.infty
    for num in range(1, 6):
        item = {'num': num}
        for cov in covTypes:
            model = trainModel(data, num, cov)
            _bic = model.bic(data)
            item[cov] = _bic
            if _bic < bestBIC:
                bestGMM = model
                bestBIC = _bic
            else:
                pass
        re.append(item)
    re = pd.DataFrame(re)
    re = re.set_index(['num'])
    
    fig = plt.figure(figsize=(8, 4), dpi=80)
    ax = fig.add_subplot(121)
    visualizeResult(ax,
                    data,
                    bestGMM.predict(data),
                    bestGMM.means_)
    ax = fig.add_subplot(122)
    visualizeBIC(ax, 
                 re, 
                 covTypes, 
                 colors)
    plt.show()

if __name__ == '__main__':
    run()