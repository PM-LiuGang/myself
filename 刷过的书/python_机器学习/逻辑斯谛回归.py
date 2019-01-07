# -*- coding: utf-8 -*-
"""
创建时间 Mon Jan  7 12:10:24 2019
作者:PM.liugang
描述:逻辑斯谛回归对类别概率建模，线性二分类模型，分类模型，工业街最常用的分类模型
之一，可以使用OvR技巧扩展为多分类模型；逻辑回归中激活函数变成了sigmod函数
逻辑斯谛不但能预测类别，还能输出具体的概率值，很多场景概率往往比淡出的类别值重要的多
遗留：
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import warnings

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
#from sklearn.preprocessing import MinMaxScaler

sys.path.append('C:\\Users\\Administrator\\Desktop\\myself')
warnings.filterwarnings('ignore')
# sigmod函数图形示例
def sigmod(z):
    return 1.0 / (1.0+np.exp(-z))

z = np.arange(-7,7,0.1)
phi_z = sigmod(z)
plt.plot(z,phi_z)
plt.axvline(0.0,color='k')
## 需要添加edgecolor,否则没有上下的两条线的颜色
plt.axhspan(0.0,1.0,facecolor='1.0',alpha=1,ls='dotted',edgecolor='r')
## plt.axhline(y=1,ls='dotted',color='k')
## plt.axhline(y=0,ls='dotted',color='k')
plt.axhline(y=0.5,ls='dotted',color='k')
plt.yticks([0.0,0.5,1.0])
plt.ylim(-0.1,1.1)
plt.xlabel('z')
plt.ylabel('$\phi (z)$')
plt.show()

# 逻辑斯谛模型
from sklearn.linear_model import LogisticRegression
from plotClassifierRegions import plot_decision_regions

## 准备数据
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
print('=======标签共有几类========')
print(np.unique(y))
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,
                                                  random_state=0)
## 数据标准化
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std,X_test_std))
y_combined = np.hstack((y_train,y_test))

lr = LogisticRegression(C=1000.0,random_state=0)
lr.fit(X_train_std,y_train)
plot_decision_regions(X_combined_std,y_combined,classifier=lr,
                      test_idx=range(105,150))
plt.xlabel('花瓣长度（标准化后）')
plt.ylabel('花瓣宽度（标准化后）')
plt.legend(loc='upper left')
plt.show()

lr_proba = lr.predict_proba(X_test_std[0,:].reshape(1,-1)) # 预测输出概率

for i,p in enumerate(lr_proba[0]):
    print('属于第%d类的概率是%.2f%%' % (i+1,p * 100))
    

