# -*- coding: utf-8 -*-
"""
创建时间：Fri Feb  8 21:26:05 2019
描述：
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import scipy.stats.stats as scss

from statsmodels.stats.outliers_influence import variance_inflation_factor
from pandas.tools.plotting import scatter_matrix
import warnings

warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def generateData(n):
    '''

    '''
    data = []
    np.random.seed(2046)
    for i in range(0, 3):
        for j in range(0, 3):
            data.append({'x1': i, 'x2': j})
    data = pd.DataFrame(data * n)  # note
    data['x3'] = data['x1'] + np.random.random(9 * n)
    error = 0.1 * np.random.random(9 * n)
    data['y'] = 0.7 * data['x1'] - 1.1 * data['x2'] + \
        0.3 * data['x3'] + error
    return data


def visualize(data):
    '''

    '''
    axes = scatter_matrix(data,
                          alpha=1,
                          diagonal='kde',
                          range_padding=.9,
                          figsize=(8, 8))
    corr = data.corr(method='pearson').as_matrix()
    for i, j in zip(*plt.np.triu_indices_from(axes, k=1)):
        axes[i, j].annotate("%s: %.3f" % ("相关系数", corr[i, j]),
                            (0.5, 0.9),
                            xycoords='axes fraction',
                            ha='center',
                            va='center')
    plt.show()


def trainModel(X, Y):
    '''

    '''
    model = sm.OLS(Y, X)
    re = model.fit()
    return re


def uncorrelatedVariable(data):
    '''

    '''
    print('x1和x2的相关系数为： %s' %
          scss.pearsonr(data['x1'], data['x2'])[0])
    Y = data['y']
    X = sm.add_constant(data['x1'])
    re = trainModel(X, Y)
    print(re.summary())
    X1 = sm.add_constant(data['x2'])
    re1 = trainModel(X1, Y)
    print(re1.summary())
    X2 = sm.add_constant(data[['x1', 'x2']])
    re2 = trainModel(X2, Y)
    print(re2.summary())


def correlatedVariable(data):
    '''
    用强相关的x1和x3搭建模型
    '''
    print("x1和x3的相关系数为：%s" %
          scss.pearsonr(data["x1"], data["x3"])[0])
    Y = data['y']
    X = sm.add_constant(data['x1'])
    re = trainModel(X, Y)
    print(re.summary())
    X1 = sm.add_constant(data['x3'])
    re1 = trainModel(X1, Y)
    print(re1.summary())
    X2 = sm.add_constant(data[['x1', 'x3']])
    re2 = trainModel(X2, Y)
    print(re2.summary())
    # 检测多重共线性
    print('检测假设x1和x3同时不显著')
    print(re2.f_test(['x1=0', 'x3=0']))
    vif = pd.DataFrame()
    vif['VIF Factor'] = [variance_inflation_factor(X2.values, i)
                         for i in range(X2.shape[1])]
    vif['features'] = X2.columns
    print(vif)


def increaseDataSet():
    '''

    '''
    index = []
    x1Std = []
    x1 = []
#    vif = []
    for i in range(1, 150):
        data = generateData(i)
        Y = data['y']
        X = data[['x1', 'x3']]
        X = sm.add_constant(X)
        re = trainModel(X, Y)
        k = re.cov_params()
        index.append(i)
        x1Std.append(np.sqrt(k.loc['x1', 'x1']))
        x1.append(re.params['x1'])
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.plot(index, x1, 'r-', label='%s' % 'a1的估计值')
    ax.plot(index, x1Std, 'b', label='%s' % 'a1标准差的估计值')
    plt.legend(loc=4, shadow=True)
    plt.show()


def centeringData(data):
    '''

    '''
    Y = data['y']
    X = np.round(data[['x3']], 1)
    X2 = np.round(X ** 2, 1)
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(211)
    ax.scatter(X, X2)
    ax.set_xlabel('$x3$')
    ax.set_ylabel('$x3^2$')
#    ax.set_xticks(np.linspace(-0.1,3.1,5))

    ax1 = fig.add_subplot(212)
    centerX = np.round(X - X.mean(), 1)
    centerX2 = np.round(centerX ** 2, 1)
    ax1.scatter(centerX, centerX2)
    ax1.set_xlabel(r'$x3 - \overline{x3}$')
    ax1.set_ylabel(r'$(x3 - \overline{x3})^2$')
#    ax.set_xticks(np.linspace(-1.5,1.6,5))
    plt.show()

    X = pd.concat([X, X2], axis=1, ignore_index=True)
    X.columns = ['x3', 'x3_squared']
    X = sm.add_constant(X)
    re = trainModel(X, Y)
    print(re.summary())
    X = pd.concat([centerX, centerX2], axis=1, ignore_index=True)
    X.columns = ['x3_center', 'x3_center_sqaured']
    X = sm.add_constant(X)
    re1 = trainModel(X, Y)
    print(re1.summary())


if __name__ == '__main__':
    data = generateData(2)
    visualize(data)
    uncorrelatedVariable(data)
    correlatedVariable(data)
    increaseDataSet()
    centeringData(data)
