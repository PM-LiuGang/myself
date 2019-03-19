# -*- coding: utf-8 -*-
"""
创建时间：Tue Feb  5 21:37:22 2019
描述：展示不平衡的数据对模型的影响
作者: PM.LiuGang
Review:190311
遗留：
----------------------------------
np.random.multvariate_normal:
mean = [0, 0]
cov = [[1, 0], [0, 100]]  # diagonal covariance
import matplotlib.pyplot as plt
x, y = np.random.multivariate_normal(mean, cov, 5000).T
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()

"""
import numpy as np
import matplotlib.pyplot as plt
import warnings

from sklearn import metrics
from sklearn.linear_model import LogisticRegression

plt.rcParams["font.sans-serif"] = ["SimHei"]
warnings.filterwarnings('ignore')


def generateData(n):
    '''
    产生均衡的逻辑回归数据
    '''
    np.random.seed(4060)
    mean = [0,0]
    cov = [[1, 0], [0, 1]]
    # 生成多元正态分布矩阵 X.shape=(n,2)
    X = np.random.multivariate_normal(mean, cov, n)  
    beta = np.array([1, -1]).reshape(2, 1)
    error = np.random.logistic(size=n).reshape(-1, 1)
    # Y.shape = (2000,1) true + 0 = 1;False + 0 = 0
    Y = (np.dot(X, beta) + error > 0) + 0 
    return X, Y


def unbalanceData(X, Y, zeroTimes):
    '''
    通过将类别0的数据重复zeroTimes次，将均衡数据集变为非均衡数据集
    平衡：Y=0 1010 X=0 990 非平衡：Y=0 1010 X=0 990*zeroTimes
    
    Parameters
    ----------
    X : np.ndarray
        数据集-不含标签
    Y : np.ndarray
        数据集的标签
    zeroTimes : int
        数据重复的次数
    Returns
    -------
    X0X1 : np.ndarray
        非平衡数据集-不含标签
    Y0Y1 : np.ndarray
        非平衡数据集的标签
    '''
    # 为什么X0，Y0是(np.array,np.arrar)结构 
    # np.where的返回结果 np.where(condition)->tuple of ndarrays
    # np.where(Y==0)[0]取出索引（行数）
    X0 = np.repeat(X[np.where(Y == 0)[0]], zeroTimes, axis=0) # X0.shape = (990 * zeroTimes, 2)
    Y0 = np.repeat(Y[np.where(Y == 0)[0]], zeroTimes, axis=0) # Y0.shape =(990*n,1)
    X1 = X[np.where(Y > 0)[0]] # shape (1010,1)
    Y1 = Y[np.where(Y > 0)[0]]
    X0X1 = np.append(X0, X1, axis=0)
    Y0Y1 = np.append(Y0, Y1, axis=0)
    return X0X1, Y0Y1


def logitModel(X, Y):
    '''
    搭建逻辑回归模型，并得到预测结果
    '''
    model = LogisticRegression(C=1e4)  # 为了消除惩罚项的干扰，将惩罚系数设为很大
    model.fit(X, Y.ravel())
    pred = model.predict(X)
    return pred


def visualize(ratios, predPositive, truePositive, aucs, accuracies,
              title):
    '''
    将模型可视化
    
    Parameters
    ----------
    ratios : [float,float,float,....,n(zeroTimes)]
        原始数据集里Y>0的占比
    predPositive : np.array [int,int,int,...,n(zeroTimes)]
        通过model预测标签Y>0的数目
    truePositive : np.array [int,int,int,...,n(zeroTimes)]
        数据集中原始标签Y>0的数目
    aucs : [float,float,float,....,n(zeroTimes)]
        auc的面积
    accuracies : [float,float,float,....,n(zeroTimes)]
        auc的准确率
    Returns
    -------
    
    '''
    fig = plt.figure(figsize=(8, 3), dpi=80)
    ax = fig.add_subplot(1, 2, 1)
    plt.suptitle(title) # 图标总标题
    ax.plot(ratios, predPositive, label='%s' % '预测结果里类别1的个数')
    ax.plot(ratios, truePositive, 'k--', label='%s' % '原始数据集里类别1的个数')
    ax.set_xlabel("原始数据集Y>0的占比")
    ax.set_ylabel("原始数据集Y>0的数量")
    ax.set_xlim([0, 0.5])
    ax.invert_xaxis()  # 将x或y轴逆序显示
    plt.legend(shadow=True, loc='best')

    ax1 = fig.add_subplot(1, 2, 2)
    ax1.plot(ratios, aucs, 'r', label='%s' % '曲线下的面积（AUC）')
    ax1.plot(ratios, accuracies, 'k-', label='%s' % '准确度（ACC）')
    ax1.set_xlabel("原始数据集Y>0的占比")
    ax1.set_ylabel("Value")
    ax1.set_xlim([0, 0.5])
    ax1.set_ylim([0.5, 1])
    ax1.invert_xaxis()
    plt.legend(shadow=True, loc='best')


def evaluateModel(Y, pred,title=None):
    '''
    评估模型效果，其中包括ACC、AUC以及预测结果中类别1的个数
    
    Parameters
    ----------
    Y : np.array [array([]), array([]), array([]), array([])...]
        数据集的类标签
    pred : np.array [array([]), array([]), array([]), array([])...]
        模型预测数据的类标签    
    '''
    predPositive = [] 
    truePositive = [] 
    aucs = [] 
    accuracies = [] 
    ratios = [] 
    for i in range(len(Y)):
        ratios.append(len(Y[i][Y[i] > 0]) / float(len(Y[i])))
        predPositive.append(len(pred[i][pred[i] > 0]))
        truePositive.append(len(Y[i][Y[i] > 0]))
        fpr, tpr, _ = metrics.roc_curve(Y[i], pred[i]) # fpr,tpr,_->array([x,x,x])
        accuracies.append(metrics.accuracy_score(Y[i], pred[i]))
        aucs.append(metrics.auc(fpr, tpr))
    visualize(ratios, predPositive, truePositive, aucs, accuracies,
              title=title)


def balanceData(X, Y):
    '''
    通过调整各个类别的比重，解决非均衡数据集的问题
    '''
    positiveWeight = len(Y[Y > 0]) / float(len(Y))
    classWeight = {1: 1. / positiveWeight, \
                   0: 1. / (1 - positiveWeight)}
    model = LogisticRegression(class_weight=classWeight, C=1e4)
    model.fit(X, Y.ravel())
    pred = model.predict(X)
    return pred


def imbalanceDataEffect():
    '''
    展示非均衡数据集对搭建模型的影响
    '''
    X, Y = generateData(2000)
    trueY = []
    predY = []
    balancePredY = []
    for zeroTimes in np.arange(1, 100): # 为什么改成4，只有两幅图
        _X, _Y = unbalanceData(X, Y, zeroTimes)
        trueY.append(_Y) 
        predY.append(logitModel(_X, _Y))
        balancePredY.append(balanceData(_X, _Y))
    evaluateModel(trueY, predY, title="非平衡数据集")
    evaluateModel(trueY, balancePredY, title="平衡数据集")


if __name__ == '__main__':
    imbalanceDataEffect()
