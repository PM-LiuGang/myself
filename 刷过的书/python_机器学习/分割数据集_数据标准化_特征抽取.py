# -*- coding: utf-8 -*-
"""
创建时间 Wed Jan  2 15:52:24 2019
描述:
将数据集分割为训练集和测试集
统一特征取值范围
选择有意义的特征
序列特征选择算法
作者:PM.liugang
遗留：
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

plt.rcParams['font.sans-serif'] = ['SimHei']  # 输出中文
plt.rcParams['axes.unicode_minus'] = False  # 正负轴显示

# preparation data
dfWine = pd.read_csv('wine_data.csv')  # df.shape is (178,14)
dfWine.columns = ['class label', 'alcohol', 'Malic acid', 'Ash', 
                  'Alcalinity of ash','Magnesium', 'Total phenois', 
                  'Flavanoide', 'Nonflavamoid','Proanthocyanins', 
                  'Color intensity', 'Hue', 'OD2380/OD315','Proline']
print('Class labels', np.unique(dfWine['class label']))
print('*' * 20)
# split data 
X, y = dfWine.iloc[:, 1:].values, dfWine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=0)
# MinMaxScaler
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)
# StandardScaler
## StandardScaler只使用训练集fit一次
## 保证训练集和测试集使用相同的标准进行的特征缩放
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)

# 选择有意义的特征 - 避免 高方差 高偏差
# 方法1：收集更多的训练数据

# 方法2：正则化
## 由于wine数据集是多类别数据，所以lr使用One vs Rest方法，lr intercept的三个值
## 分别属于三个模型，第一个模型是类别1 vs 类别2和3，第二个模型是 类别2 vs 类别1和3
## 第三个模型用类别3 vs 类别1和2
## 通过lr coef得到权重数组，共三行 shape=(3,13)
## 每一个类对应一行，每一行有13个参数，对应13个特征
## 0值，说明L1正则可以作为特征选择的一种手段
LogisticRegression(penalty='l1')  # L1
lr = LogisticRegression(penalty='l1', C=0.1)
lr.fit(X_train_std, y_train)
print('训练集的准确率:', lr.score(X_train_std, y_train))
print('测试集的准确率:', lr.score(X_test_std, y_test))
print('线性回归的截距', lr.intercept_)
print('线性回归的系数', (lr.coef_).round(4))
print('*' * 20)

## 正则路径可视化
fig = plt.figure()
ax = plt.subplot(111)
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black',
          'pink', 'lightgreen', 'lightblue', 'gray', 'indigo', 'orange']
weights = []
params = []

for c in np.arange(-4, 6, dtype=float): # 原文中python2，python3需要加dtype
    lr = LogisticRegression(penalty='l1', C=10**c, random_state=0)
    lr.fit(X_train_std, y_train)
    weights.append(lr.coef_[1])
    params.append(10 ** c)

weights = np.array(weights)
for column, color in zip(range(weights.shape[1]), colors):
    plt.plot(params,
             weights[:, column],
             label=dfWine.columns[column+1],
             color=color)

plt.axhline(0, color='black', linestyle='--', linewidth=3)
plt.xlim([10 ** (-5), 10 ** 5])
plt.ylabel('权重系数')
plt.xlabel('C')
plt.xscale('log')
plt.legend(loc='upper left')
ax.legend(loc='upper center',
          bbox_to_anchor=(1.38, 1.03), # 图例的位置
          ncol=1, # 图裂的列数
          fancybox=True, # 图例是否有外框
          title='Feature', # 图例是否有标题
          fontsize=12) # 图例的字体大小
plt.show()

## 从图中可以看出：如果C<0.1,正则项威力很大时，所有特征权重都为 0

# 方法3：选择一个相对简单点的模型，参数少一点的

# 方法4：降低数据的维度


