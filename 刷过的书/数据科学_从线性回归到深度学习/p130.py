# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb  5 16:26:51 2019
描述：展示使用逻辑回归解决多元分类问题
作者: PM.LiuGang
Review:
遗留：每个散点图的点（含义）不理解
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LogisticRegression

plt.rcParams["font.sans-serif"] = ["SimHei"]


def readData(path):
    data = pd.read_csv(path, encoding='utf-8')
    data.columns = ['label', 'x1', 'x2']
    return data


def multiLogit(data):
    '''
    使用（不同方法）逻辑回归对多元分类问题建模，并可视化结果
    '''
    features = ['x1', 'x2']
    labels = 'label'
    fig = plt.figure(figsize=(8, 3), dpi=80)
    methods = ['multinomial', 'ovr']
    for i in range(len(methods)):
        model = LogisticRegression(multi_class=methods[i],
                                   solver='sag',
                                   max_iter=1000,
                                   random_state=42)
        model.fit(data[features], data[labels])
        x1Min, x2Min = np.min(data[features]) - 0.5
        x1Max, x2Max = np.max(data[features]) + 0.5
        area = np.dstack(np.meshgrid(np.arange(x1Min, x1Max, 0.02),
                                     np.arange(x2Min, x2Max, 0.02)))  
        area = area.reshape(-1,2) # 生成Cartesian积
        pic = model.predict(area)
        ax = fig.add_subplot(1, 2, i + 1)
        colors = np.array(['blue', 'gray', 'white']) # blue replace black
        ax.scatter(area[:, 0], 
                   area[:, 1],
                   c=colors[pic], # ?
                   alpha=0.3,
                   s=4, # size
                   edgecolors=colors[pic]) # ?
        ax.scatter(data['x1'], 
                   data['x2'],
                   c=colors[data[labels]], # ?
                   edgecolors='red')
        ax.set_xlim(x1Min, x1Max)
        ax.set_ylim(x2Min, x2Max)
    plt.show()


if __name__ == '__main__':
    dataPath = 'multi_logit.csv'
    data = readData(dataPath)
    multiLogit(data)
