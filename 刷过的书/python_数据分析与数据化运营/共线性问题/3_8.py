# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:05:06 2018
@author: 刘刚
review 180925 多元一次 -> 一元一次
"""

import numpy as np
import os

from sklearn.linear_model import Ridge
from sklearn.decomposition import PCA as pca
from sklearn.linear_model import LinearRegression

'''准备数据集'''
data = np.loadtxt('data5.txt', delimiter='\t')
x = data[:, :-1]
y = data[:, -1]
print('{:*^60}'.format('Train before PCA'))
print(x.shape)

'''使用岭回归'''
model_ridge = Ridge(alpha=1.0)
model_ridge.fit(x, y)
print('{:*^60}'.format('Ridge Coef'))
print(model_ridge.coef_)
print('{:*^60}'.format('Ridge Intercept'))
print(model_ridge.intercept_)

'''使用主成分回归进行分析'''
model_pca = pca()
data_pca = model_pca.fit_transform(x)
# 得到所有主成分方差占比的累积数据
ratio_cumsum = np.cumsum(model_pca.explained_variance_ratio_)
print('{:*^60}'.format('PCA Ratio Cumsum'))
print(ratio_cumsum)

rule_index = np.where(ratio_cumsum > 0.8)  # 获取方差超过0.8的索引值
print('{:*^60}'.format('Rule Index'))
print(rule_index)
min_index = rule_index[0][0]  # 获取最小的索引值 这个例子是特例
data_pca_result = data_pca[:, :min_index + 1]  # 根据最小值索引提取主成分
print('{:*^60}'.format('Train after PCA '))
print(data_pca_result.shape)

'''建立普通线性回归模型'''
model_liner = LinearRegression()
model_liner.fit(data_pca_result, y)
print('{:*^60}'.format('LinearRegression Coef'))
print(model_liner.coef_)
print('{:*^60}'.format('LinearRegression Intercept'))
print(model_liner.intercept_)
print('转换后的方程: y = {0} * x + {1} '.format(model_liner.coef_[0],
      model_liner.intercept_))
