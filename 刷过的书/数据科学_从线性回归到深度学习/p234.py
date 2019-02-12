# -*- coding: utf-8 -*-
"""
创建时间：Mon Feb 11 18:51:10 2019
描述：展示决策树联结逻辑回归模型
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

plt.rcParams["font.sans-serif"] = ["SimHei"]


def generateData(n):
    '''
    生成训练数据
    '''
    X, y = make_classification(n_samples=n, n_features=4)
    data = pd.DataFrame(X, columns=['x' + str(i) for i in range(1, 5)])
    data['y'] = y
    return data


def trainModel(data, features, label):
    '''
    分别使用逻辑回归，决策树和决策树+逻辑回归建模
    '''
    res = {}
    trainData, testData = train_test_split(data, test_size=0.5)
    # 单独使用逻辑回归
    logitModel = LogisticRegression()
    logitModel.fit(trainData[features], trainData[label])
    logitProb = logitModel.predict_proba(testData[features])[:, 1]
    res['logit'] = roc_curve(testData[label], logitProb)
    
    # 单独使用决策树
    dtModel = DecisionTreeClassifier(max_depth=2)
    dtModel.fit(trainData[features], trainData[label])
    dtProb = dtModel.predict_proba(testData[features])[:, 1]
    res['DT'] = roc_curve(testData[label], dtProb)
    
    # 决策树和逻辑回归联结
    # 为了防止过拟合，使用不同的数据训练决策树和逻辑回归
    trainDT, trainLR = train_test_split(trainData,
                                        test_size=0.5)
    # 使用决策树对前两个变量做变换
    m = 2
    _dt = DecisionTreeClassifier(max_depth=2)
    _dt.fit(trainDT[features[:m]], trainDT[label])
    leafNode = _dt.apply(trainDT[features[:m]]).reshape(-1, 1)  # ?
    coder = OneHotEncoder()
    coder.fit(leafNode)
    newFeature = np.c_[
        coder.transform(_dt.apply(trainLR[features[:m]]).reshape(-1, 1)).toarray(),
        trainLR[features[m:]]]
    _logit = LogisticRegression()
    _logit.fit(newFeature[:, 1:], trainLR[label])
    testFeature = np.c_[
        coder.transform(_dt.apply(testData[features[:m]]).reshape(-1, 1)).toarray(),
        testData[features[m:]]]
    dfLogitProb = _logit.predict_proba(testFeature[:, 1:])[:, 1]
    res['DT + logit'] = roc_curve(testData[label], dfLogitProb)
    return res


def visualize(re):
    '''

    '''
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    styles = ['k--', 'r-.', 'b']
    model = ['logit', 'DT', 'DT + logit']  # 70行对应
    for i, s in zip(model, styles):
        fpr, tpr, _ = re[i]
        _auc = auc(fpr, tpr)
        ax.plot(fpr, tpr, s, label='%s:%s: %s=%.2f' %
                ('模型', i, '曲线下面积(AUC)', _auc))
    plt.title('3种模型效果比较')  # add
    plt.legend(loc=4, shadow=True)
    plt.show()


if __name__ == '__main__':
    np.random.seed(4040)
    data = generateData(4000)
    re = trainModel(data, ['x1', 'x2', 'x3', 'x4'], 'y')
    visualize(re)
