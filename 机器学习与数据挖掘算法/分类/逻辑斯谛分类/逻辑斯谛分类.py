# -*- coding: utf-8 -*-
"""
创建时间 Thu Sep  6 11:33:26 2018
描述:逻辑斯谛分类模型
作者:PM.liugang
逻辑斯谛回归是一个分类模型，而不是回归模型
几率比 p/1-p
logit(p) = log(p/(1-p)) 0<p<1
logit(p(y=1|x)) = W0X0 + W1X1 + W2X2 + ... + WmXm = 求和(WmXm) = W.T * x
logit函数的反函数，也就logistic函数，也简称sigmoid函数
f(z) = 1 / 1 + e**(-z)
z = W.T*X = W0X0 + W1X1 + W2X2 + ... + WmXm
正则化是解决共线性（特征间高度相关）的一个很有用的方法，它可以过滤掉数据中的噪声，
并最终防止过拟合
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import Perceptron
from matplotlib.colors import ListedColormap  
import warnings
warnings.filterwarnings('ignore')

iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,\
                                test_size=0.3,random_state=0)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

ppn = Perceptron(n_iter=40,eta0=0.1,random_state=0)
ppn.fit(X_train_std,y_train)

X_combined_std = np.vstack((X_train_std,X_test_std))
y_combined = np.hstack((y_train,y_test))

def sigmoid(z):
    return 1.0 / (1.0+np.exp(-z))

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    markers = list('sxo^v')
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),\
                           np.arange(x2_min, x2_max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    X_test, y_test = X[test_idx, :], y[test_idx]

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],\
            alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)

    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='', alpha=1.0, linewidths=1,\
                    marker='o', s=55, label='test set')

z = np.arange(-7,7,0.1)
phi_z = sigmoid(z)
plt.plot(z,phi_z)
plt.axvline(0.0,color='k') # Add a vertical line across the axes
plt.axhspan(0.0,1.0,facecolor='1.0',alpha=1.0,ls='dotted')
plt.axhline(y=0.5,ls='dotted',color='k')
plt.axhline(y=0.0,ls='dotted',color='k')
plt.axhline(y=1.0,ls='dotted',color='k')
plt.yticks([0.0,0.5,1.0]) # plt.yticks(0.0,0.5,1.0)
plt.ylim(-0.1,1.1)
plt.xlabel('z')
plt.ylabel('$\phi (z)$')
plt.show()

from sklearn.linear_model import LogisticRegression
#C Inverse of regularization strength; must be a positive float.
lr = LogisticRegression(C=1000.0,random_state=0) 
lr.fit(X_train_std,y_train)
plot_decision_regions(X_combined_std,y_combined,classifier=lr,\
                      test_idx = range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.show()

plot_decision_regions(X_combined_std,y_combined,classifier=ppn,\
                      test_idx = range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.show()
'''
print('*' * 60)
lr.predict_proba(X_test_std[0,:])
# array=[0.70793846 1.50872803] error  sum(array)= 100%
print('*' * 60)
'''
weights,params = [],[]
for h in np.arange(-5.0,5.0):
    lr = LogisticRegression(C=10**h,random_state=0)
    lr.fit(X_train_std,y_train)
    weights.append(lr.coef_[1]) # 线性回归系数
    params.append(10**h)

weights = np.array(weights)
plt.plot(params,weights[:,0],\
         label='petal length')
plt.plot(params,weights[:,1],\
         linestyle='--',label = 'petal width')

plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.legend(loc='upper left')
plt.xscale('log')
plt.show()
