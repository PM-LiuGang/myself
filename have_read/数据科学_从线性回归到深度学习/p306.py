# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb 12 22:16:19 2019
描述：展示spectral embedding的效果
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import matplotlib.pyplot as plt

from spectral_embedding_ import spectral_embedding


def generateData():
    '''
    生成邻接矩阵
    '''
    data = np.array([
        [0, 1, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 0]])
    return data


def visualize(data):
    '''

    '''
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.scatter(data[:, 0],
               data[:, 1],
               s=200,
               edgecolors='k')
    plt.show()


def run():
    '''

    '''
    data = generateData()
    #
    re = spectral_embedding(data,
                            n_components=2,
                            drop_first=False)
    visualize(re)


if __name__ == '__main__':
    run()
