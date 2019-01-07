# -*- coding: utf-8 -*-
"""
创建时间 Mon Jan  7 14:44:51 2019
作者:PM.liugang
描述:
如果一个模型饱受过拟合困扰，我们也说此模型方差过高，造成这个结果的原因可能是模型
含有太多的参数导致模型过于复杂；同时，模型也可能遇到欠拟合问题，此模型偏差过高，要找一个
对测试集变现很好
正则化是解决特征共线性，过滤数据中嗓音和防止过拟合的有用方法，背后的原理是引入额外的
信息（偏差）来惩罚过大的权重参数，最常见的形式就是L2正则，也是也称为权重衰减，L2收缩
逻辑斯谛函数：
1 / 1 + (-np.exp(np.dot(wT*x)))
遗留：学习模型时，一定熟记的模型函数
"""
import matplotlib.pyplot as plt
import numpy as np 

from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

# 准备数据
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
print('=======标签共有几类========')
print(np.unique(y))
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,
                                                  random_state=0)
print('===========================')

# 数据标准化
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

weights,params = [],[]
for c in np.arange(-5,5,dtype=float): # 必须得加入数据类型
    lr = LogisticRegression(C=10**c,random_state=0)
    lr.fit(X_train_std,y_train)
    weights.append(lr.coef_[1]) # 取第二类 Petal？ lr.coef_.shape=(3,2)
    params.append(10**c) 

weights = np.array(weights)

plt.plot(params,weights[:,0], # 取第一个特征
         label='Petal length')
plt.plot(params,weights[:,1], # 取第二个特征
         linestyle='--',
         label='Petal Width')
plt.ylabel('Weight coefficient')
plt.xlabel('C')
plt.legend(loc='upper left')
plt.xscale('log')
plt.show()

