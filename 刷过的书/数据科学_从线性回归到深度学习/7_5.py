# -*- coding: utf-8 -*-
"""
创建时间：Fri Feb  8 19:43:38 2019
描述：
作者: PM.LiuGang
Review:
遗留：80行报错
"""

#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import scipy.stats as scs

from sklearn.model_selection import train_test_split
from sklearn import metrics

plt.rcParams["font.sans-serif"] = ["SimHei"]


def transLabel(data):
    '''
    将文字变量转换为数字变量
    '''
    data['label_code'] = pd.Categorical(data.label).codes
    return data


def readData(path):
    data = pd.read_csv(path, encoding='utf-8')
    cols = ['age',
            'education_num',
            'capital_gain',
            'capital_loss',
            'hours_per_week',
            'label']
    return data[cols]


def transFeature(data, category):
    '''
    根据传入的分段区间，将每星期工作时间转换为定量变量
    '''
    labels = ['(0)-(1)'.format(category[i], category[i + 1])
              for i in range(len(category) - 1)]
    data['hours_per_week_group'] = pd.cut(
        data['hours_per_week'],
        category,
        include_lowes=True,
        labels=labels)
    

def getCatergory(data):
    '''
    基于卡方检验，得到每星期工作时间的‘最优’分段
    '''
    interval = [data['hours_per_week'].min(),data['hours_per_week'].max()]
    _category = doDivide(data, interval)
    a = set()
    for i in _category:
        a = a.union(set(i))
    category = list(a)
    category.sort()
    return category



def doDivide(data, interval):
    '''
    使用贪心算法，得到‘最优’的分段
    interval:list
    '''
    category = []
    pValue, chi2, index = divideData(data, interval[0], interval[1])
    if chi2 < 15:  # ?
        category.append(interval)
    else:
        category += doDivide(data, [interval[0], index]) # error
        category += doDivide(data, [index, interval[1]])
        


def divideData(data, minValue, maxValue):
    '''
    遍历所有可能的分段，返回卡房统计量最高的分段
    '''
    maxChi2 = 0
    index = -1
    maxpValue = 0
    for i in range(minValue + 1, maxValue):
        category = pd.cut(data['hours_per_week'],
                          [minValue, i, maxValue],
                          include_lowest=True)
        cross = pd.crosstab(data['label'], category)
        chi2, pValue, _, _ = scs.chi2_contingency(cross)  # 计算卡方统计量
        if chi2 > maxChi2:
            maxpValue = pValue
            maxChi2 = chi2
            index = i
    return maxpValue, maxChi2, index


def trainModel(data):
    formula = """label_code ~ education_num + capital_gain + \
        capital_loss + C(hours_per_week_group)"""
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def baseModel(data):
    '''
    原有模型
    '''
    formula = "label_code ~ education_num + capital_gain \
        + capital_loss + hours_per_week"
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def makePrediction(re, testSet, alpha=0.5):
    '''
    使用训练好的模型对测试数据做预测
    '''
    pd.options.mode.chained_assignment = None
    data = testSet.copy()
    data['prob'] = re.predict(data)
    data['pred'] = data.apply(lambda x: 1 if x['prob'] > alpha else 0,
                              axis=1)
    return data


def evaluation(newRe, baseRe):
    '''
    展示将每星期工作时间离散化之后，模型效果的变化
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
    ax.plot(fpr, tpr, 'k',
            label='%s;%s = %0.2f' % ('加入性别后的ROC曲线', '曲线下面积（AUC）', auc))

    fpr, tpr, _ = metrics.roc_curve(baseRe['label_code'],
                                    baseRe['prob'])
    auc = metrics.auc(fpr, tpr)
    ax.plot(fpr, tpr, 'b-',
            label='%s;%s = %0.2f' % ('加入性别前的ROC曲线', '曲线下面积（AUC）', auc))
    plt.legend(shadow=True)
    plt.show()





def logitRegression(data):
    '''
    逻辑回归模型分析步骤展示
    '''
    data = transLabel(data)
    trainSet, testSet = train_test_split(data,
                                         test_size=0.2,
                                         random_state=2310)
    category = getCatergory(trainSet)
    trainSet = transFeature(trainSet, category)
    testSet = transFeature(testSet, category)
    newRe = trainModel(trainSet)
    print(newRe.summary())
    newRe = makePrediction(newRe, testSet)
    baseRe = baseModel(trainSet)
    baseRe = makePrediction(baseRe, testSet)
    evaluation(newRe, baseRe)


if __name__ == '__main__':
    pd.set_option('display.width', 1000)
    dataPath = 'adult.data'
    data = readData(dataPath)
    logitRegression(data)
