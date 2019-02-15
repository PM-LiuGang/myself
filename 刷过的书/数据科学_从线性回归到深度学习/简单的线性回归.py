# -*- coding: UTF-8 -*-
# 回归日期 2018-09-13

import numpy as np
#import sys
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

def readData(path):
	data = pd.read_csv(path)
	return data

def linearModel(data):
    '''
    主运行函数，包括训练模型，评估模型，可视化模型的泛化能力
    param data 数据集 | pd
    '''
    feature = ['x']
    label = ['y']
    traindata = data[:15]
    testdata = data[15:]
    model = trainModel(traindata, feature, label)
    error, score = evaluateModel(model, testdata, feature, label)
    visualizeModel(model, data, feature, label, error, score)

def trainModel(traindata, feature, label):
    '''
    训练数据
    param traindata 训练数据
    param feature 数据集中的特征名称 int
    param label 数据集中的类标签名称 float
    return 返回训练好的线性模型
    '''
    model = linear_model.LinearRegression()
    model.fit(traindata[feature], traindata[label])
    return model

def evaluateModel(model, testdata, feature, label):
    '''
    param model
    param testdata
    param feature 
    param label
    logic 均方差
    return 均方差、准确率
    '''
    error = np.mean(
        (model.predict(testdata[feature]) - testdata[label])
        ** 2)
    score = model.score(  # .score是model的属性？
        testdata[feature],
        testdata[label])
    return error, score

def visualizeModel(model, data, feature, label, error, score):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.set_title('%s' % '线性回归示例')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.scatter(data[feature],
               data[label],
               color='b',
               label='%s:$y = x + \epsilon$' % '真实值')  # 不转义 \epsilon = ε
    # model.intercept_ = 0.628 系数
    # model.coef_ = 1.012 截距
    if model.intercept_ > 0:
        ax.plot(data[feature],  # 画线图
                model.predict(data[feature]), # 预测的数据都是线性的，所以是直线
                color='r',
                label='%s:$y = %.3fx$ + %.3f' %
                ('预测值', model.coef_, model.intercept_))
    else: # 如果 < 0 ,二四象限
        ax.plot(data[feature],
                model.predict(data[feature]),
                color='r',
                label='%s:$y = %.3fx$ - %.3f' % ("预测值", model.coef_, abs(model.intercept_)))
    legend = plt.legend(shadow=True)  # 图例带阴影
    legend.get_frame().set_facecolor('#6F93AE')  # 设置图例边框颜色
    # 添加文本，在图中0.99 0.01占比处添加 均方差：error 换行 决定系数：score
    # error=0.726 | score=0.828
    ax.text(0.99, 0.01,
            '%s%.3f\n%s%.3f' % ("均方差：", error, "决定系数：", score),
            style='italic',
            verticalalignment='bottom', # 垂直底部对齐
            horizontalalignment='right', # 水平右侧对齐
            transform=ax.transAxes,
            color='m',
            fontsize=13)

if __name__ == '__main__':
    path = 'simple_example.csv'
    data = readData(path)
    #!pd read_csv 读取路径不能有中文，报错，初始化文件失败
    linearModel(data)
