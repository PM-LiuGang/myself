# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:55:46 2018

@author: 刘刚
"""

import numpy as np
import  matplotlib.pyplot as plt
from sklearn.cluster import KMeans as km
from sklearn import metrics 
import os

os.chdir(r'D:\python\python_数据分析与数据化运营\chapter4')

raw_data = np.loadtxt('cluster.txt')
x = raw_data[:,:-1]
y_true = raw_data[:,-1]

n_clusters = 3
model_kmeans = km(n_clusters=n_clusters,random_state=0)
model_kmeans.fit(x)
y_pred = model_kmeans.predict(x)

n_samples,n_features = x.shape
inertias = model_kmeans.inertia_
adjusted_rand_s = metrics.adjusted_rand_score(y_true,y_pred)
mutual_info_s = metrics.mutual_info_score(y_true,y_pred)
adjusted_mutual_info_s = metrics.adjusted_mutual_info_score(y_true,y_pred)
homogeneity_s = metrics.homogeneity_score(y_true,y_pred)
completeness_s = metrics.completeness_score(y_true,y_pred)
v_measure_s = metrics.v_measure_score(y_true,y_pred)
silhouette_s = metrics.silhouette_score(x,y_pred,metric='euclidean')
calinski_harabaz_s = metrics.calinski_harabaz_score(x, y_pred)  # Calinski和Harabaz得分
print ('samples: %d \t features: %d' % (n_samples, n_features))  # 打印输出样本量和特征数量
print (70 * '-')  # 打印分隔线
print ('ine\tARI\tMI\tAMI\thomo\tcomp\tv_m\tsilh\tc&h')  # 打印输出指标标题
print ('%d %.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%d' % (
inertias, adjusted_rand_s, mutual_info_s, adjusted_mutual_info_s, homogeneity_s, completeness_s, v_measure_s,silhouette_s, calinski_harabaz_s))  # 打印输出指标值
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

centers = model_kmeans.cluster_centers_
colors = ['#4EACC5','#FF9C32','#4E9A06']
plt.figure()
for i in range(n_clusters):
    index_sets = np.where(y_pred == i)
    cluster = x[index_sets]
    plt.scatter(cluster[:,0],cluster[:,1],c=colors[i],marker='.')
    plt.plot(centers[i][0],centers[i][1],'o',markerfacecolor=colors[i],markeredgecolor='k',markersize=6)
plt.show()

new_x = np.array([1,10086]).reshape(1,-1)
cluster_label = model_kmeans.predict(new_x)
print('cluster of new data point is : %d' % cluster_label)


    
    