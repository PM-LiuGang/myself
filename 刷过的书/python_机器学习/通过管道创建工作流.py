# -*- coding: utf-8 -*-
"""
创建时间 Mon Jan 28 15:15:36 2019
作者:PM.liugang
描述:
Pipeline对象接收元素构成的列表作为输入,每个元组第一个值作为变量名，元组第二个元素是
sklearn中的transformer或Estimator,最后一步是一定是一个Estimator；StandardScaler,PCA
都是transformer；当管道pipe lr执行fit方法时，首先StandardScaler执行fit和transform方法，
然后将转换后的数据输入给PCA,PCA同样执行fit transform方法，最后将数据输入给
LogisticResgression训练一个lr模型
遗留：
"""
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import StratifiedKFold # K折交叉验证

# 准备数据集，标签转换
df = pd.read_csv('wdbc.data',header=None)

X = df.iloc[:,2:].values
y = df.iloc[:,1].values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.7)

le = LabelEncoder()
y = le.fit_transform(y)

print('总共分几类：',np.unique(y))
print('标签转换')
print('总共分几类：',np.unique(y))

# 将transformer和Estimator放入同一个管道
pipe_lr = Pipeline([('scl',StandardScaler()),
                    ('pca',PCA(n_components=2)),
                    ('clf',LogisticRegression(random_state=1))])
pipe_lr.fit(X_train,y_train)
print('测试准确率：%.3f' % pipe_lr.score(X_test,y_test))

# K折交叉验证评估模型性能
kfold = St