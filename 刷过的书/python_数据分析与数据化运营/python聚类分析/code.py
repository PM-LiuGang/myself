# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:55:46 2018
review 180926 4-1-6
@author: 刘刚
"""

import numpy as np
import  matplotlib.pyplot as plt

from sklearn.cluster import KMeans as km
from sklearn import metrics 

'''准备数据集'''
raw_data = np.loadtxt('cluster.txt')
x = raw_data[:,:-1]
y_true = raw_data[:,-1]

'''构建模型'''
n_clusters = 3
model_kmeans = km(n_clusters=n_clusters,random_state=0)
model_kmeans.fit(x)
y_pred = model_kmeans.predict(x)

'''模型指标评估'''
n_samples,n_features = x.shape
# 样本距离最近中心的总和 值越小越好 值越小证明样本在类间的分布越集中 即类内的距离越小 
inertias = model_kmeans.inertia_
# 调整后的兰德指数 [-1,1] 负数代表结果不好 越接近于1越好，意味着聚类结果与真实情况吻合
adjusted_rand_s = metrics.adjusted_rand_score(y_true,y_pred)
# 互信息 相同数据的两个标签之间的相似度的度量 结果是非负值
mutual_info_s = metrics.mutual_info_score(y_true,y_pred)
# 调整后的互信息
##更大数量的聚类群，通常MI较高，而不管实际上是否有更多的信息共享，通过聚类群的概率来纠正这种影响
##两个聚类集相同时，AMI=1，随机分区平均预期AMI约为0，也可能为为负数
adjusted_mutual_info_s = metrics.adjusted_mutual_info_score(y_true,y_pred)
# 同质化得分 如果所有的聚类都只包含属于单个类的成员的数据点，则聚类结果将满足同质性
# [0,1] 值越大意味着聚类结果与真实情况吻合
homogeneity_s = metrics.homogeneity_score(y_true,y_pred)
# 完整性得分 如果作为给定类的成员的所有数据点是相同集群的元素，则聚类结果将满足同质性
completeness_s = metrics.completeness_score(y_true,y_pred)
# 同质化与完整性之间的谐波平均值 v = 2*（完整性*均匀性）/（均匀性+完整性） 【0，1】
# 值越大意味着聚类结果与真实情况吻合
v_measure_s = metrics.v_measure_score(y_true,y_pred)
# 轮廓系数 计算所有样本的平均轮廓系数 使用平均群内距离和每个样本的平均最近簇距离来计算 
# 它是一种非监督式评估指标，0表示附近的值表示重叠的聚类，负值通常表示样本已被分配到错误的集群[-1,1]
silhouette_s = metrics.silhouette_score(x,y_pred,metric='euclidean')
# 该分数定义为群内离散和簇间离散的比值，它是一种非监督式的评估指标
calinski_harabaz_s = metrics.calinski_harabaz_score(x, y_pred)  # Calinski和Harabaz得分

print ('samples: %d \t features: %d' % (n_samples, n_features))  # 打印输出样本量和特征数量
print (70 * '-')  # 打印分隔线
print ('ine\tARI\tMI\tAMI\thomo\tcomp\tv_m\tsilh\tc&h')  # 打印输出指标标题
print ('%d %.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%d' % \
       (inertias, 
        adjusted_rand_s, 
        mutual_info_s, 
        adjusted_mutual_info_s, 
        homogeneity_s, 
        completeness_s, 
        v_measure_s,silhouette_s, 
        calinski_harabaz_s)
       )  # 打印输出指标值
print (70 * '-')  # 打印分隔线
print ('short name \t full name')  # 打印输出缩写和全名标题
print ('ine \t inertias')
print ('ARI \t adjusted_rand_s')
print ('MI \t mutual_info_s')
print ('AMI \t adjusted_mutual_info_s')
print ('homo \t homogeneity_s')
print ('comp \t completeness_s')
print ('v_m \t v_measure_s')
print ('silh \t silhouette_s')
print ('c&h \t calinski_harabaz_s')

'''可视化结果'''
centers = model_kmeans.cluster_centers_
colors = ['#4EACC5','#FF9C32','#4E9A06']
plt.figure()
for i in range(n_clusters):
    index_sets = np.where(y_pred == i) # 1 2维索引
    cluster = x[index_sets] # values
    plt.scatter(cluster[:,0],
                cluster[:,1],
                c=colors[i],
                marker='.')
    plt.plot(centers[i][0],
             centers[i][1],
             'o',
             markerfacecolor=colors[i],
             markeredgecolor='k',
             markersize=6)
plt.show()
'''预测新数据'''
new_x = np.array([1,10086]).reshape(1,-1)
cluster_label = model_kmeans.predict(new_x)
print('cluster of new data point is : %d' % cluster_label)


    
    