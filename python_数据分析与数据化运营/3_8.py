# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:05:06 2018

@author: 刘刚
"""

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.decomposition import PCA as pca
from sklearn.linear_model import LinearRegression

import os
os.chdir('D:\\python\\python_数据分析与数据化运营\\chapter3')

data = np.loadtxt('data5.txt',delimiter='\t')
x = data[:,:-1]
y = data[:,-1]

model_ridge = Ridge(alpha=1.0)
model_ridge.fit(x,y)
print(model_ridge.coef_)
print(model_ridge.intercept_)

model_pca = pca()
data_pca = model_pca.fit_transform(x)
ratio_cumsm = np.cumsum(model_pca.explained_variance_ratio_)
print(ratio_cumsm)
rule_index = np.where(ratio_cumsm>0.8)
min_index = rule_index[0][0]
data_pca_result = data_pca[:,:min_index+1]
model_liner = LinearRegression()
model_liner.fit(data_pca_result,y)
print(model_liner.coef_)
print(model_liner.intercept_)