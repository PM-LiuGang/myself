# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb 12 18:30:24 2019
描述：展示KMeans模型的收敛过程
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs 

def generateData(n):
    '''
    生成随机的无标签聚类数据
    '''
    centers = [[1,1],[-1,1]]
    X,_ = make_blobs(n_samples=n, # 样本总数目 _ feature.shape
                     centers=centers,
                     cluster_std=.5) # 标准差
    return X


def visualizeData(data):
    '''
    将训练数据可视化
    '''
    fig = plt.figure(figsize=(6,6),dpi=80)
    ax = fig.add_subplot(111)
    ax.scatter(data[:,0],data[:,1])
    ax.get_xaxis().set_visible(False) # 返回X轴实例，并设置不可见
    ax.get_yaxis().set_visible(False)
    plt.show()
    
    
def visualizeModel(ax,data,labels,centers):
    '''
    将模型结果可视化
    '''
    colors = ['#82CCFC','k']
    if labels is None:
        ax.scatter(data[:,0],
                   data[:,1])
    else:
        ax.scatter(data[:,0],
                   data[:,1],
                   c=[colors[i] for i in labels],
                   marker='o',
                   alpha=0.6)
    ax.scatter(centers[:,0],
               centers[:,1],
               marker='*',
               c=colors,
               edgecolors='white',
               s=700,
               linewidths=2)
    ax.get_xaxis().set_visible(False) 
    ax.get_yaxis().set_visible(False)
    

def trainModel(data,step):
    '''
    使用KMeans模型对数据聚类
    '''
    model = KMeans(n_clusters=2,
                   init=np.array([[1,-1],[-1,1]]),
                   max_iter=step, # 最大迭代次数（EM）
                   algorithm='full', # 使用EM算法
                   n_init=1) # 算法重复的次数
    model.fit(data)
    return model


def run(data):
    '''
    主程序
    '''
    fig = plt.figure(figsize=(10,10),dpi=80)
    for i in range(4):
        ax = fig.add_subplot(2,2,i+1)
        if i==0:
            visualizeModel(ax,
                           data,
                           None,
                           np.array([[1,-1],[-1,1]]))
        else:
            model = trainModel(data,i)
            visualizeModel(ax,
                           data,
                           model.labels_, # [0,1,2....]
                           model.cluster_centers_)
    plt.show()
    
    
if __name__ == '__main__':
    np.random.seed(1001)
    data = generateData(400)
    visualizeData(data)
    run(data)
    
    
    



    
              
    