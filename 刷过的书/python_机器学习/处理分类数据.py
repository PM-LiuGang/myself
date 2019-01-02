# -*- coding: utf-8 -*-
"""
创建时间 Wed Jan  2 15:07:14 2019
描述:处理分类数据
作者:PM.liugang
遗留：
"""
# preparation data
import pandas as pd
df = pd.DataFrame([['green', 'M', 10.1, 'class1'],
                   ['red', 'L', 13.5, 'class2'],
                   ['blue', 'XL', 15.3, 'class1']])
df.columns = ['color', 'size', 'price', 'classlabel']
# display data
print(df)
print('*' * 20)
# map ordinal feature
sizeMapping = {'XL': 3,
               'L': 2,
               'M': 1}
df['size'] = df['size'].map(sizeMapping)
print(df)
print('*' * 20)
## invSizeMapping = {v:k for k, v in sizeMapping.items()}
# code categories
import numpy as np
classMapping = {label: idx for idx, label in
                enumerate(np.unique(df['classlabel']))}
print(classMapping)
print('*' * 20)
# transform with dict  class1 -> 0 class2 -> 1
df['classlabel'] = df['classlabel'].map(classMapping)
print(df)
print('*' * 20)
invClassMapping = {v:k for k, v in classMapping.items()} # v:k k,v
df['classlabel'] = df['classlabel'].map(invClassMapping)
print(df)
print('*' * 20)
# categories transform in sklean.LabelEncoder
from sklearn.preprocessing import LabelEncoder
classLe = LabelEncoder()
y = classLe.fit_transform(df['classlabel'].values)
print(y)
print('*' * 20)
## fit_transform <-> merge(fit,transform)
classLe.inverse_transform(y)
# 用LabelEncoder处理无须的分类数据
X = df[['color','size','price']].values
colorLe = LabelEncoder()
X[:,0] = colorLe.fit_transform(X[:,0])
print(X)
print('*' * 20)
# 独热编码 one-hot-encoding
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0]) # 要进行独热编码的列
# ohe = OneHotEncoder(categorical_features[0],sparse=False)
oheFit = ohe.fit_transform(X).toarray() # 将稀疏矩阵转换为一般矩阵
print(oheFit)
print(X)
print('*' * 20)
# get_dummies 创建哑矩阵，默认会对df中所有字符串的列进行独热编码
Xdf = df[['price','color','size']]
print(pd.get_dummies(Xdf)) # 只会对字符串类型进行独热编码

