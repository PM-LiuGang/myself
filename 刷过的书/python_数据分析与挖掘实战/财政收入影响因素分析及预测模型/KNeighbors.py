# -*- coding: utf-8 -*-
"""
创建时间 Wed Jan 23 10:57:12 2019
作者:PM.liugang
review:190307
描述:
1.确定k大小和距离度量
2.对于测试集中的一个样本，找到训练集中和它最近的k个样本
3.将这k个样本的投票结果作为测试样本的类别
通常欧氏距离用于实数域的数据集，此时一定要对特征进行标准化，每一维度特征的重要性等同
遗留：
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

sys.path.append('C:\\Users\\Administrator\\Desktop\\myself')
from plotClassifierRegions import plot_decision_regions

'''搭建模型'''
knn = KNeighborsClassifier(n_neighbors=5, # 最近的5个样本 default n_neighbors=5
                           p=2, # default p=2退化为欧氏距离 p=1 退化为曼哈顿距离
                           metric='minkowski') # 距离度量方式 default minkowski

def showModel(trainData, testData, y_train, y_test, classifier=None):
    """
    可视化模型
    
    Parameters
    ----------
    trainData : np.array
        训练数据
    testData : np.array
        测试数据
    y_train : np.array
        训练数据标签
    y_test : np.array
        测试数据集标签
    classifier : 
        分类器
        
    Returns
    -------
    
    """
    sc = StandardScaler()
    sc.fit(trainData)
    trainDataDf = pd.DataFrame(trainData)
    print('{:*^35}'.format('原始数据概况'))
    print(trainDataDf.describe())
    X_train_std = sc.transform(trainData)
    print('{:*^35}'.format('标准化后数据概况'))
    X_train_std_df = pd.DataFrame(X_train_std)
    print(X_train_std_df.describe())  
    X_test_std = sc.transform(testData)
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))
    
    knn.fit(X_train_std,y_train)
    
    plot_decision_regions(X_combined_std,y_combined,
                      classifier=knn,
                      test_idx=range(105,150))
    plt.xlabel('Petal Length [Standardized]')
    plt.ylabel('Petal Width [Standardized]')
    plt.show()


if __name__ == "__main__":
    iris = datasets.load_iris()
    X = iris.data[:,[2,3]]
    y = iris.target
    print('数据分为%s类,分别是' % len(np.unique(y)))
    X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                      test_size=0.3,
                                                      random_state=0)
    showModel(X_train, X_test, y_train, y_test, knn)
    