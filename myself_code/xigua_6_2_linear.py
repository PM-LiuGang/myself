# -*- coding: utf-8 -*-
"""
创建时间 Sun Sep 16 14:36:23 2018
描述:西瓜书6.2题
作者:PM.liugang
"""
# 数据集整体与分割

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.svm import SVC

data = pd.read_csv('1111.txt', index_col='编号')
dataFeature = data.iloc[:, -3:-1]
xx = np.array((data[data['好瓜'] == 1])[['密度', '含糖率']])
yy = np.array((data[data['好瓜'] == -1])[['密度', '含糖率']])
dataLabels=data.iloc[:, -1]
dataFeatureFirst=dataFeature['密度']
dataFeatureSec=dataFeature['含糖率']
# 建立线性核和高斯核的模型
svc_linear=SVC(kernel='linear', C=10000)
svc_linear.fit(dataFeature, dataLabels)
svc_linear_support_vetors=svc_linear.support_vectors_

w=svc_linear.coef_[0]
xaxis=np.linspace(0, 3, 5)  # default number = 50
a=-w[0] / w[1]  # 倾斜度
y_sep=a * xaxis - (svc_linear.intercept_[0]) / w[1]  # /w[1]

fig=plt.figure()
ax=fig.add_subplot(111)
h=0

ax.plot(xaxis, y_sep, 'k-')
ax.scatter([i[0] for i in xx],
           [i[1] for i in xx],
           s=50,
           c='r',
           label='_1')

ax.scatter([i[0] for i in yy],
           [i[1] for i in yy],
           s=50,
           label='_0',
           c='y')

ax.scatter([i[0] for i in np.array(dataFeature)],
           [i[1] for i in np.array(dataFeature)],
           s=150,
           c='',
           edgecolors='r',
           label='source')

ax.scatter([i[0] for i in svc_linear_support_vetors],
           [i[1] for i in svc_linear_support_vetors],
           s=150,
           c='',
           edgecolors='y',
           label='rbf'
           )

