# -*- coding: UTF-8 -*-
"""
此脚本用于展示过拟合问题
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures  # 多项式特征


def evaluate_model(model, testdata, features, labels, featurizer):
    '''
    param model 模型
    param testdata 数据集
    param features 特征 
    param labels 标签
    param featurizer 分类器
    return error,score 误差率和准确率
    '''
    _f = featurizer.fit_transform(testdata[features])
    _t = testdata[labels]
    error = np.mean(((model.predict(_f)) - _t) ** 2)
    score = np.mean(
        model.score(featurizer.fit_transform(testdata[features]),
                    testdata[labels]))
    return error, score


def train_model(traindata, features, labels, featurizer):
    '''
    定义评估模型，拟合数据
    param featurizer 特征多项式 按照多项式格式转换数据，作为输入使用
    return 返回训练好的线性模型
    '''
    model = linear_model.LinearRegression(
        fit_intercept=False)  # fit_intercept 是否存在截距，默认存在 True
    model.fit(featurizer.fit_transform(traindata[features]),
              traindata[labels])
    return model


def visualize_model(model, featurizer, data, features, labels, evaluation):
    '''
    param featurizer
    param evaluation
    return plt.show
    '''
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig = plt.figure(figsize=(10, 10), dpi=80)
    for i in range(4):
        ax = fig.add_subplot(2, 2, i+1)
        visualize_tion(
            ax,
            data,
            model[i],
            featurizer[i],
            evaluation[i],
            features,
            labels)
    plt.show()

def visualize_tion(ax, data, model, featurizer, evaluation, features, labels):
    ax.scatter(data[features], data[labels], color='b')
    ax.plot(data[features], 
            model.predict(featurizer.fit_transform(data[features])), 
            color='r')
    #evaluation[0] = error, evaluation[1] = score
    ax.text(0.01,
            0.99,
            '%s%.3f\n%s%.3f' % ('均方差:',
                                evaluation[0],
                                '决定系数:',
                                evaluation[1]),
            style='italic',
            verticalalignment='top',
            horizontalalignment='left',
            transform=ax.transAxes,
            color='m',
            fontsize=13)


def over_fitting(data):
    features = ['x']
    labels = ['y']
    traindata = data[:15]
    testdata = data[15:]
    featurizer = []
    
    over_fitting_model = [] # 不同degree的多项式 对应的线性模型
    over_fitting_evaluation = []
    
    model = []
    evaluation = []
    
    for i in range(1, 11, 3): # 1 4 7 10
        featurizer.append(PolynomialFeatures(degree=i))
        over_fitting_model.append(train_model(traindata, 
            features, 
            labels, 
            featurizer[-1]))
        model.append(train_model(data, features, labels, featurizer[-1]))
        over_fitting_evaluation.append(evaluate_model(
            over_fitting_model[-1], 
            testdata, 
            features, 
            labels, 
            featurizer[-1]))
        evaluation.append(evaluate_model(model[-1], 
                                         data, 
                                         features, 
                                         labels, 
                                         featurizer[-1]))
    visualize_model(model, 
                    featurizer, 
                    data, 
                    features, 
                    labels, 
                    evaluation)
    visualize_model(over_fitting_model, 
                    featurizer, 
                    data,
                    features, 
                    labels, 
                    over_fitting_evaluation)


def readdata(path):
    data = pd.read_csv(path)
    return data


if __name__ == "__main__":
    data = readdata('simple_example.csv')
    featurizer = PolynomialFeatures(degree=5)
    over_fitting(data)
