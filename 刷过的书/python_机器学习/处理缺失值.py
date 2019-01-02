# -*- coding: utf-8 -*-
"""
创建时间 Wed Jan  2 10:12:58 2019
描述:处理缺失值
作者:PM.liugang
遗留：
"""
import pandas as pd

from io import StringIO

csvData = '''A,B,C,d
             1.0,2.0,3.0,4.0
             5.0,6.0,,8.0
             0.0,11.0,12.0,'''
             
#csvData = unicode(csvData) # 原文中 error，python3取消了unicode
# preparation data
df = pd.read_csv(StringIO(csvData),encoding='utf-8')
# data display
print('{:*^40}'.format('df'))
print(df)
# missing values in each column
print('{:*^40}'.format('每一列中的缺失值个数'))
print(df.isnull().sum()) 
print('*' * 20)
# pandas to numpy
dfNumpy  = df.values
print(dfNumpy)
print('*' * 20)
# clean up the missing values of features or samples
print(df.dropna())
print('*' * 20)
print(df.dropna(axis=1))
print('*' * 20)
print(df.dropna(how='all'))
print('*' * 20)
print(df.dropna(thresh=4))
print('*' * 20)
print(df.dropna(subset=['C']))
print('*' * 20)
# modity the missing values
from sklearn.preprocessing import Imputer
imr = Imputer(missing_values='NaN',
              strategy='mean',
              axis=0)
imr = imr.fit(df) 
imputedData = imr.transform(dfNumpy)
print(dfNumpy)
print('*' * 20)
print(imputedData)
print('*' * 20)
# learn API of estimator in module 'sklearn'
