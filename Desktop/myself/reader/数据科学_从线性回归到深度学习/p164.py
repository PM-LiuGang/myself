# -*- coding: utf-8 -*-
"""
创建时间：Thu Feb  7 16:43:25 2019
描述：此脚本用于如何处理定性变量
作者: PM.LiuGang
Review:190301
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


def transLabel(data, columnsName):
    '''
    将文字变量转化为数字变量
    '''
    data[columnsName + '_code'] = pd.Categorical(data[columnsName]).codes 
    return data


def readData(path):
    '''
    读取指定文件的数据
    
    Parameters
    ----------
    path : str
        文件名称，可带路径名称或不带路径名称
        
    Returns
    -------
    data[col] : pd.DataFrame
        data
    '''
    data = pd.read_csv(path)
    cols = ["workclass",
            "sex",
            "age",
            "education_num",
            "capital_gain",
            "capital_loss",
            "hours_per_week",
            "label"] # 列名根据需求进行修改
    return data[cols]


def trainModel2(data):
    '''
    加入workclass变量，搭建逻辑回归模型，并训练模型
    
    Returns
    -------
    re : model
        训练好的模型
    '''
    l = [" ?",
         " Never-worked",
         " Without-pay",
         " State-gov",
         " Self-emp-not-inc",
         " Private",
         " Federal-gov",
         " Local-gov",
         " Self-emp-inc"]
    contrast = np.eye(9, 6, k=-3) # 对角单位矩阵
    contrast_mat = ContrastMatrix(contrast, l[3:]) # 对比矩阵
    formula = """label_code ~ C(workclass, contrast_mat, levels=l)
        + C(sex) 
        + education_num 
        + capital_gain
        + capital_loss 
        + hours_per_week""" # C ? 
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def trainModel3(data):
    '''
    加入性别变量，搭建逻辑回归模型，并训练模型
    '''
    l = [' Male', ' Female']
    contrast = [[-0.33], [0.67]]
    contrast_mat = ContrastMatrix(contrast, ['Ridit(sex)'])
    formula = """label_code ~ C(sex, contrast_mat, levels=l) 
        + education_num 
        + capital_gain 
        + capital_loss 
        + hours_per_week"""
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def trainModel(data):
    '''
    加入性别变量，搭建逻辑回归模型，并训练模型
    '''
    formula = '''
        label_code ~ C(sex) 
        + education_num 
        + capital_gain 
        + capital_loss 
        + hours_per_week'''
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def baseModel(data):
    '''
    基本逻辑回归模型
    '''
    formula = "label_code ~ education_num + capital_gain \
        + capital_loss + hours_per_week"
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()
    return re


def makePrediction(re, testSet, alpha=0.5):
    '''
    对验证集进行预测，然后对预测结果进行离散分类
    
    Parameters
    ----------
    re : model
        已训练好的模型
    testSet : pd.DataFrame
        验证集
    alpha : float
        阈值，如果大于阈值置1，否则置0
        
    Returns
    -------
    data pd.DataFrame
        添加预测概率列和分类标签
    '''
    pd.options.mode.chained_assignment = None
    data = testSet.copy()
    data['prob'] = re.predict(data)
    data['pred'] = data.apply(lambda x: 1 if x['prob'] > alpha else 0, axis=1)
    return data


def evaluation(newRe, baseRe):
    '''
    评估新模型和基础模型的效果（泛化能力）
    
    Parameters
    ----------
    newRe : [DataFrame,DataFrame3,DataFrame2.....]
        已添加预测概率列和分类标签
    baseRe : [DataFrame1,DataFrame2......]
        原始数据
    
    Returns
    -------
    matplotlib.pyplot.Axes
    '''
    # 加入性别后的模型
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.set_title('%s' % 'ROC曲线')
    ax.set_xlabel('Fales Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.plot([0, 1], [0, 1], 'g--', label='0-1单位对角线')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    note = ['加入workclass变量', '加入sex变量']
    color = list('ry')
    for seq, re in enumerate(newRe):        
        fpr, tpr, _ = metrics.roc_curve(re['label_code'],
                                        re['prob'])
        auc = metrics.auc(fpr, tpr)
        ax.plot(fpr, tpr,color[seq],    
                label='%s%s;%s = %0.2f' % (note[seq],'的ROC曲线', '曲线下面积（AUC）', auc))
    # 基础模型
    fpr, tpr, _ = metrics.roc_curve(baseRe['label_code'],
                                    baseRe['prob'])
    auc = metrics.auc(fpr, tpr)
    ax.plot(fpr, tpr, 'b-', 
            label='%s;%s = %0.2f' % ('加入性别前的ROC曲线', '曲线下面积（AUC）', auc))
    plt.legend(loc=4, shadow=True,)
    plt.show()
    
#def props(key): 
#    if ' >50K' in key:
#        return {'color': "#C6E2FF"}
#    else:
#        return {'color': '0.45'}

def analyseData(data):
    '''
    性别和标签（>50K,<=50K)的交叉关系
    '''
    cross1 = pd.crosstab(data['sex'], data['label'])
    print('显示sex & label交叉报表：')
    print(cross1)
    props = lambda key: {'color': "#C6E2FF"} \
                         if ' >50K' in key else {'color': '0.45'} # 每个块的颜色
    mosaic(cross1[[' >50K', ' <=50K']].stack(), properties=props, gap=0.05)
    plt.show()


def logitRegression(data):
    '''
    逻辑回归主程序
    '''
    data = transLabel(data,'label')
    analyseData(data)
    trainSet, testSet = train_test_split(data, test_size=0.2,random_state=2310)
    # 新模型
    modelSum = [trainModel2, trainModel3]
    newModelSum = []
    for m in modelSum:
        newRe = m(trainSet)
        print('{:*^70}'.format(m.__name__ + ':新模型OLS参数一览'))
        print(newRe.summary())
        newRe = makePrediction(newRe, testSet)
        newModelSum.append(newRe)
    # 基本模型
    baseRe = baseModel(trainSet)
    baseRe = makePrediction(baseRe, testSet)
    evaluation(newModelSum, baseRe)


if __name__ == '__main__':
    dataPath = 'adult.data'
    data = readData(dataPath)
    logitRegression(data)
