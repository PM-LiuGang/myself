# -*- coding: utf-8 -*-
"""
创建时间 Thu Jan  3 15:58:31 2019
作者:PM.liugang
描述:利用随机森林评估特征重要性
遗留：
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.base import clone # 克隆模型，只带参数，不带任何数据
from itertools import combinations # 创建特征子集
from sklearn.cross_validation import train_test_split # 0.20 will be removed
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

plt.rcParams['font.sans-serif'] = ['SimHei'] #输出中文
plt.rcParams['axes.unicode_minus'] = False#正负轴显示

# 准备数据
dfWine = pd.read_csv('wine_data.csv')  # df.shape is (178,14)
dfWine.columns = ['class label', 'alcohol', 'Malic acid', 'Ash', 
                  'Alcalinity of ash','Magnesium', 'Total phenois', 
                  'Flavanoide', 'Nonflavamoid','Proanthocyanins', 
                  'Color intensity', 'Hue', 'OD2380/OD315','Proline']
print('Class labels', np.unique(dfWine['class label']))
print('*' * 20)

# 分割数据
X, y = dfWine.iloc[:, 1:].values, dfWine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=0)
'''
# MinMaxScaler
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)
# StandardScaler
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)
'''
feat_labels = dfWine.columns[1:]
forest = RandomForestClassifier(n_estimators=10000,random_state=0,
                                n_jobs=-1)
forest.fit(X_train,y_train)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
for f in range(X_train.shape[1]):
    # - 左对齐 | * 定义宽度 | s 接收字符串
    print("%2d) %-*s %f" % \
         (f+1,30,feat_labels[f],importances[indices[f]]))
    
plt.title('Feature Importance')
plt.bar(range(X_train.shape[1]),
        importances[indices],
        color='lightblue',
        align='center')
plt.xticks(range(X_train.shape[1]),
           feat_labels, # 用标签做的刻度
           rotation=90,)
plt.xlim([-1,X_train.shape[1]])
plt.tight_layout()
plt.show()
'''
Alcohol是最能区分类别的特征，重要性排名前三的特征在SBS的最优5特征子集内

X_selected = forest.transform(X_train,threshold=0.15) # 没有 transform方法
X_selected.shape
