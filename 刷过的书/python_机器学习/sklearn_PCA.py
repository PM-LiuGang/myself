# -*- coding: utf-8 -*-
"""
描述：
创建时间：Sun Dec 30 10:05:51 2018
作者: PM.LiuGang
python IDE：Spyder
Review:
输入：
遗留：
"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.decomposition import KernelPCA

X, y = make_moons(n_samples=100, random_state=123)
scikitKpca = KernelPCA(n_components=2,kernel='rbf',gamma=15)
Xskernpca = scikitKpca.fit_transform(X)

plt.scatter(Xskernpca[y==0,0],
            Xskernpca[y==0,1],
            color='red',
            marker='^',
            alpha=0.5)
plt.scatter(Xskernpca[y==1,0],
            Xskernpca[y==1,1],
            color='blue',
            marker='o',
            alpha=0.5)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
