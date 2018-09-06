# -*- coding: utf-8 -*-
# K均值 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
kmodel = KMeans(n_clusters=k, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好
kmodel.fit()  # 训练模型

r1 = pd.DataFrame(kmodel.cluster_centers_, columns=[
                  typelabel[keys[i]]])  # 聚类中心
r2 = pd.Series(kmodel.labels_).value_counts()  # 分类统计
r2 = pd.DataFrame(r2, columns=[])  # 转为DataFrame，记录各个类别的数目
r = pd.concat([r1, r2], axis=1).sort_values()  # 匹配聚类中心和类别数目
r.index = [1, 2, 3, 4]
# k均值 2


file = 'cluster.txt'

raw_data = np.loadtxt(file)
y_true = raw_data[:, -1]
x = raw_data[:, :-1]

n_clusters = 3
model_kmeans = KMeans(n_clusters=3, random_state=0)
model_kmeans.fit(x)
y_pre = model_kmeans.predict(x)

n_samples, n_features = x.shape
# 表示样本距离最近的聚类中心的总和，越小越好
inertias = model_kmeans.inertia_
# 调整后的兰德指数，越接近1越好
adjusted_rand_s = metrics.adjusted_rand_score(y_true, y_pre)
# 互信息，相同数据的两个标签之间的相似度的度量
mutual_info_s = metrics.mutual_info_score(y_true, y_pre)
# 调整后的互信息，
adjusted_mutual_info_s = metrics.adjusted_mutual_info_score(y_true, y_pre)
# 同质化得分，【0,1】，越大越好
homogeneity_s = metrics.homogeneity_score(y_true, y_pre)
# 完整性得分，越大越好，【0,1】
completeness_s = metrics.completeness_score(y_true, y_pre)
# 同质化与完成性的的谐波平均值，【0，1】，越大越好
v_measure_s = metrics.v_measure_score(y_true, y_pre)
# 轮廓系数，【-1,1】，越大越好
silhouette_s = metrics.silhouette_score(x, y_pre, metric='euclidean')
# 群内离散比簇间离散的比值
cnlinskski_harabaz_s = metrics.calinski_harabaz_score(x, y_pre)
print('n_samples is %s,\n,n_features is %s ' % (n_samples, n_features))
print(70 * '=')
print(inertias, '\n', adjusted_rand_s, '\n', adjusted_mutual_info_s, '\n', adjusted_mutual_info_s, '\n',
      homogeneity_s, '\n', completeness_s, '\n', v_measure_s, '\n', silhouette_s, '\n', cnlinskski_harabaz_s)

centers = model_kmeans.cluster_centers_
'''
[out]
array([[-0.97756516, -1.01954358],
       [ 0.9583867 ,  0.99631896],
       [ 0.98703574, -0.97108137]])
'''
colors = ['#4EACC5', '#FF9C34', '#4E9A06']
plt.figure()
for i in range(n_clusters):
    index_sets = np.where(y_pre == i)  # return index->array[1,3,4,5,33...]
    cluster = x[index_sets]
    plt.scatter(cluster[:, 0], cluster[:, 1], c=colors[i], marker='.')
    # qiao用折线图画了一个点
    plt.plot(centers[i][0], centers[i][1], 'o',
             mfc=colors[i], markeredgecolor='k', markersize=6)
plt.show()
