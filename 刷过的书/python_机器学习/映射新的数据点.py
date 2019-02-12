# -*- coding: utf-8 -*-
"""
描述：实际应用中，我们常常需要将多个数据集转换，比如，训练集和测试机，还有可能在
训练好模型后，又收集到的新数据，本文主要将不属于训练集的数据进行映射
创建时间：Sun Dec 30 08:57:31 2018
作者: PM.LiuGang
python IDE：Spyder
Review:
输入：
遗留：
"""
'''
pdist:N维空间中观测值对距离
squareform:将矢量形式的距离矢量转换为方形形式的距离,矩阵，反之亦然
exp:计算输入数组中所有元素的指数
eigh:解复的一般或广义特征值问题实对称矩阵
'''
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
from sklearn.datasets import make_moons

def rbf_kernel_pca(X, gamma ,n_components):
    '''
    以RBF举例说明核PCA变形
    ====================================
    X | shape=[n_samples, n_features]
    gamma | float | RBF核的调整参数
    n_components | int | 返回的主成分参数
    '''
    sq_dists = pdist(X, 'sqeuclidean')
    mat_sq_dists = squareform(sq_dists)
    K = exp(-gamma * mat_sq_dists)
    N = K.shape[0]
    one_n = np.ones((N, N)) / N # ！np.ones(())
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)
    eigvals, eigvecs = eigh(K)
    alphas = np.column_stack(eigvecs[:,-i] for i in range(1,n_components+1))
    lambdas = [eigvals[-i] for i in range(1, n_components+1)]
    return alphas, lambdas

X, y = make_moons(n_samples=100, random_state=123)
alphas, lambdas = rbf_kernel_pca(X, gamma=15,n_components=1)

xNew = X[25]
xProj = alphas[25]

def projectX(xNew, X, gamma, alphas, lambdas):
    pairDist = np.array([np.sum((xNew-row)**2) for row in X])
    k = np.exp(-gamma * pairDist)
    return k.dot(alphas/lambdas)

xReproj = projectX(xNew, X, gamma=15, alphas=alphas, lambdas=lambdas)
print(xReproj)

plt.scatter(alphas[y==0,0],
            np.zeros((50)),
            color='red',
            marker='^',
            alpha=0.5)
plt.scatter(alphas[y==1,0],
            np.zeros((50)),
            color='blue',
            marker='o',
            alpha=0.5)
plt.scatter(xProj,
            0,
            color='black',
            label=' X[25]',
            marker='^',
            s=100)
plt.scatter(xReproj,
            0,
            color='green',
            label='remapped point X[25]',
            marker='x',
            s=500)
plt.legend(scatterpoints=1)
plt.show()