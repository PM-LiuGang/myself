# -*- coding: utf-8 -*-
"""
描述：PCA步骤
一RBF核为例
1.计算核矩阵k，也就是计算任意两个训练样本
2.对核矩阵K进行中心化处理
3.计算特征值，取最大的K个特征值对应的特征向量 ！这里的特征向量并不是主成分轴
创建时间：%(date)s
作者: PM.LiuGang
python IDE：Spyder
Review date:
输入：
遗留：
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
from sklearn.datasets import make_moons
from sklearn.decomposition import PCA

def rbf_kernel_pca(X, gamma ,n_components):
    '''
    以RBF举例说明核PCA变形
    ====================================
    X | shape=[n_samples, n_features]
    gamma | float | RBF核的调整参数
    n_components | int | 返回的主成分参数
    '''
    # 计算欧几里得等分距离
    sq_dists = pdist(X, 'sqeuclidean')
    
    # 将成对距离转换成方形矩阵
    mat_sq_dists = squareform(sq_dists)
    
    # 计算对称核矩阵
    K = exp(-gamma * mat_sq_dists)
    
    # 核矩阵中心化
    N = K.shape[0]
    one_n = np.ones((N, N)) / N # ！np.ones(())
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)
    
    # 从K获取特征对
    eigvals, eigvecs = eigh(K)
    
    # 收集 top k 特征向量（投影样本）
    X_pc = np.column_stack(eigvecs[:,i] for i in range(1, n_components + 1))
    return X_pc

'''半月形数据分割'''
# 原始数据
X,y = make_moons(n_samples=100, random_state=123)
plt.scatter(X[y==0,0],
            X[y==0,1],
            color='red',
            marker='^',
            alpha=0.5)
plt.scatter(X[y==1,0],
            X[y==1,1],
            color='blue',
            marker='o',
            alpha=0.5)

# 用sklearn实现核PCA
scikit_pca = PCA(n_components=2)
X_spca = scikit_pca.fit_transform(X)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7,3))
ax[0].scatter(X_spca[y==0,0], 
              X_spca[y==0,1],
              color='red', 
              marker='^',
              alpha=0.5)
ax[0].scatter(X_spca[y==1,0], 
              X_spca[y==1,1],
              color='blue', 
              marker='o',
              alpha=0.5)
ax[1].scatter(X_spca[y==0,0], 
              np.zeros((50,1)) + 0.02,
              color='red', 
              marker='^',
              alpha=0.5)
ax[1].scatter(X_spca[y==1,0], 
              np.zeros((50,1)) - 0.02,
              color='blue', 
              marker='o',
              alpha=0.5)
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[1].set_ylim([-1,1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
plt.show()

# 尝试rbf_kernel_pca，对非线性数据的解决效果
from matplotlib.ticker import FormatStrFormatter
X_kpca = rbf_kernel_pca(X,gamma=15,n_components=2)
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(10,4))
ax[0].scatter(X_kpca[y==0,0],
              X_kpca[y==0,1],
              color='red',
              marker='^',
              alpha=0.5)
ax[0].scatter(X_kpca[y==1,0],
              X_kpca[y==1,1],
              color='blue',
              marker='o',
              alpha=0.5)
ax[1].scatter(X_kpca[y==0,0],
              np.zeros((50,1)) + 0.02,
              color='red',
              marker='^',
              alpha=0.5)
ax[1].scatter(X_kpca[y==1,0],
              X_kpca[y==1,1] - 0.02,
              color='blue',
              marker='o',
              alpha=0.5)
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[1].set_ylim([-1,1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
ax[0].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax[1].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
plt.show()

'''分离同心圆数据'''
from sklearn.datasets import make_circles
X, y = make_circles(n_samples=1000,random_state=123,noise=0.1,factor=0.2)
plt.scatter(X[y==0,0],X[y==0,1],
            color='red',
            marker='^',
            alpha=0.5)
plt.scatter(X[y==1,0],X[y==1,1],
            color='blue',
            marker='o',
            alpha=0.5)
plt.show()

# 标准PCA处理数据集
scikit_pca = PCA(n_components=2)
X_spca = scikit_pca.fit_transform(X)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7,3))
ax[0].scatter(X_spca[y==0,0], 
              X_spca[y==0,1],
              color='red', 
              marker='^',
              alpha=0.5)
ax[0].scatter(X_spca[y==1,0], 
              X_spca[y==1,1],
              color='blue', 
              marker='o',
              alpha=0.5)
ax[1].scatter(X_spca[y==0,0], 
              np.zeros((500,1)) + 0.02,
              color='red', 
              marker='^',
              alpha=0.5)
ax[1].scatter(X_spca[y==1,0], 
              np.zeros((500,1)) - 0.02,
              color='blue', 
              marker='o',
              alpha=0.5)
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[1].set_ylim([-1,1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
plt.show()
# RBF核PCA处理数据集
X_kpca = rbf_kernel_pca(X, gamma=15, n_components=2)
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(7,3))
ax[0].scatter(X_kpca[y==0,0],
              X_kpca[y==0,1],
              color='red',
              marker='^',
              alpha=0.5)
ax[0].scatter(X_kpca[y==1,0],
              X_kpca[y==1,1],
              color='blue',
              marker='o',
              alpha=0.5)
ax[1].scatter(X_kpca[y==0,0],
              np.zeros((500,1)) + 0.02,
              color='red',
              marker='^',
              alpha=0.5)
ax[1].scatter(X_kpca[y==1,0],
              np.zeros((500,1)) - 0.02,
              color='blue',
              marker='o',
              alpha=0.5)
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[1].set_ylim([-1,1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
ax[0].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax[1].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
plt.show()