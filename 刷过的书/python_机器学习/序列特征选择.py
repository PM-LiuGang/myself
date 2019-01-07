# -*- coding: utf-8 -*-
"""
创建时间 Thu Jan  3 13:48:59 2019
作者:PM.liugang
描述:序列特征选择算法
遗留：fit代码有一块不明白
通过特征选择进行维度降低，这个方法尤其对非正则模型有用
维度降低有两种做法：1.特征选择和2.特征抽取
特征选择：从原始特征集中选择一个子集合，其中一种方法
序列特征选择：用于将原始的d维度特征空间降低到k维度特征子空间，其中，k<d,算法原理是
自动选择一个特征子集，子集中的特征都是和问题最相关的特征，由于溢出了不相干特征和
噪音也降低了模型的泛化误差
经典的序列特征选择算法是序列后向选择（SBS)，其步骤为：
1.初始化k=d，其中d是原始特征维度
2.确定那个评价函数最大的特征，评价函数？
3.从Xk中移除特征x_,k=k-1
4.如果k等于事先确定的阈值则终止，否则，回到步骤2
========================================================
from itertools import combinations
创建一个迭代器，返回iterable中所有长度为r的子序列,\
返回的子序列中的项按输入iterable中的顺序排序
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.base import clone  # 克隆模型，只带参数，不带任何数据
from itertools import combinations
from sklearn.cross_validation import train_test_split  # 0.20 will be removed
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

plt.rcParams['font.sans-serif'] = ['SimHei']  # 输出中文
plt.rcParams['axes.unicode_minus'] = False  # 正负轴显示


class SBS():
    def __init__(self, estimator, k_features, scoring=accuracy_score,
                 test_size=0.25, random_state=1):
        '''
        序列特征选择算法
        ———————————————
        estimator：评估器
        k_features：想要得到的特征子集数
        scoring：准确率
        test_size：分割尺寸
        '''
        self.scoring = scoring
        self.estimator = clone(estimator)
        self.k_features = k_features
        self.test_size = test_size
        self.random_state = random_state

    def fit(self, X, y):
        '''
        拟合数据集与类标签
        ———————————————
        X 训练集
        y 类标签
        '''
        X_train, X_test, y_train, y_test = \
            train_test_split(X, y, test_size=self.test_size,random_state=self.random_state)
        dim = X_train.shape[1]  # 维数
        self.indices_ = tuple(range(dim)) 
        self.subsets_ = [self.indices_] # [()]?
        score = self._calc_score(X_train, y_train, X_test, y_test,self.indices_)
        self.scores_ = [score]

        while dim > self.k_features: # 当维数大于想要得到的特征数时
            scores = []
            subsets = []
            for p in combinations(self.indices_, r=dim-1):
                score = self._calc_score(X_train, y_train, X_test, y_test, p)
                scores.append(score)
                subsets.append(p)

            best = np.argmax(scores) # 返回最大值对应的索引（行或列），如果不指定轴，默认先左后右，先上后下
            self.indices_ = subsets[best]
            self.subsets_.append(self.indices_)
            dim -= 1
            self.scores_.append(scores[best])
        self.k_score_ = self.scores_[-1]
        return self

    def transform(self, X):
        '''
        按索引抽取训练集中指定列
        ——————————————————————
        X 训练集
        '''
        return X[:, self.indices_]

    def _calc_score(self, X_train, y_train, X_test, y_test, indices):
        '''
        计算验证集（类标签）与预测的准确率得分
        ———————————————————————————————————
        X_train 训练集数据
        y_train 训练集类标签
        X_test 验证集数据
        y_test 验证集类标签
        '''
        self.estimator.fit(X_train[:, indices], y_train)
        y_pred = self.estimator.predict(X_test[:, indices])
        score = self.scoring(y_test, y_pred)
        return score


# 准备数据
dfWine = pd.read_csv('wine_data.csv')  # df.shape is (178,14)
dfWine.columns = ['class label', 'alcohol', 'Malic acid', 'Ash',
                  'Alcalinity of ash', 'Magnesium', 'Total phenois',
                  'Flavanoide', 'Nonflavamoid', 'Proanthocyanins',
                  'Color intensity', 'Hue', 'OD2380/OD315', 'Proline']
print('Class labels', np.unique(dfWine['class label']))
print('*' * 20)
# 分割数据
X, y = dfWine.iloc[:, 1:].values, dfWine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=0)
# MinMaxScaler
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)
# StandardScaler
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)
# 建模 拟合 特征数与准确率的趋势变化图
knn = KNeighborsClassifier(n_neighbors=2)
sbs = SBS(knn, k_features=1)
sbs.fit(X_train_std, y_train)
k_feat = [len(k) for k in sbs.subsets_]
plt.plot(k_feat, sbs.scores_, marker='o')
plt.ylim([0.7, 1.1])
plt.ylabel('准确率')
plt.xlabel('特征数')
plt.grid()
plt.show()

print('=========最优的5维度特征信息==========')
k5 = list(sbs.subsets_[8])
print(dfWine.columns[1:][k5])
knn.fit(X_train_std, y_train)
print('训练集的准确率:', knn.score(X_train_std, y_train))
print('验证集的朱雀率:', knn.score(X_test_std, y_test))
print('=========只使用这5个维度特征信息=======')
knn.fit(X_train_std[:, k5], y_train)
print('训练集的准确率:', knn.score(X_train_std[:, k5], y_train))
print('验证集的朱雀率:', knn.score(X_test_std[:, k5], y_test))

'''
使用不到一半的原始特征，虽然在训练集上分类准确率下降了，但是在测试集上的表现
却提高了，此时训练集和测试集准确率相差不多了，降低了过拟合
特征选择算法，包括基于特征参数的递归后向消除法，基于树方法，单变量统计检验
'''
