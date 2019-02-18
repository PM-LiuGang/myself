# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb  5 21:37:22 2019
描述：展示不平衡的数据对模型的影响
作者: PM.LiuGang
Review:
遗留：
"""
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
import warnings

from sklearn import metrics
from sklearn.linear_model import LogisticRegression

plt.rcParams["font.sans-serif"] = ["SimHei"]
warnings.filterwarnings('ignore')


def generateData(n):
    '''
    产生均衡的逻辑回归数据
    '''
    np.random.seed(4060)
    cov = [[1, 0], [0, 1]]
    X = np.random.multivariate_normal([0, 0], cov, n)  # 生成正态分布矩阵
    beta = np.array([1, -1]).reshape(2, 1)
    error = np.random.logistic(size=n).reshape(-1, 1)  # 逻辑分布
    Y = (np.dot(X, beta) + error > 0) + 0
    return X, Y


def unbalanceData(X, Y, zeroTimes):
    '''
    通过将类别0的数据重复zeroTimes次，将均衡数据集变为非均衡数据集
    '''
    X0 = np.repeat(X[np.where(Y == 0)[0]], zeroTimes, axis=0)
    Y0 = np.repeat(Y[np.where(Y == 0)[0]], zeroTimes, axis=0)
    X1 = X[np.where(Y > 0)[0]]
    Y1 = Y[np.where(Y > 0)[0]]
    _X = np.append(X0, X1, axis=0)
    _Y = np.append(Y0, Y1, axis=0)
    return _X, _Y


def logitModel(X, Y):
    '''
    搭建逻辑回归模型，并得到预测结果
    '''
    model = LogisticRegression(C=1e4)  # 为了消除惩罚项的干扰，将惩罚系数设为很大
    model.fit(X, Y.ravel())
    pred = model.predict(X)
    return pred


def visualize(ratios, predPositive, truePositive, aucs,
              accuracies):
    '''
    将模型可视化
    '''
    fig = plt.figure(figsize=(8, 3), dpi=80)
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(ratios,
            predPositive,
            label='%s' % '预测结果里类别1的个数')
    ax.plot(ratios,
            truePositive,
            'k--',
            label='%s' % '预测结果里类别1的个数',
            )
    ax.set_xlim([0, 0.5])
    ax.invert_xaxis()  # 将x或y轴逆序显示
    plt.legend(shadow=True, loc='best')

    ax1 = fig.add_subplot(1, 2, 2)
    ax1.plot(ratios,
             aucs,
             'r',
             label='%s' % '曲线下面积（AUC）')
    ax1.plot(ratios,
             accuracies,
             'k-',
             label='%s' % '准确度（ACC）')
    ax1.set_xlim([0, 0.5])
    ax1.set_ylim([0.5, 1])
    ax1.invert_xaxis()
    plt.legend(shadow=True, loc='best')


def evaluateModel(Y, pred):
    '''
    评估模型效果，其中包括ACC、AUC以及预测结果中类别1的个数
    '''
    predPositive = []
    truePositive = []
    aucs = []
    accuracies = []
    ratios = []
    for i in range(len(Y)):
        ratios.append(len(Y[i][Y[i] > 0]) / float(len(Y[i])))
        predPositive.append(len(pred[i][pred[i] > 0]))
        truePositive.append(len(Y[i][Y[i] > 0]))
        fpr, tpr, _ = metrics.roc_curve(Y[i], pred[i])
        accuracies.append(metrics.accuracy_score(Y[i],
                                                 pred[i]))
        aucs.append(metrics.auc(fpr, tpr))
    visualize(ratios, predPositive, truePositive, aucs, accuracies)


def balanceData(X, Y):
    '''
    通过调整各个类别的比重，解决非均衡数据集的问题
    '''
    positiveWeight = len(Y[Y > 0]) / float(len(Y))
    classWeight = {1: 1. / positiveWeight, 0: 1. / (1 - positiveWeight)}
    model = LogisticRegression(class_weight=classWeight, C=1e4)
    model.fit(X, Y.ravel())
    pred = model.predict(X)
    return pred


def imbalanceDataEffect():
    '''
    展示非均衡数据集对搭建模型的影响
    '''
    X, Y = generateData(2000)
    trueY = []
    predY = []
    balancePredY = []
    for zeroTimes in np.arange(1, 100):
        _X, _Y = unbalanceData(X, Y, zeroTimes)
        trueY.append(_Y) # Y error 
        predY.append(logitModel(_X, _Y))
        balancePredY.append(balanceData(_X, _Y))
    evaluateModel(trueY, predY)
    evaluateModel(trueY, balancePredY)


if __name__ == '__main__':
    imbalanceDataEffect()
