# -*- coding: utf-8 -*-
"""
创建时间：Sun Feb 10 23:13:39 2019
描述：展示svm和logit regression的差异
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.svm import SVC
#from sklearn.metrics.pairwise import linear_kernel, laplacian_kernel
#from sklearn.metrics.pairwise import polynomial_kernel, rbf_kernel
from sklearn.linear_model import LogisticRegression

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False


def generateData(n, centers):
    '''
    生成非训练模型数据
    '''
    np.random.seed(2044)
    X = np.r_[np.random.randn(n, 2) + centers[0],
              np.random.randn(n, 2) + centers[1]]
    X = np.round(X,2)
    Y = [[0]] * n + [[1]] * n
    data = np.concatenate((Y, X), axis=1)
    data = pd.DataFrame(data, columns=['y', 'x1', 'x2'])
    return data


def drawData(ax, data):
    '''
    将数据可视化
    '''
    label1 = data[data['y'] > 0]
    ax.scatter(label1[['x1']], label1[['x2']],
               marker='o')
    label0 = data[data['y'] == 0]
    ax.scatter(label0[['x1']], label0[['x2']],
               marker='^',
               color='k')
    return ax


def visualize(A, B, reA, reB):
    '''
    将模型可视化
    '''
    fig = plt.figure(figsize=(8, 4), dpi=80)
    ax = fig.add_subplot(121)
    drawData(ax, A)
    drawHyperplane(ax, reA[0].coef_, reA[0].intercept_, 'k')
    drawHyperplane(ax, reA[1].coef_, reA[1].intercept_, "r-.")
    ax.set_xlim([-12, 12])
    ax.set_ylim([-7, 7])
    plt.legend(shadow=True, loc='best')

    ax1 = fig.add_subplot(122)
    drawData(ax1, B)
    drawHyperplane(ax, reB[0].coef_, reB[0].intercept_, 'k')
    drawHyperplane(ax, reB[1].coef_, reB[1].intercept_, "r-.")
    ax.set_xlim([-12, 12])
    ax.set_ylim([-7, 7])
    plt.legend(shadow=True, loc='best')
    plt.show()


def drawHyperplane(ax, coef, intercept, style):
    '''
    将数据点描绘出来
    '''
    a = -coef[0][0] / coef[0][1]
    xx = np.linspace(-8, 12)
    yy = a * xx - (intercept) / coef[0][1]
    ax.plot(xx, yy, style,
            label='%s: %.2f' % ('直线斜率', a))
    return ax


def svmAndLogit(data):
    '''
    分别训练SVM和logit regression模型
    '''
    svmModel = SVC(C=1, kernel='linear')
    svmModel.fit(data[['x1', 'x2']], data['y'])
    logitModel = LogisticRegression()
    logitModel.fit(data[['x1', 'x2']], data['y'])
    return svmModel, logitModel


def softAndHardMargin(data):
    '''
    分别训练soft margin和hard margin svm模型
    '''
    hardMargin = SVC(C=1, kernel='linear')
    hardMargin.fit(data[['x1', 'x2']], data['y'])
    softMargin = SVC(C=1e-4, kernel='linear')
    softMargin.fit(data[['x1', 'x2']], data['y'])
    return hardMargin, softMargin


if __name__ == "__main__":
    A = generateData(5, [[-1, -1], [3, 3]])
    B = A.append(generateData(200, [[-7, -2], [8.5, 3]]))
    svmA, logitA = svmAndLogit(A)
    svmB, logitB = svmAndLogit(B)
    visualize(A, B, (svmA, logitA), (svmB, logitB))
    softA, hardA = softAndHardMargin(A)
    softB, hardB = softAndHardMargin(B)
    visualize(A, B, (softA, hardA), (softB, hardB))
