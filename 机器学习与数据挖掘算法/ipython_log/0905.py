# IPython log file

from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
x = iris.data[:,[2,3]]
y = iris.target
get_ipython().run_line_magic('cd', 'main')
np.unique(y)
#[Out]# array([0, 1, 2])
get_ipython().run_line_magic('cd', '机器学习与数据挖掘算法/')
get_ipython().run_line_magic('ls', '')
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
x
...
iris
....
....
x = iris.data[:,[2,3]]
x
...
y
#[Out]# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#[Out]#        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#[Out]#        0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#[Out]#        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#[Out]#        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#[Out]#        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#[Out]#        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
type(y)
#[Out]# numpy.ndarray
type(x)
#[Out]# numpy.ndarray
x
...
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
# test_size x:y = 3:7
len(x_train)
#[Out]# 105
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(x_train)
#[Out]# StandardScaler(copy=True, with_mean=True, with_std=True)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(y_train)
x_test_std = sc.transform(y_train)
x_test_std = sc.transform(x_test))
x_test_std = sc.transform(x_test)
_
#[Out]# StandardScaler(copy=True, with_mean=True, with_std=True)
__
#[Out]# StandardScaler(copy=True, with_mean=True, with_std=True)
x_train_std
...
x_test_std
...
from sklearn.linear_model import Perceptron
ppn = Perceptron(n_iter=40,eta0=0.1,random_state=0)
# eta 学习速率 如果学习速率过大，算法可能跳过全局最优解
# 如果学习速率过小，算法需要更多次的迭代达到收敛，这将导致训练速度变慢
# random state=0 每次迭代后初始化重排训练数据集
y_pred = ppn.predict(x_test_std)
ppn.fit(x_train,y_train)
#[Out]# Perceptron(alpha=0.0001, class_weight=None, eta0=0.1, fit_intercept=True,
#[Out]#       max_iter=None, n_iter=40, n_jobs=1, penalty=None, random_state=0,
#[Out]#       shuffle=True, tol=None, verbose=0, warm_start=False)
y_pred = ppn.predict(x_test_std)
print('Misclassified samples: %d' % (y_test != y_pred).sum())
y_test.shape
#[Out]# (45,)
print('Misclassified samples: %d' % (y_test = y_pred).sum())
print('Misclassified samples: %d' % (y_test == y_pred).sum())
import pandas as pd
pd.concat(y_pred,y_test,axis=1)
pd.concat(y_pred,y_test,axis=1)
pd.concat(y_pred,y_test,axis=0)
pd.concat([y_pred,y_test],axis=0)
np.concatenate(y_pred,y_test)
np.concatenate([y_pred,y_test])
#[Out]# array([0, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
#[Out]#        1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0,
#[Out]#        1, 2, 1, 0, 2, 0, 2, 0, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 0, 0, 2,
#[Out]#        1, 0, 0, 2, 0, 0, 1, 1, 0, 2, 1, 0, 2, 2, 1, 0, 1, 1, 1, 2, 0, 2,
#[Out]#        0, 0])
np.concatenate([y_pred,y_test],axis=1)
np.concatenate([y_pred,y_test],axis=0)
#[Out]# array([0, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
#[Out]#        1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0,
#[Out]#        1, 2, 1, 0, 2, 0, 2, 0, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 0, 0, 2,
#[Out]#        1, 0, 0, 2, 0, 0, 1, 1, 0, 2, 1, 0, 2, 2, 1, 0, 1, 1, 1, 2, 0, 2,
#[Out]#        0, 0])
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
x = iris.data[:,[2:3]]
x = iris.data[:,[2,3]]
y = iris.target
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(x_train)
#[Out]# StandardScaler(copy=True, with_mean=True, with_std=True)
x_test_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)
x_test_std = sc.transform(x_train)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)
x_train_std.shape
#[Out]# (105, 2)
x_test_std.shape
#[Out]# (45, 2)
from sklearn.linear_model import Perceptron
ppn = Perceptron(n_iter=40,eta0=0.1,random_state=0)
ppn.fit(x_train_std,y_train)
#[Out]# Perceptron(alpha=0.0001, class_weight=None, eta0=0.1, fit_intercept=True,
#[Out]#       max_iter=None, n_iter=40, n_jobs=1, penalty=None, random_state=0,
#[Out]#       shuffle=True, tol=None, verbose=0, warm_start=False)
y_pred = ppn.predict(x_test_std)
print('Misclassified samples: %d' % (y_test != y_pred).sum())
# 这回对了
y_test.shape = y_pred.shape
y_test.shape == y_pred.shape
#[Out]# True
y_test.shape
#[Out]# (45,)
y_pred.shape
#[Out]# (45,)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
from sklearn.metrics import accuracy_score
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
x = iris.data[:,[2,3]]
y = iris.target
z = iris.target_names
z
#[Out]# array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(x_train)
#[Out]# StandardScaler(copy=True, with_mean=True, with_std=True)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)
from sklearn.linear_model import Perceptron
ppn = Perceptron(n_iter=40,eta0=0.1,random_state=0)
ppn.fit(x_train_std,y_train)
#[Out]# Perceptron(alpha=0.0001, class_weight=None, eta0=0.1, fit_intercept=True,
#[Out]#       max_iter=None, n_iter=40, n_jobs=1, penalty=None, random_state=0,
#[Out]#       shuffle=True, tol=None, verbose=0, warm_start=False)
y_pred = ppn.predict(x_test_std)
print('Misclassified samples: %d ' % (y_pred != y_test).sum())
from sklearn.metrics import accuracy_score
print('Accuracy : %.2f' % accuracy_score(y_test,y_pred))
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    marker = list('sxo^v')
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    x_test, y_test = X[test_idx, :], y[test_idx]

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == c1, 0], y=X[y == c1, 1],
                    alpha=0.8, c=cmap(idx), marker=marker[idx], label=c1)

    if test_idx:
        x_test, y_test = x[test_idx, :], y[test_idx]
        plt.scatter(x_test[:, 0], x_test[:, 1], c='', alpha=1.0, linewidths=1,
                    marker='o', s=55, label='test set')
                    
