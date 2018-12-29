# -*- coding: utf-8 -*-
"""
创建时间 Fri Dec 28 13:30:35 2018
描述:LDA线性判别区分
作者:PM.liugang
遗留：转换矩阵W与书中不一致 eigenPairs[1][1] 符号相反
"""

'''
LDA:监督算法:
LDA方法的关键步骤：
1.对d维数据集进行标准化处理（d为特征的数量）
2.对于每一个类别，计算d维的均值向量
3.构造类间的散步矩阵Sb以及类内的散步矩阵Sw
4.计算矩阵Sw的-1次幂 * Sb的特征值及对应的特征向量
5.选取前k个特征值所对应的特征向量，构造一个d*k维的转换W,其中特征向量以列的形式排列
6.使用转换矩阵W将样本映射到新的特征子空间上
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

plt.rcParams['font.sans-serif'] = ['SimHei'] # 输出中文
plt.rcParams['axes.unicode_minus'] = False # 正负轴显示

# 准备数据
dfWine = pd.read_csv('wine_data.csv')  # 原文是heared=None->error
x, y = dfWine.iloc[:, 1:].values, dfWine.iloc[:, 0].values
x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.3,
                                                    random_state=0)
# 数据标准化处理
sc = StandardScaler()
xTrainStd = sc.fit_transform(x_train)
xTestStd = sc.fit_transform(x_test)

'''计算散步矩阵'''
# 三个类别类别内对应的三个均值向量
np.set_printoptions(precision=4)  # 控制打印精度
meanVecs = []
for label in range(1, 4):
    meanVecs.append(np.mean(xTrainStd[y_train == label], axis=0))
    print('均值向量 %s: %s\n' % (label, meanVecs[label-1]))

# 通过均值向量计算类内散布矩阵,通过各类别的散步矩阵来计算
d = 13
SW = np.zeros((d, d))
for label, mv in zip(range(1, 4), meanVecs):
    classScatter = np.zeros((d, d))
    for row in x[y == label]:
        row, mv = row.reshape(d, 1), mv.reshape(d, 1)
        classScatter += (row-mv).dot((row-mv).T)  # P87
    SW += classScatter  # SW.shape (13,13)

print('内散步矩阵: %sx%s' % (SW.shape[0], SW.shape[1]))
# 假设训练集的类标签是均匀分布的，实际情况np.bincounty->[0,40,49,35]
print('类标签分布: %s' % np.bincount(y_train)[1:])  # =value_counts
print('=' * 60)
# 对各类别的散布矩阵做缩放处理，通过各类别单独的散布矩阵除以此类别内样本数量
SW = np.zeros((d, d))
for label, mv in zip(range(1, 4), meanVecs):
    classScatter = np.cov(xTrainStd[y_train == label].T)  # 协方差矩阵
    SW += classScatter
print('标准化内散布矩阵 %sx%s' % (SW.shape[0], SW.shape[1]))
# 类间散布矩阵
meanOverall = np.mean(xTrainStd, axis=0)
# meanOverall.shape (13,1) xTrainStd.shape (124,13) ?
SB = np.zeros((d, d))
for i, meanVecs in enumerate(meanVecs):
    n = x[y == i+1, :].shape[0]
    meanVecs = meanVecs.reshape(d, 1)
    meanOverall = meanOverall.reshape(d, 1)
    # ↓ 原文中缩进错误，在for循环里
    SB += n * (meanVecs-meanOverall).dot((meanVecs-meanOverall).T)  # P87

print('类间散布矩阵 %sx%s' % (SB.shape[0], SB.shape[1]))
print('=' * 60)

'''在特征子空间上的选取线性判别算法'''
eigenVals, eigenVecs = np.linalg.eig(np.linalg.inv(SW).dot(SB))
eigenPairs = [(np.abs(eigenVals[i]), eigenVecs[:, i])
              for i in range(len(eigenVals))]  # \space
eigenPairs = sorted(eigenPairs, key=lambda k: k[0], reverse=True)
print('降序对特征值进行排序: \n')

'''按照特征值降序绘制出特征对线性判别信息保持程度的图像'''
# 图像所用数据源自定义(原文中代码报错)，结果与书中一致
##########myself################
tot = []
for eigenVals in eigenPairs:
    print(eigenVals[0])
    tot.append(eigenVals[0])

discr = []
for i in tot:
    discr.append(i/sum(tot))
##########myself################
cum_discr = np.cumsum(discr)
plt.bar(range(1, 14),
        discr,
        alpha=0.5,
        align='center',
        label='单个特征区分')
plt.step(range(1, 14),
         cum_discr,
         where='mid',
         label='累计区分')
plt.ylabel('区分率')
plt.xlabel('线性判别')
plt.ylim([-0.1, 1.1])
plt.legend(loc='best')
plt.show()

'''原始数据映射到新特征空间'''
w = np.hstack((eigenPairs[0][1][:,np.newaxis].real,
              eigenPairs[1][1][:,np.newaxis].real)) # w.shape is (13,2)
print('========矩阵:W========= \n',w)
xTrainLda = xTrainStd.dot(w)
colors = list('rbg')
markers = list('sxo')
for l, c, m in zip(np.unique(y_train),colors, markers):
    plt.scatter(xTrainLda[y_train==1,0],
                xTrainLda[y_train==1,1],
                c=c,
                label=l,
                marker=m)
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.legend(loc='upper right')
plt.show()

