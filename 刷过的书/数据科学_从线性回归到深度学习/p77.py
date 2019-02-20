# -*- coding: utf-8 -*-
"""
创建时间：Mon Feb 18 20:20:54 2019
描述：使用statsmodels搭建线性回归模型
作者: PM.LiuGang
Review:
遗留：
坐标的分布和点的分布对应不上
"""

import os
import sys
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

from statsmodels.sandbox.regression.predstd import wls_prediction_std

plt.rcParams['font.sans-serif']=['SimHei']


def modelSummary(re):
    '''
    分析线性回归模型的统计性质
    param re model
    '''
    print(re.summary())
    print('检验假设x的系数等于0：')
    print(re.f_test('x=0'))
    print('检验假设const的系数等于0：')
    print(re.f_test('const=0'))
    print('检验假设x的系数等于1和const的系数等于0 同时成立')
    print(re.f_test(['x=1','const=0']))
    
    
def visualizeModel(re, data, features, labels):
    '''
    
    '''
    prStd, preLow, preUp = wls_prediction_std(re,alpha=0.05)
    fig = plt.figure(figsize=(6,6),dpi=80)
    ax = fig.add_subplot(111)
    ax.set_title('%s' % '线性回归统计分析示例')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')

    ax.scatter(data[features], 
               data[labels],
               color='b', # 用blue画原始点
               label='%s: $y = x + \epsilon$' % '真实值')
    ax.plot(data[features],
            preUp - 10,
            'r--', # 红色上界
            label='%s' % '95%置信区间')
    ax.plot(data[features],
            re.predict(data[features]) - 10,
            color='g', # 黄色预测值
            label='%s: $y = %.3fx$' % ('预测值',re.params[features]))
    ax.plot(data[features],
            preLow - 10,
            'r--') # 红色下界
    legend = plt.legend(shadow=True)
    legend.get_frame().set_facecolor('#6F93AE')
    ax.set_yticks(np.linspace(0,30,7))     
    ax.set_yticklabels(('0','10','15','20','25','30','35'))         
    plt.show()
    
    
def trainModel(X,Y):
    '''
    
    '''
    model = sm.OLS(Y, X) # 最小二乘线性（OLS）回归模型
    re = model.fit()
    return re


def linearModel(data):
    '''
    
    '''
    features = ['x']
    labels = ['y']
    Y = data[labels]
    X = sm.add_constant(data[features]) # x带常数项
    re = trainModel(X, Y)
    modelSummary(re)
    resNew = trainModel(data[features],Y) # x不带常数项 
    print(resNew.summary())
    visualizeModel(resNew, data, features, labels)
    
    
def readData(path):
    '''
    
    '''
    data = pd.read_csv(path)
    return data


if __name__ == '__main__':
    dataPath = 'simple_example.csv'
    data = readData(dataPath)
    linearModel(data)
    
    
    