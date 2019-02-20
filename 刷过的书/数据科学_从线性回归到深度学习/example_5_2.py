# -*- coding: utf-8 -*-
"""
创建时间：Mon Feb  4 21:01:32 2019
描述：
作者: PM.LiuGang
Review:
遗留：
mosaic与书中图不一致：（占比）颜色不一致、横坐标轴的刻度不一致
"""

#import os
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np

from sklearn.model_selection import train_test_split
from statsmodels.graphics.mosaicplot import mosaic


def modelSummary(re):
    '''
    分析逻辑回归模型的统计性质
    ————————————————————————
    param re:模型
    '''
    print(re.summary())
    # 用 f test检验education num的系数是否显著
    print('检验假设education num的系数等于0：')
    print(re.f_test('education_num=0'))
    # 用f test检验两个假设是否同时成立
    print('检验假设education num的系数等于0.32和hours per week的系数等于0')
    print(re.f_test('education_num=0.32,hours_per_week=0.04'))


def visualData(data):
    data[['age', 'hours_per_week', 'education_num', 'label_code']].hist(
        rwidth=0.9,
        grid=False,
        figsize=(8, 8),
        alpha=0.6,
        color='grey')


def analyseData(data):
    print('显示基本统计信息')
    print(data.describe(include='all'))
    cross1 = pd.crosstab(pd.qcut(data['education_num'],
                                 [0, .25, .5, .75]),
                                 data['label'])
    print('显示education num和label交叉报表')
    print(cross1)
    # 交叉报表图形化
    props = lambda key:{'color': '0.45'} if '>50K' in key \
        else {'color': '#C6E2FF'}
    mosaic(cross1[[' >50K', ' <=50K']].stack(), properties=props) # !
    print('# 计算hours per week，label交叉报表')
    cross2 = pd.crosstab(pd.cut(data['hours_per_week'], 5), data['label'])
    # 将交叉报表归一化，利于分析数据
    cross2_norm = cross2.div(cross2.sum(1).astype(float), axis=0)
    print('显示hour per week和label交叉报表')
    print(cross2_norm)
    # 图形化归一化后的交叉报表
    cross2_norm.plot(kind='bar', color=['#C6E2FF', '0.45'], rot=0)
    plt.show()

def trainModel(data):
    formula = 'label_code ~ age + education_num + capital_gain + \
        capital_loss + hours_per_week'
    model = sm.Logit.from_formula(formula, data=data) # formula?
    re = model.fit()
    return re


def transLabel(data):
    '''
    将文字变量转换为数字变量
    '''
    data['label_code'] = pd.Categorical(data.label).codes
    return data


def readData(path):
    data = pd.read_csv(path,encoding='utf-8')
    cols = ['age', 'education_num', 'capital_gain', 'capital_loss',
            'hours_per_week', 'label']
    return data[cols]


def interpreModel(re):
    conf = re.conf_int() # ?
    conf['OR'] = re.params # re.params?
    # 计算各个变量对事件发生比的影响
    # conf里面的3列，分别对应着估计值的下界，上界和估计值
    conf.columns = ['2.5%', '97.5%', 'OR']
    print('各个变量对事件发生比的影响')
    print(np.exp(conf))
    print('各个变量的边际效应：')
    print(re.get_margeff(at='overall').summary()) # get_margeff


def makePrediciton(re, testSet, alpha=0.5):
    pd.options.mode.chained_assignment = None # 关闭告警
    testSet['prob'] = re.predict(testSet)
    print('事件发生概率（预测概率）大于0.6的数据个数：')
    print(testSet[testSet['prob'] > 0.6].shape[0])
    print('事件发生概率（预测概率）大于0.5的数据个数：')
    print(testSet[testSet['prob'] > 0.5].shape[0])
    testSet['pred'] = testSet.apply(
            lambda x: 1 if x['prob'] > alpha else 0, axis=1)
    return testSet


def evaluation(re):
    bins = np.array([0, 0.5, 1])
    label = re['label_code']
    pred = re['pred']
    tp, fp, fn, tn = np.histogram2d(label, pred, bins=bins)[0].flatten() # flatten？
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    print('查准率：%.3f,查全率%.3f,F1:%.3f' % \
          (precision, recall, f1))


def logitRegression(data):
    '''
    逻辑回归模型分析步骤展示
    ——————————————————————
    data:DataFrame
    '''
    data = transLabel(data)
    visualData(data)
    analyseData(data)
    trainSet, testSet = train_test_split(data,
                                         test_size=0.2,
                                         random_state=0)
    re = trainModel(trainSet)
    modelSummary(re)
    interpreModel(re)
    re = makePrediciton(re, testSet)
    evaluation(re)


if __name__ == '__main__':
    pd.set_option('display.width', 1000) # 设置显示格式
#    路径内有中文识别不了，所以注释掉了
#    homePath = os.path.dirname(os.path.abspath(__file__)) # ?
#    # 根据系统判断路径符号
#    if os.name == 'nt': # windows
#        dataPath = "%s\\adult.data" % homePath
#    else:
#        dataPath = "%s/adult.data" % homePath
    dataPath = 'adult.data'
    data = readData(dataPath)
    logitRegression(data)
