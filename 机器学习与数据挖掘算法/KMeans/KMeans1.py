# -*- coding: utf-8 -*-
# K均值
# review 18.12.17
'''
表示样本距离最近的聚类中心的总和，越小越好 inertias
调整后的兰德指数，越接近1越好 adjusted_rand_s
互信息，相同数据的两个标签之间的相似度的度量mutual_info_s
调整后的互信息 adjusted_mutual_info_s
同质化得分 [0,1]，越大越好,homogeneity_s
完整性得分，越大越好，[0,1] completeness_s 
同质化与完成性的的谐波平均值，[0，1]，越大越好 v_measure_s
轮廓系数，[-1,1]，越大越好 silhouette_s
群内离散比簇间离散的比值 cnlinskski_harabaz_s
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn import metrics

# 准备数据
file = 'cluster.txt'  # 没找到源数据文件
raw_data = np.loadtxt(file)
x = raw_data[:, :-1]
y_true = raw_data[:, -1]
# 构建模型
n_clusters = 3
model_kmeans = KMeans(n_clusters=3, random_state=0)
model_kmeans.fit(x)
y_pre = model_kmeans.predict(x)
# 打印模型参数
n_samples, n_features = x.shape
inertias = model_kmeans.inertia_
adjusted_rand_s = metrics.adjusted_rand_score(y_true, y_pre)
mutual_info_s = metrics.mutual_info_score(y_true, y_pre)
adjusted_mutual_info_s = metrics.adjusted_mutual_info_score(y_true, y_pre)
homogeneity_s = metrics.homogeneity_score(y_true, y_pre)
completeness_s = metrics.completeness_score(y_true, y_pre)
v_measure_s = metrics.v_measure_score(y_true, y_pre)
silhouette_s = metrics.silhouette_score(x, y_pre, metric='euclidean')
cnlinskski_harabaz_s = metrics.calinski_harabaz_score(x, y_pre)

print('n_samples is %s,\n,n_features is %s ' %
      (n_samples, n_features))
print(70 * '=')
print(inertias, '\n', 
      adjusted_rand_s, '\n', 
      adjusted_mutual_info_s, '\n', 
      homogeneity_s, '\n', 
      completeness_s, '\n', 
      v_measure_s, '\n', 
      silhouette_s, '\n', 
      cnlinskski_harabaz_s)
# 数据跟模型效果可视化
centers = model_kmeans.cluster_centers_ # centers.shape is (3,2)
colors = ['#4EACC5', '#FF9C34', '#4E9A06']
plt.figure()
for i in range(n_clusters): 
    index_sets = np.where(y_pre == i)  # return index
    cluster = x[index_sets]
    plt.scatter(cluster[:, 0], cluster[:, 1], 
                c=colors[i], 
                marker='.')
    plt.plot(centers[i][0], centers[i][1], 'o', # plt.scatter ?
             mfc=colors[i], 
             markeredgecolor='k', 
             markersize=6)
plt.show()
