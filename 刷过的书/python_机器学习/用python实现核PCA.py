# -*- coding: utf-8 -*-
"""
描述：PCA步骤
RBF核为例
1.计算核矩阵k，也就是计算任意两个训练样本
2.对核矩阵K进行中心化处理
3.计算特征值，取最大的K个特征值对应的特征向量 ！这里的特征向量并不是主成分轴
作者: PM.LiuGang
Review:190326
遗留：
实际操作的图与书中图不一致,xDiyKernelPCA分类器无效
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh  # np.linalg.eigh区别
from sklearn.datasets import make_moons
from sklearn.decomposition import PCA
from matplotlib.ticker import FormatStrFormatter

plt.rcParams['font.sans-serif'] = ['SimHei']  # 输出中文
plt.rcParams['axes.unicode_minus'] = False  # 正负轴显示


def rbf_kernel_pca(X, gamma, n_components):
    '''

    Parameters
    ----------
    X : 数据集
    gamma : k(x(j),x(u)) = exp(-γ‖X(j)-X(u)‖^2),径向基中的γ值
    n_components : 成分数

    Returns
    ------- 
    X_pc : np.array, (n_samples, n_components)
    '''
    """计算核矩阵"""
    sq_dists = pdist(X, 'sqeuclidean')  # 计算(欧几里得)平方距离 len(sq_dists)=4950
    # 将成对距离转换成方形矩阵 mat_sq_dists.shape=(100,100)
    mat_sq_dists = squareform(sq_dists)
    K = exp(-gamma * mat_sq_dists)  # rbf公式计算对称核矩阵 K.shape=(100,100)

    """将核矩阵进行中心化处理,PCA总是处理标准化后的数据"""
    N = K.shape[0]
    one_n = np.ones((N, N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + \
        one_n.dot(K).dot(one_n)  # K.shape=(100,100)

    """计算特征值,取n个top特征值对应的特征向量"""
    eigvalues, eigvecs = eigh(
        K)  # 从K获取特征对 eigvalues.shape=(1000,) eigvecs.shape=(1000,1000)
    X_pc = np.column_stack(  # 收集 top k 特征向量 np.column_stack将1维数组按列扩展成2维数组
        eigvecs[:, i] for i in range(1, n_components + 1))  # X_pc.shape=(1000,2)
    return X_pc


print("""1.半月形数据分割""")
X, y = make_moons(n_samples=100, random_state=123)
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red', marker='^', alpha=0.5)
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', marker='o', alpha=0.5)
plt.title("半月形原数据")
plt.show()

print("demo1-使用标准PCA处理半月形数据")
sklearnPCA = PCA(n_components=2)
xSklearnData = sklearnPCA.fit_transform(X)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(6, 4))
ax[0].scatter(xSklearnData[y == 0, 0], xSklearnData[y == 0, 1], color='red',
              marker='^',
              alpha=0.5)
ax[0].scatter(xSklearnData[y == 1, 0], xSklearnData[y == 1, 1], color='blue',
              marker='o',
              alpha=0.5)
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title("半月形-标准PCA")

ax[1].scatter(xSklearnData[y == 0, 0], np.zeros((50, 1)) + 0.02, color='red',  # 100个样本，每个类的数据占一半
              marker='^',
              alpha=0.5)
ax[1].scatter(xSklearnData[y == 1, 0], np.zeros((50, 1)) - 0.02, color='blue',
              marker='o',
              alpha=0.5)
ax[1].set_ylim([-1, 1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
ax[1].set_title("半月形-标准PCA(±0.02)")
plt.show()

print("""demo2-用rbf_kernel_pca处理半月形数据""")
xDiyKernelPCA = rbf_kernel_pca(X, gamma=15, n_components=2)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
ax[0].scatter(xDiyKernelPCA[y == 0, 0], xDiyKernelPCA[y == 0, 1], color='red', marker='^',
              alpha=0.5)
ax[0].scatter(xDiyKernelPCA[y == 1, 0], xDiyKernelPCA[y == 1, 1], color='blue', marker='o',
              alpha=0.5)
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax[0].set_title("半月形-rbf_kernel_pca")

ax[1].scatter(xDiyKernelPCA[y == 0, 0], np.zeros((50, 1)) + 0.02, color='red', marker='^',
              alpha=0.5)
ax[1].scatter(xDiyKernelPCA[y == 1, 0], np.zeros((50, 1)) - 0.02, color='blue', marker='o',
              alpha=0.5)
ax[1].set_ylim([-1, 1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
ax[1].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax[1].set_title("半月形-rbf_kernel_pca±0.02")
plt.show()

print("""2.分离同心圆数据""")
from sklearn.datasets import make_circles
X, y = make_circles(n_samples=1000, random_state=123, noise=0.1, factor=0.2)
fig = plt.figure()
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red', marker='^', alpha=0.5)
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', marker='o', alpha=0.5)
plt.title("同心圆数据")
plt.show()

print("""a.使用标准PCA分离同心圆数据""")
scikit_pca = PCA(n_components=2)
xSklearnData = scikit_pca.fit_transform(X)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
ax[0].scatter(xSklearnData[y == 0, 0], xSklearnData[y == 0, 1], color='red', marker='^',
              alpha=0.5)
ax[0].scatter(xSklearnData[y == 1, 0], xSklearnData[y == 1, 1], color='blue', marker='o',
              alpha=0.5)
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].set_title("同心圆-标准PCA")

ax[1].scatter(xSklearnData[y == 0, 0], np.zeros((500, 1)) + 0.02, color='red',
              marker='^',
              alpha=0.5)
ax[1].scatter(xSklearnData[y == 1, 0], np.zeros((500, 1)) - 0.02, color='blue',
              marker='o',
              alpha=0.5)
ax[1].set_ylim([-1, 1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
ax[1].set_title("同心圆-标准PCA(±0.02)")
plt.show()

print("""b.使用RBF核PCA处理同心圆数据""")
xDiyKernelPCA = rbf_kernel_pca(X, gamma=15, n_components=2)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 3))
ax[0].scatter(xDiyKernelPCA[y == 0, 0], xDiyKernelPCA[y == 0, 1], color='red', marker='^',
              alpha=0.5)
ax[0].scatter(xDiyKernelPCA[y == 1, 0], xDiyKernelPCA[y == 1, 1], color='blue', marker='o',
              alpha=0.8)
ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[0].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax[0].set_title("同心圆-rbf_kernel_pca")

ax[1].scatter(xDiyKernelPCA[y == 0, 0], np.zeros((500, 1)) + 0.02, color='red',
              marker='^',
              alpha=0.5)
ax[1].scatter(xDiyKernelPCA[y == 1, 0], np.zeros((500, 1)) - 0.02, color='blue',
              marker='o',
              alpha=0.5)
ax[1].set_ylim([-1, 1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
ax[1].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax[1].set_title("同心圆-rbf_kernel_pca(±0.02)")
plt.show()
