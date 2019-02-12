# -*- coding: utf-8 -*-
"""
创建时间：Thu Feb  7 16:43:25 2019
描述：此脚本用于如何处理定性变量
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

from patsy import ContrastMatrix
from sklearn.model_selection import train_test_split
from sklearn import metrics
from statsmodels.graphics.mosaicplot import mosaic

plt.rcParams["font.sans-serif"] = ["SimHei"]


def transLabel(data):
    '''
    将文字变量转化为数字变量
    '''
    data['label_code'] = pd.Categorical(data.label).codes
    return data


def readData(path):
    data = pd.read_csv(path)
    cols = ["workclass",
            "sex",
            "age",
            "education_num",
            "capital_gain",
            "capital_loss",
            "hours_per_week",
            "label"]
    return data[cols]


def trainModel2(data):
    '''
    加入workclass变量，搭建逻辑回归模型，并训练模型
    '''
    # 定义workclass的类别顺序，数组里的第一个值为基准类别
    l = [" ?",
         " Never-worked",
         " Without-pay",
         " State-gov",
         " Self-emp-not-inc",
         " Private",
         " Federal-gov",
         " Local-gov",
         " Self-emp-inc"]
    # 定义各个类别对应的虚拟变量
    contrast = np.eye(9, 6, k=-3)
    # 为每个虚拟变量命名
    contrast_mat = ContrastMatrix(contrast, l[3:])  # 公式中使用
    formula = """label_code ~ C(workclass, contrast_mat, levels=l)
        + C(sex) + education_num + capital_gain
        + capital_loss + hours_per_week"""
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def trainModel3(data):
    '''

    '''
    l = [' Male', ' Female']  # 公式中使用
    contrast = [[-0.33], [0.67]]
    contrast_mat = ContrastMatrix(contrast, ['Ridit(sex)'])  # 公式中使用
    formula = """label_code ~ C(sex, contrast_mat, levels=l) \
        + education_num + capital_gain + capital_loss + hours_per_week"""
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def trainModel(data):
    '''

    '''
    formula = "label_code ~ C(sex) + education_num \
        + capital_gain + capital_loss + hours_per_week"
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def baseModel(data):
    '''

    '''
    formula = "label_code ~ education_num + capital_gain \
        + capital_loss + hours_per_week"
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def makePrediction(re, testSet, alpha=0.5):
    '''

    '''
    pd.options.mode.chained_assignment = None
    data = testSet.copy()
    data['prob'] = re.predict(data)
    data['pred'] = data.apply(
        lambda x: 1 if x['prob'] > alpha else 0, axis=1)
    return data


def evaluation(newRe, baseRe):
    '''

    '''
    fpr, tpr, _ = metrics.roc_curve(newRe['label_code'],
                                    newRe['prob'])
    auc = metrics.auc(fpr, tpr)
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.set_title('%s' % 'ROC曲线')
    ax.set_xlabel('Fales Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.plot([0, 1], [0, 1], 'r--')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.plot(fpr, tpr, 'k', label='%s;%s = %0.2f' %
            ('加入性别后的ROC曲线', '曲线下面积（AUC）', auc))

    fpr, tpr, _ = metrics.roc_curve(baseRe['label_code'],
                                    baseRe['prob'])
    auc = metrics.auc(fpr, tpr)
    ax.plot(fpr, tpr, 'b-', label='%s;%s = %0.2f' %
            ('加入性别前的ROC曲线', '曲线下面积（AUC）', auc))
    plt.legend(shadow=True)
    plt.show()


def analyseData(data):
    '''

    '''
    cross1 = pd.crosstab(data['sex'], data['label'])
    print('显示sex & label交叉报表：')
    print(cross1)

    def props(key): return {'color': '0.45'} if ' >50K' in key else \
        {'color': "#C6E2FF"}
    mosaic(cross1[[' >50K', ' <=50K']].stack(), properties=props)
    plt.show()


def logitRegression(data):
    '''

    '''
    data = transLabel(data)
    analyseData(data)
    trainSet, testSet = train_test_split(data,
                                         test_size=0.2,
                                         random_state=2310)
    newRe = trainModel3(trainSet)
#    newRe = trainModel2(trainSet)
#    newRe = trainModel1(trainSet)
    print(newRe.summary())
    newRe = makePrediction(newRe, testSet)
    baseRe = baseModel(trainSet)
    baseRe = makePrediction(baseRe, testSet)
    evaluation(newRe, baseRe)


if __name__ == '__main__':
    dataPath = 'adult.data'
    data = readData(dataPath)
    logitRegression(data)
