# -*- coding: utf-8 -*-
"""
创建时间 Wed Jan  2 15:52:24 2019
描述:
=========================================================================
下面的图示C的取值趋势对的权重系数变化变化的影响（注：采用的是L1正则化的惩罚项）
带有惩罚项的损失函数：newCost = C * oldCost + (1/2)*(‖w‖1**2)
C=1/λ C越小->权重系数也在不断减小，对权重系数惩罚也越来越大
λ越大，会缩小阴影球的球星面积，直至面积趋近为0，权重系数趋近于0
C<0.1,正则项威力很大时，所有特征权重都为0
Wine数据集是多类别数据，所以lr使用了One-vs-Rest(OvR)方法，所以lr.intercept_和
lr.coef_是三组值，分别属于三个模型：第一个模型用类别1 vs 类别2和3；第二个模型用
类别2 vs 类别1和3；第三个模型用类别3 vs 类别1和2
=========================================================================
review:090325
作者:PM.liugang
遗留：
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

plt.rcParams['font.sans-serif'] = ['SimHei']  # 输出中文
plt.rcParams['axes.unicode_minus'] = False  # 正负轴显示


def dataWash(xTrain, xTest, firstTrans, secondTrans):
    """
    Parameters
    ----------
    firstTrans:第一个数据标准化转化器
    secondTrans:第二个数据标准化转化器
    """
    xTrainNorm = firstTrans.fit_transform(xTrain)
    xTestNorm = firstTrans.transform(xTest)
    xTrainStd = secondTrans.fit_transform(xTrain)
    xTestStd = secondTrans.transform(xTest)
    return xTrainNorm, xTestNorm, xTrainStd, xTestStd


def showLogisticRegressionRegur(lr, xTrainStd, xTestStd, yTrain, yTest):
    """
    Parameters
    ----------
    lr:训练好的模型
    """
    print("C=0.1,多类别数据(采用OvR)，的情况下：")
    print('训练集的准确率:', lr.score(xTrainStd, yTrain))
    print('测试集的准确率:', lr.score(xTestStd, yTest))
    print('线性回归的截距:', lr.intercept_)  # 为什么会是[float1,float2,float3]
    print('线性回归的权重系数:')
    print("类1：", (lr.coef_[0]).round(4))
    print("类2：", (lr.coef_[1]).round(4))
    print("类3：", (lr.coef_[2]).round(4))

columns = ['class label', 'alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash',
           'Magnesium', 'Total phenois', 'Flavanoide', 'Nonflavamoid',
           'Proanthocyanins', 'Color intensity', 'Hue', 'OD2380/OD315', 'Proline']
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'pink',
          'lightgreen', 'lightblue', 'gray', 'indigo', 'orange']
mms = MinMaxScaler()
ss = StandardScaler()
lr = LogisticRegression(penalty="l1", C=0.1)
dfWine = pd.read_csv('wine_data.csv')
dfWine.columns = columns
dataFeature = dfWine.iloc[:, 1:]
dataLabel = dfWine.iloc[:, 0]
xTrain, xTest, yTrain, yTest = train_test_split(dataFeature, dataLabel,
                                                test_size=.3,
                                                random_state=0)

print("数据集标签是:{0}".format(np.unique(dfWine['class label'])))

if __name__ == "__main__":
    xTrainNorm, xTestNorm, xTrainStd, xTestStd = dataWash(
        xTrain, xTest, mms, ss)
    lr.fit(xTrainStd, yTrain)
    showLogisticRegressionRegur(lr, xTrainStd, xTestStd, yTrain, yTest)
    weights = []
    params = []
    for c in np.arange(-4., 6.):
        lr = LogisticRegression(penalty='l1', C=10**c, random_state=0)
        lr.fit(xTrainStd, yTrain)
        weights.append(lr.coef_[2])  # 取指定类别
        params.append(10 ** c)

    weights = np.array(weights)

    fig = plt.figure()
    ax = plt.subplot(111)
    for column, color in zip(range(weights.shape[1]), colors):
        plt.plot(params, weights[:, column],  # 依次画出每个特征与权重参数的图线
                 label=dfWine.columns[column+1],
                 color=color)
    plt.axhline(0, color='black', linestyle='--', linewidth=3)
    plt.xlim([10 ** (-5), 10 ** 5])
    plt.xlabel('$C$')  # 如果没有$，有warning
    plt.xscale('log')  # 图中显示的是(10**-5,10**5) 如果不加,(0,100000),以指数的方式显示
    plt.ylabel('权重系数')
    ax.legend(loc='upper center',
              bbox_to_anchor=(1.28, 1.03),  # 图例的位置
              ncol=1,  # 图例的列数
              fancybox=True,  # 图例是否有外框
              title="特征名称",  # 图例是否有标题
              fontsize=12)  # 图例的字体大小
    plt.show()
