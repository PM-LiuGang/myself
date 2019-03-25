# -*- coding: utf-8 -*-
"""
创建时间 Mon Jan  7 12:10:24 2019
作者:PM.liugang
描述:逻辑斯谛回归对类别概率建模；线性二分类模型：分类模型；
可以使用OvR技巧扩展为多分类模型；逻辑回归中激活函数变成了sigmod函数
逻辑斯谛不但能预测类别，还能输出具体的概率值，很多场景概率往往比淡出
的类别值重要的多
遗留：
review:190312
"""
import sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\myself')
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from plotClassifierRegions import plot_decision_regions

def sigmod(z):
    """sigmod分布函数
    
    Parameters
    ----------
    z : np.ndarray
        数据横坐标
    
    Returns
    -------
    P(概率)
    """
    return 1.0 / (1.0+np.exp(-z)) # F分布函数


def logisticDistributionVisual(z):
    """可视化Logistics分布的函数图形
    Parameters
    ----------
    z : np.ndarray
        横坐标
    
    Returns
    -------
    
    """
    phiZ = sigmod(z)
    plt.plot(z, phiZ)
    plt.axhspan(0, 1, facecolor='w', alpha=1.0, edgecolor='r')
    plt.axhline(y=0.5, color="k")
    plt.axvline(0, 0, color="k")
    plt.yticks([0.0, 0.5, 1.0])
    plt.ylim(-0.1, 1.1)
    plt.xlabel("z")
    plt.ylabel("$\phi(z)$")
    plt.title("Logistic分布函数图形")
    plt.show()


def dataCollation(trainData, testData, trainLabel, testLabel):
    """
    
    """
    sc = StandardScaler()
    sc.fit(trainData)
    xTrainStd = sc.transform(trainData)
    xTestStd = sc.transform(testData)
    xCombinedStd = np.vstack((xTrainStd, xTestStd))
    yCombine = np.hstack((trainLabel, testLabel))
    return xTrainStd, xTestStd, xCombinedStd, yCombine


iris = datasets.load_iris()
trainData = iris.data[:,[2,3]]
trainLabel = iris.target
print("训练数据的形状：",trainData.shape)
print("训练数据共有%s类" % (len(np.unique(trainLabel))))    
X_train, X_test, y_train, y_test = train_test_split(
        trainData,trainLabel,
        test_size=0.3,
        random_state=0)



if __name__ == "__main__":
    z = np.arange(-7,7,0.1)
    logisticDistributionVisual(z)
    xTrainStd, xTestStd, xCombinedStd, yCombine = dataCollation(X_train, 
                                                                X_test, 
                                                                y_train, 
                                                                y_test)
    lr = LogisticRegression(C=1000.0,random_state=0)
    lr.fit(xTrainStd, y_train)
    plot_decision_regions(xCombinedStd,yCombine,
                          classifier=lr,
                          test_idx=range(105,150)) # 105-150是验证集
    plt.xlabel('花瓣长度（标准化后）')
    plt.ylabel('花瓣宽度（标准化后）')
    plt.legend(loc='upper left')
    plt.show()
    # 预测输出概率
    lr_proba = lr.predict_proba(X_test[0,:].reshape(1,-1)) 
    for i,p in enumerate(lr_proba[0]):
        print('属于第%d类的概率是%.2f%%' % (i+1,p * 100))
    

