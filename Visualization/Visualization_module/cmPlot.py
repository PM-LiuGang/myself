# -*- coding: utf-8 -*-
"""
创建时间 Sat Sep 22 20:00:59 2018
描述:分类可视模块
作者:PM.liugang
"""
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix

def cmPlot(yTrue, yPred):
    '''
    可视化混淆矩阵
    
    Parameters
    ----------
    yTrue : np.array or pd.DataFrame or pd.Series
        原始数据集中的分类标签
    yPred : np.array or pd.DataFrame or pd.Series
        测试数据集中的预测分类标签
    
    Returns 
    -------
    可视化混淆矩阵
    '''
    cm = confusion_matrix(yTrue, yPred)  # 生成混淆矩阵
    plt.matshow(cm, cmap=plt.cm.Greens)  # 配色风格使用cm.Greens
    plt.colorbar()  # 颜色柱标签
    for x in range(len(cm)):
        for y in range(len(cm)): # 混淆矩阵都是方阵
            plt.annotate(cm[x, y],
                         xy=(x, y),
                         horizontalalignment='center',
                         verticalalignment='center')
    plt.ylabel('True Label')  # 坐标轴标签
    plt.xlabel('Predicted Label')  # 坐标轴标签
#    return plt 
    plt.show()
    