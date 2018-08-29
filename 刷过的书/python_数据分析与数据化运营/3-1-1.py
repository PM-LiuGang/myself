# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 06:24:13 2018
缺失值的处理
@author: 刘刚
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

df = pd.DataFrame(np.random.randn(10,4),columns=['col1','col2','col3','col4'])
df.iloc[1:2,1] = np.nan
df.iloc[4,3] = np.nan
print(df)
print(70*'=')
nan_all = df.isnull()
print(nan_all)
print(70*'=')
nan_col1 = df.isnull().any()
nan_col2 = df.isnull().all()
print(nan_col1)
print(70*'=')
print(nan_col2)
print(70*'=')
df2 = df.dropna()
print(df2)
print(70*'=')
nan_model = Imputer(missing_values='NaN',strategy='mean',axis=0)
nan_result = nan_model.fit_transform(df)
print(nan_result)
print(70*'=')
nan_result_pd1 = df.fillna(method='backfill')
nan_result_pd2 = df.fillna(method='bfill')
nan_result_pd3 = df.fillna(method='pad')
nan_result_pd4 = df.fillna(0)
nan_result_pd5 = df.fillna({'col2':1.1,'col4':1.2})
nan_result_pd6 = df.fillna(df.mean()['col2':'col4'])
print(nan_result_pd1)
print(70*'=')
print(nan_result_pd2)
print(70*'=')
print(nan_result_pd3)
print(70*'=')
print(nan_result_pd4)
print(70*'=')
print(nan_result_pd5)
print(70*'=')
print(nan_result_pd6)
print(70*'=')

dfcopy = df.copy()

from scipy.interpolate import lagrange #导入拉格朗日插值法
'''
|description：ployinterp_column 用拉格朗日插值法进行插补
|param s:矩阵每一列
|param n：为被插值的位置
|param k：取前后的数据个数，默认5
|return：插值并返回结果
'''
def ployinterp_column(s,n,k=5):
    y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))]
    y = y[y.notnull()]
    return lagrange(y.index,list(y))(n)#不明白(n)

for i in dfcopy.columns:
    for j in range(len(dfcopy)):
        if (dfcopy[i].isnull())[j]:
            dfcopy[i][j] = ployinterp_column(dfcopy[i],j)
            
print(70 * '-')            
print(dfcopy)