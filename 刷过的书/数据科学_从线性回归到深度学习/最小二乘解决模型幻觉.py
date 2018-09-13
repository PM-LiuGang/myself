# -*- coding: UTF-8 -*-
# 回归日期 2018-09-13
"""
此脚本用于如何使用统计方法解决模型幻觉
模型幻觉:在搭建模型的过程中，我们往往会从已知的特征中提取更多新的特征，并以此搭建更为复杂的模型
但是模型越复杂，值其本身越会掉入不断“自我催眠，强化偏见”的过程，从而引起过度拟合的问题,如果将
毫不相关的变量加入到模型中，也会得到相应的参数估计值，而这个估计值几乎不可能为0，这就造成了所谓的“模型幻觉”
模型幻觉会引起模型参数的不可靠，更严重的是使得原本可能较为正确的估计扭曲为错误,比如将原来变量
的正效应估计为负效应(变量对应的参数为正时成为正效应，否则为负效应)
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as smapi


def generate_randomvar():
    np.random.seed(4873)
    data_feature = np.random.randint(20, size=(100, 3))
    data_labels = np.random.randint(2, size=(100,))
    # data = np.hstack(data_feature,data_labels)
    return data_feature, data_labels


def train_model(x, y):
    # 训练模型
    model = smapi.OLS(x, y)  # 一个简单普通的最小二乘模型
    res = model.fit()
    return res


def evaluate_model(res):
    # 评估模型
    print(res.summary())
    print('检测假设z的系数等于0')
    # ValueError:shapes (100,3) and (100,3) not aligned: 3 (dim 1) != 100 (dim 0)
    print(res.f_test('z=0'))
    print('检测假设const的系数等于0')
    print(res.f_test('const'))
    print('检测假设z和const的系统同时等于0')
    print(res.f_test(['z=0', 'const=0']))


def confidence_interval(data):
    features = ['x']
    labels = ['y']


if __name__ == '__main__':
    df, dl = generate_randomvar()
    res = train_model(df, dl)
    evaluate_model(res)