x_combined_std = np.vstack((x_train_std,x_test_std))
y_combined = np.hstack((y_train,y_test))
plot_decision_regions(x=x_combined_std,y=y_combined,classifier=ppn,test_idx=range(105,150))
x_train_std

plot_decision_regions(X=x_combined_std,y=y_combined,classifier=ppn,test_idx=range(105,150))
# -*- coding: utf-8 -*-
"""
创建时间 Wed Sep  5 16:01:27 2018
描述:
作者:PM.liugang
"""

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    marker = list('sxo^v')
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    x_test, y_test = X[test_idx, :], y[test_idx]

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx), marker=marker[idx], label=c1)

    if test_idx:
        x_test, y_test = x[test_idx, :], y[test_idx]
        plt.scatter(x_test[:, 0], x_test[:, 1], c='', alpha=1.0, linewidths=1,
                    marker='o', s=55, label='test set')
                    
plot_decision_regions(X=x_combined_std,y=y_combined,classifier=ppn,test_idx=range(105,150))
# -*- coding: utf-8 -*-
"""
创建时间 Wed Sep  5 16:01:27 2018
描述:
作者:PM.liugang
"""

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    marker = list('sxo^v')
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    x_test, y_test = X[test_idx, :], y[test_idx]

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx), marker=marker[idx], label=cl)

    if test_idx:
        x_test, y_test = x[test_idx, :], y[test_idx]
        plt.scatter(x_test[:, 0], x_test[:, 1], c='', alpha=1.0, linewidths=1,
                    marker='o', s=55, label='test set')
                    
plot_decision_regions(X=x_combined_std,y=y_combined,classifier=ppn,test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
#[Out]# Text(0.5,0,'petal length [standardized]')
# -*- coding: utf-8 -*-
"""
创建时间 Wed Sep  5 16:01:27 2018
描述:
作者:PM.liugang
"""

from matplotlib.colors import ListedColormap # 
import matplotlib.pyplot as plt
import numpy as np

'''
np.meshgrid的函数说明

#将两个一维数组转换成二维数组
#xnums = np.range(3) [0,1,2]
#ynums = np.range(6) [0,1,2,3,4,5] 
#d1,d2 = np.meshgrid(xnums,ynums)
	6行3列
	d1
	[0,1,2],
	[0,1,2],
	[0,1,2],
	[0,1,2],
	[0,1,2],
	[0,1,2]
	d2
	[0,0,0],
	[1,1,1],
	[2,2,2],
	...
	[5,5,5]
'''

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    marker = list('sxo^v')
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])
	#第一列的最小、最大值
	#第二列的最小、最大值
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
	#xx1.shape = 
	xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
	#np.ravle 二维降到一维
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)#z.shape = (?,2)
    z = z.reshape(xx1.shape) # z.shape = xx1.shape
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap) # 等高填充
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max()) # 坐标轴的范围
    x_test, y_test = X[test_idx, :], y[test_idx] # 划分测试集

    for idx, cl in enumerate(np.unique(y)): # 1,label-1
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx), marker=marker[idx], label=cl)
	# 遗留bug 无法高亮 不出任何数据
    if test_idx:
        x_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(x_test[:, 0], x_test[:, 1], c='', alpha=1.0, linewidths=1,marker='o', s=55, label='test set')
    
    plt.xlabel('Petal length [standardized]')
    plt.ylabel('Petal width [standardized]')
    plt.legend(loc='upper left')
    plt.show()
    
plot_decision_regions(X=x_combined_std,y=y_combined,classifier=ppn,test_idx=range(105,150))
get_ipython().run_line_magic('logstop', '')
