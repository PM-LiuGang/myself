# -*- coding: utf-8 -*-
"""
创建时间：Mon Feb  4 21:01:32 2019
描述：
作者: PM.LiuGang
Review:20190220
遗留：
"""

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np

from sklearn.model_selection import train_test_split
from statsmodels.graphics.mosaicplot import mosaic # 马赛克图


def modelSummary(re):
    '''
    分析逻辑回归模型的统计性质
    
    Parameters
    ----------
    re : model
        statsmodel
        
    Return
    ------
    f_test's result
    '''
    print(re.summary())
    print('检验假设education num的系数等于0：')
    print(re.f_test('education_num=0'))
    print('检验假设education num的系数等于0.32和hours per week的系数等于0')
    print(re.f_test('education_num=0.32,hours_per_week=0.04'))


def visualData(data):
    '''
    可视化数据中的指定四列：年龄，每周工作时间，受教育年龄，标签编码
    
    Parameters
    ----------
    data : pd.DataFrame
    
    Returns
    -------
    matplotlib.pyplot.Axes
    '''
    data[['age', 'hours_per_week', 'education_num', 'label_code']].hist(
        rwidth=0.5, # 柱子的宽度
        grid=False, # 是否显示坐标网格线
        figsize=(8, 8),
        alpha=0.6,
        color='grey') # 灰白


def analyseData(data):
    '''
    数据的统计和多列交叉报表
    
    Parameters
    ----------
    data : pd.DataFrame
    
    Returns
    -------
    matplotlib.pyplot.Axes
    '''
    print('{:*^60}'.format('显示基本统计信息'))
    print(data.describe(include='all'))
    cross1 = pd.crosstab(pd.qcut(data['education_num'],
                                 [0, .25, .5, .75, 1]), # 存在None值
                                 data['label'])
    print('{:*^60}'.format('显示education num和label交叉报表'))
    print(cross1)
    props = lambda key:{'color': '#FF00FF'} if ' >50K' in key \
        else {'color': '#0000FF'}
    mosaic(cross1[[' >50K', ' <=50K']].stack(), properties=props, gap=0.03)
    print('{:*^60}'.format('# 计算hours per week，label交叉报表'))
    cross2 = pd.crosstab(pd.cut(data['hours_per_week'], 5), data['label'])
    print(cross2)
    cross2_norm = cross2.div(cross2.sum(1).astype(float), axis=0) # axis=0->TypeError
    print('{:*^60}'.format('显示hour per week和label交叉报表(占比)'))
    print(cross2_norm)
    cross2_norm.plot(kind='bar', rot=0) # rot 旋转刻度标签
    plt.show()

def trainModel(data):
    '''
    使用逻辑回归训练模型
    
    Parameters
    ----------
    data : pd.DataFrame
    
    Returns
    -------
    re : fitted Logit-model
    '''
    formula = 'label_code ~ age + education_num + capital_gain + \
        capital_loss + hours_per_week' # ~(=)
    model = sm.Logit.from_formula(formula, data=data) 
    re = model.fit()
    return re


def transLabel(data):
    '''
    将data['label']文字变量转换为数字变量
    
    Parameters
    ----------
    data : pd.DataFrame
    
    Return
    ------
    data : pd.DataFrame 
        新增一列，将原label列转换成数字标签
    '''
    data['label_code'] = pd.Categorical(data.label).codes
    return data


def readData(path):
    '''
    读取数据,提取指定列数据，生成新data
    
    Parameters
    ----------
    path : str
        要读取的文件名称，路径可选
        
    Returns
    -------
    data[cols] : pd.DataFrame
        指定数据的五列
    '''
    data = pd.read_csv(path,encoding='utf-8')
    cols = ['age', 
            'education_num', 
            'capital_gain', 
            'capital_loss',
            'hours_per_week', 
            'label']
    return data[cols]


def interpreModel(re):
    '''
    统计模型的置信度区间、参数系数，模型的边际效应
    
    Parameters
    ----------
    re : model
        fitted model
        
    Returns
    -------
    None
    '''
    conf = re.conf_int() # 返回每个参数的置信度区间 shape=6,2
    conf['OR'] = re.params # 返回每个参数的系数 shape=6,3
    conf.columns = ['2.5%', '97.5%', 'OR']
    print('各个变量对事件发生比的影响')
    print(np.exp(conf))
    print('各个变量的边际效应：')
    print(re.get_margeff(at='overall').summary()) # 拟合模型的边际效应


def makePrediciton(re, testSet, alpha=0.5):
    '''
    通过模型的预测结果将样本二分类
    
    Parameters
    ----------
    re : fitted model
        已训练完成的逻辑回归模型
    testSet : pd.DataFrame
        验证数据集
    alpha : int or float
        阈值
    Returns
    -------
    testSet : pd.DataFrame
        验证数据集，增加了样本的预测标签列['pred']
    '''
    pd.options.mode.chained_assignment = None # 关闭告警
    testSet['prob'] = re.predict(testSet)
    print('事件发生概率（预测概率）大于0.6的数据个数：')
    print(testSet[testSet['prob'] > 0.6].shape[0])
    print('事件发生概率（预测概率）大于0.5的数据个数：')
    print(testSet[testSet['prob'] > 0.5].shape[0])
    testSet['pred'] = testSet.apply(lambda x: \
               1 if x['prob'] > alpha else 0, axis=1)
    return testSet


def evaluation(data):
    '''
    通过查准率和查全率评估模型
    
    Parameters
    ----------
    re : model
        fitted logit-model
        
    Returns
    -------
    Precision,Recall,F1
    '''
    bins = np.array([0, 0.5, 1])
    label = data['label_code']
    pred = data['pred']
    tp, fp, fn, tn = np.histogram2d(label, pred, bins=bins)[0].flatten()
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    print('查准率：%.3f,查全率%.3f,F1:%.3f' % \
          (precision, recall, f1))


def logitRegression(data):
    '''
    逻辑回归模型分析步骤展示
    
    Parameters
    ----------
    data : DataFrame
    
    Returns
    -------
    
    '''
    data = transLabel(data) 
    visualData(data)
    analyseData(data)
    trainSet, testSet = train_test_split(data, test_size=0.2, random_state=0)
    re = trainModel(trainSet)
    modelSummary(re)
    interpreModel(re)
    re = makePrediciton(re, testSet)
    evaluation(re)


if __name__ == '__main__':
    pd.set_option('display.width', 1000) # 设置显示格式
    '''
    路径内有中文识别不了，所以注释掉了
    homePath = os.path.dirname(os.path.abspath(__file__)) # 识别当前文件的所在路径
    # 根据系统判断路径符号
    if os.name == 'nt': # windows
        dataPath = "%s\\adult.data" % homePath
    else:
        dataPath = "%s/adult.data" % homePath
    '''
    dataPath = 'adult.data'
    data = readData(dataPath)
    logitRegression(data)
