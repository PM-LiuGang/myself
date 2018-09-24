# -*- coding: utf-8 -*-
"""
创建时间 Sat Sep 22 20:00:59 2018
描述:
作者:PM.liugang
"""

def cmPlot(yTrue, yPred):
    '''
    param yTrue
    param yPred
    return 可视化混淆矩阵
    '''
    cm = confusion_matrix(yTrue, yPred)  # 生成混淆矩阵
    plt.matshow(cm, cmap=plt.cm.Greens)  # 画混淆矩阵图，配色风格使用cm.Greens
    plt.colorbar()  # 颜色标签
    for x in range(len(cm)):  # 数据标签
        for y in range(len(cm)):
            plt.annotate(cm[x, y],
                         xy=(x, y),
                         horizontalalignment='center',
                         verticalalignment='center')
    plt.ylabel('True label')  # 坐标轴标签
    plt.xlabel('Predicted label')  # 坐标轴标签
    return plt