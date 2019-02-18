# -*- coding: UTF-8 -*-
"""
此脚本用于展示过拟合问题
review 190217
遗留：
为什么过拟合的数据用的是traindata？,非过拟合用的是data？

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures  # 多项式特征

plt.rcParams['font.sans-serif'] = ['SimHei']  # 输出中文
plt.rcParams['axes.unicode_minus'] = False  # 正负轴显示


def evaluate_model(model, testdata, features, labels, featurizer):
    '''
    param model 模型
    param testdata 数据集
    param features 特征
    param labels 标签
    param featurizer 模型
    return error,score 均方差，R系数
    '''
    fStd = featurizer.fit_transform(testdata[features])  # 先训练，在标准化
    testdataLabel = testdata[labels]
    error = np.mean(((model.predict(fStd)) - testdataLabel) ** 2)  # 均 差 方
#    score = np.mean(model.score(fStd,testdataLabel))
    score = model.score(fStd, testdataLabel)
    return error, score


def train_model(traindata, features, labels, featurizer):
    '''
    定义评估模型，拟合数据
    param featurizer 转换器
    return 返回训练好的线性模型
    '''
    # fit_intercept 是否存在截距，默认存在 True
    model = linear_model.LinearRegression(fit_intercept=False)
#    f1 = featurizer.fit_transform(traindata[features])
#    t1 = featurizer.transform(traindata[labels]) error->shape
#    model.fit(f1,t1)
    model.fit(featurizer.fit_transform(traindata[features]), traindata[labels])
    return model


def visualize_model(model, featurizer, data, features, labels, evaluation,
                    degree, title=None):
    '''
    param model Linearmodel
    param featurizer-PolynomialFeatures list-len=4
    param data DataFrame
    param feature=['x']
    param labels=['y']
    param evaluation list
    param degree 多项式阶数
    return picture
    '''

    fig = plt.figure(figsize=(8, 8), dpi=80)
    for i in range(4):
        ax = fig.add_subplot(2, 2, i + 1)
#        ax.set_title(title)
        fig.suptitle(title) # 有遗留 参数不会写
        visualize_tion(
            ax,
            data,
            model[i],
            featurizer[i],
            evaluation[i],
            features,
            labels,
            degree[i])
    plt.show()


def visualize_tion(ax, data, model, featurizer, evaluation, features, labels, 
                   degree):
    '''

    '''
    ax.scatter(data[features], data[labels], color='b')  # 画原数据点
    ax.plot(data[features], 
            model.predict(featurizer.fit_transform(data[features])),
            color='r')
    ax.text(0.01, 0.99,
            '%s%.3f\n%s%.3f\n%s%s' %
            ('均方差:', evaluation[0],
             '决定系数:', evaluation[1],
             '多项式阶数:', degree),
            style='italic', # 斜体
            verticalalignment='top', # 对齐方式，相对于框线
            horizontalalignment='left', # 对齐方式
            transform=ax.transAxes,  # (0.01,0.99)在图片中的位置是相对位置，左下角是0,0
            color='m',
            fontsize=13)


def over_fitting(data):
    '''
    # featurizer.shape = (n_sample,degree+1)
    '''
    features = ['x']
    labels = ['y']
    traindata = data[:15]
    testdata = data[15:]
    featurizer = []
    over_fitting_model = []  # 不同degree的多项式 对应的线性模型
    over_fitting_evaluation = []
    model = []
    evaluation = []
    degree = []

    for i in range(1, 11, 3):  # 1 4 7 10
        featurizer.append(PolynomialFeatures(degree=i))
        over_fitting_model.append(train_model(traindata, features, labels,
                                              featurizer[-1]))
        model.append(train_model(data, features, labels, featurizer[-1]))

        over_fitting_evaluation.append(evaluate_model(
            over_fitting_model[-1], testdata, features, labels, featurizer[-1]))
        evaluation.append(evaluate_model(model[-1], testdata, features, labels,
                                         featurizer[-1]))
        degree.append(i)

    visualize_model(
        model,
        featurizer,
        data,
        features,
        labels,
        evaluation,
        degree,
        title = '正常数据')
    visualize_model(over_fitting_model, 
                    featurizer, 
                    data, 
                    features, 
                    labels,
                    over_fitting_evaluation, 
                    degree,
                    title = '过拟合数据')


def readdata(path):
    data = pd.read_csv(path)
    return data


if __name__ == "__main__":
    data = readdata('simple_example.csv')
    print(data.describe())
#    featurizer = PolynomialFeatures(degree=5)
    over_fitting(data)
