# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb  5 15:48:25 2019
描述：此脚本用户展示ROC曲线和AUC
作者: PM.LiuGang
Review:
遗留：
"""

#import os
#import sys
import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split  # ?

plt.rcParams["font.sans-serif"] = ["SimHei"]


def transLabel(data):
    '''
    将文字变量转换为数字变量
    '''
    data['label_code'] = pd.Categorical(data.label).codes
    return data


def trainModel(data, features, labels):
    '''
    搭建逻辑回归模型，并训练模型
    '''
    model = LogisticRegression()
    model.fit(data[features], data[labels])
    return model


def readData(path):
    data = pd.read_csv(path, encoding='utf-8')
    cols = ['age', 'education_num', 'capital_gain', 'capital_loss',
            'hours_per_week', 'label']
    return data[cols]


def visualizeRoc(fpr, tpr, auc):
    '''

    '''
    fig = plt.figure(figsize=(6,6), dpi=80)
    ax = fig.add_subplot(1,1,1)
    ax.set_title('%s' % 'ROC曲线')
    ax.set_xlabel('False positive rate')
    ax.set_ylabel('True positive rate')
    ax.plot([0, 1], [0, 1], 'r--')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.plot(fpr, 
            tpr, 
            'k', 
            label='%s: %s = %0.2f' % ('ROC曲线', '曲线下面积(AUC)', auc))
    ax.fill_between(fpr, tpr, color='grey', alpha=0.6)
    plt.legend(shadow=True)
    plt.show()


def logitRegression(data):
    '''

    '''
    data = transLabel(data)
    features = ['age', 'education_num', 'capital_gain', 'capital_loss',
                'hours_per_week']
    labels = 'label_code'
    trainSet, testSet = train_test_split(data,
                                         test_size=.2,
                                         random_state=2310)
    model = trainModel(trainSet, features, labels)
    preds = model.predict_proba(testSet[features])[:, 1]
    fpr, tpr, _ = metrics.roc_curve(testSet[labels], preds)
    auc = metrics.auc(fpr, tpr)
    visualizeRoc(fpr, tpr, auc)


if __name__ == '__main__':
    dataPath = 'adult.data'
    data = readData(dataPath)
    logitRegression(data)
