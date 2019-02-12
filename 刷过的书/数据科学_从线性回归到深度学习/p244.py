# -*- coding: utf-8 -*-
"""
创建时间：Mon Feb 11 20:26:44 2019
描述：展示GBTs
作者: PM.LiuGang
Review:
遗留：
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import GradientBoostingRegressor

plt.rcParams["font.sans-serif"]=["SimHei"]

def generateData(n):
    '''
    
    '''
    np.random.seed(1010)
    X = np.linspace(0,3*np.pi,num=n).reshape(-1,1)
    error = np.random.normal(0,0.1,size=n).reshape(-1,1)
    Y = np.abs(np.sin(X)) + error
    Y = np.where(Y>0.5,1,0)
    data = np.concatenate((Y,X),axis=1)
    data = pd.DataFrame(data,columns=['y','x'])
    return data


def trainModel(data):
    '''
    训练GBTs模型
    '''
    model = GradientBoostingRegressor(n_estimators=3,
                                      max_depth=2,
                                      learning_rate=0.8)
    model.fit(data[['x']],data['y'])
    return model


def visualize(data,model):
    '''
    将模型结果可视化
    '''
    fig = plt.figure(figsize=(6,6),dpi=80)
    ax = fig.add_subplot(111)
    ax.scatter(data['x'],data['y'],label='_nolegend_') # nolegend !
    styles = ['b--','r-.','gray']
    labels = ["深度=1", "深度=2", "深度=3"]
    # model.staged_predict Predict regression target at each stage for X
    for l,s,pred in zip(labels,
                        styles,
                        model.staged_predict(data[['x']])):
        plt.plot(data[['x']],
                 pred, # len() = 40 
                 s,
                 label=l)
    ax.legend(loc='upper center',
              bbox_to_anchor=(0.5,1.05), # 从左到右 从下到上
              ncol=3,
              fancybox=True,
              shadow=True)
    plt.show()
    
    
if __name__ == '__main__':
    data = generateData(40)
    model = trainModel(data)
    visualize(data,model)
    
    
    

