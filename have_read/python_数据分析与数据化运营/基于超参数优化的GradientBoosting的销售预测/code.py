# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:52:44 2018
描述：
本案例中的应用核心是通过自动优化方法，从众多指定的参数集合中通过交叉检验
等到最优模型以及参数组合
note1：案例异常值的处理，即使选择的模型对异常值不敏感
note2：虽然本案例是自动优化的实现，但是参数值也需要人工设定，但对开放性值的
      而言，仍然是一个多次尝试的过程，例如， minSamplesLeaf 浮点数和整数
作者: 刘刚
数据描述：
特征数 10 
数据记录数 731
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

'''数据总览'''
rawData = pd.read_table('products_sales.txt', delimiter=',')
print('{:*^60}'.format('Data Overview'))
print(rawData.tail(2))
print('{:*^60}'.format('Data Dtypes'))
print(rawData.dtypes)
print('{:*^60}'.format('Data DESC'))
print(rawData.describe().round(1).T)
'''
↑ 发现异常特征 
limit_infor 最大值异常 10 
price 有缺失值 2个
campaign fee 最大值33380
'''

'''查看异常列的值域分布'''
colNames = ['limit_infor', 
            'campaign_type', 
            'campaign_level', 
            'product_level']

for colName in colNames:
    unqueValue = np.sort(rawData[colName].unique())
    print('{:*^25}'.format('{1} unique values:{0}').\
          format(unqueValue,colName))
    
'''
↓异常值 prcie 有两个缺失值
'''

naCols = rawData.isnull().any(axis=0)
print('{:*^60}'.format('NA Cols'))
print(naCols)
naLines = rawData.isnull().any(axis=1)
print('Total number of NA lines is:{0}'.format(naLines.sum()))

'''相关性分析'''
print('{:*^60}'.format('Correlation Analyze'))
shortName = ['li','ct','cl','pl','ra','er','price',
             'dr','hr','cf','orders']
longName = rawData.columns
name_dict = dict(zip(longName,shortName))
print(rawData.corr().round(2).rename(index=name_dict,
      columns=name_dict))
print(name_dict)
'''ra 和 er 相关性0.98'''

'''异常值处理'''
salesData = rawData.fillna(rawData['price'].mean())
#salesData = rawData.drop('email_rate',axis=1) 排除共线性的干扰
salesData = salesData[salesData['limit_infor'].isin((0,1))]
salesData['campaign_fee'] = salesData['campaign_fee'].replace(
        33380,salesData['campaign_fee'].mean())
print('{:*^60}'.format('Transformed data:'))
print(salesData.describe().round(2).T.rename(index=name_dict))

'''准备数据集'''
X = salesData.iloc[:,:-1]
y = salesData.iloc[:,-1]

'''模型最优化参数训练及检验'''
modelGbr = GradientBoostingRegressor()
# loss 损失函数
##ls 最小二乘 
##lad 回归的鲁棒损失函数也是普通线性回归的基本方法，用于降低异常值和数据噪音带来的影响
##huber 是一个结合ls和lad的损失函数，它使用alpha来控制对异常值的敏感度
##quantile 分位数回归的损失函数
# alpha指定分数用来预测间隔
# min sample leaf 作为叶子节点的最小样本数 数字->数量，浮点数->总样本量的百分比
parameters = {'loss':['ls','lad','huber','quantile'],
              'min_samples_leaf':[1,2,3,4,5],
              'alpha':[0.1,0.3,0.6,0.9]}
modelGs = GridSearchCV(estimator=modelGbr,
                       param_grid=parameters,
                       cv=5)
modelGs.fit(X,y) # TypeError  min_samples_leaf:list(12345)
print('Best score is :',modelGs.best_score_)
print('Best parameter is :',modelGs.best_params_)

'''最佳模型训练数据集'''
modelBest = modelGs.best_estimator_
modelBest.fit(X,y)
plt.style.use('ggplot')
plt.figure()
plt.plot(np.arange(X.shape[0]),
         y,
         label='True y')
plt.plot(np.arange(X.shape[0]),
         modelBest.predict(X),
         label='Predict y')
plt.legend(loc=0)
plt.show()

'''新数据预测'''
newX = np.array([[1,1,0,1,15,0.5,177,0.66,101,798]])
print('{:*^60}'.format('Predict order: '))
print(modelBest.predict(newX).round(0))

