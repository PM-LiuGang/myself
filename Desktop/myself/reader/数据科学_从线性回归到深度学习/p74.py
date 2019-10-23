# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb 19 19:39:55 2019
描述：使用sklearn搭建线性回归模型
作者: PM.LiuGang
Review:20190219
遗留：
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import linear_model

plt.rcParams['font.sans-serif'] = ['SimHei']


def evaluateModel(model, testData, features, labels):
    '''
    计算线性模型的均方差和决定系数
    
    Parameters
    ----------
    model : fitted-LinearRegression-model
    testData : DataFrame
    features : list[str]
    labels : list[str]
    
    Returns
    -------
    error : float64
    score : np.float64
    '''
    error = np.mean(
        (model.predict(testData[features]) - testData[labels]) ** 2)
    score = model.score(testData[features], testData[labels])
    return error, score

def visualizeModel(model, data, features, labels, error, score):
    '''
    Parameters
    ----------
    model : fitted-linearRegressionModel
    data : DataFrame
    featues : list[str]
    labels : list[str]
    error : float64
    score : np.float64
    
    Returns
    ------
    plt : 
    '''
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.set_title('%s' % '线性回归示例')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$y$')
    ax.scatter(data[features], data[labels], color='b',
               label='%s : $y = x + \epsilon$' % '真实值')

    if model.intercept_ > 0:
        ax.plot(data[features], model.predict(data[features]), color='r',
                label='%s : $y = %.3fx$ + %.3f'
                % ('', model.coef_, model.intercept_))
    else:
        ax.plot(data[features], model.predict(data[features]), color='r',
                label='%s : $y = %.3fx$ - %.3f' # 注意是减号
                % ('', model.coef_, abs(model.intercept_)))

    legend = plt.legend(shadow=True)
    legend.get_frame().set_facecolor('#6F93AE')
    ax.text(0.99, 0.01, # 右下角
            '%s%.3f\n%s%.3f'
            % ('均方差', error, '决定系数', score),
            style='italic',
            va='bottom', # 底部对齐
            ha='right', # 右对齐
            transform=ax.transAxes,
            color='m',
            fontsize=13)
    plt.show()


def trainModel(trainData, features, labels):
    '''

    '''
    model = linear_model.LinearRegression()
    model.fit(trainData[features], trainData[labels])
    return model


def linearModel(data):
    '''

    '''
    features = ['x']
    labels = ['y']
    trainData = data[:15]
    testData = data[15:]
    model = trainModel(trainData, features, labels)
    error, score = evaluateModel(model, testData, features, labels)
    visualizeModel(model, data, features, labels, error, score)


def readData(path):
    '''

    '''
    data = pd.read_csv(path)
    return data


if __name__ == '__main__':
    dataPath = 'simple_example.csv'
    data = readData(dataPath)
    linearModel(data)
