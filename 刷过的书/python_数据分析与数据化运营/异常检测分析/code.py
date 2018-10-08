# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 00:15:58 2018
@author: 刘刚
ocsvm param:
nu:An upper bound on the fraction of training errors and\ 
a lower bound of the fraction of support vectors. (0, 1].default 0.5
dataset:必须是不包含噪音的干净数据，否则新奇点无法检测出来
"""
#ocsvm适用于高纬度的分布评估
#其他模型应采用降维或子空间聚类后，才可使用常规模型检测
#EllipticEnvelope后者只能适用于高斯分布数据集的异常检查(正态分布)
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D as a3d
from sklearn.svm import OneClassSVM as ocsvm
#from sklearn.covariance import EllipticEnvelope
#from pyecharts import Scatter3D
plt.rcParams['font.sans-serif'] = ['SimHei'] 

'''准备数据'''
raw_data = np.loadtxt('outlier.txt',delimiter=' ')
train_set = raw_data[:900,:]
test_set = raw_data[100:,:]

'''模型学习'''
model_ocsvm = ocsvm(nu=0.1,
                    kernel='rbf', # linear poly rbf sigmoid precomputed diy
                    random_state=0)
model_ocsvm.fit(train_set)
pre_test_outliers = model_ocsvm.predict(test_set)#只有1,-1两种值

'''异常结果统计'''
total_test_data = np.hstack((test_set,
                             pre_test_outliers.reshape(test_set.shape[0],1)))
normal_test_data =total_test_data[total_test_data[:,-1] == 1]
outlier_test_data =total_test_data[total_test_data[:,-1] == -1]

n_test_outliers = outlier_test_data.shape[0]
total_count_test = total_test_data.shape[0]

print('outliers:{0}/{1}'.format(n_test_outliers,total_count_test))#format的用法
print('{:*^60}'.format('All Result data (limit 5)'))#{:*^60}长度60，中间对齐，用*填充
print(total_test_data[:5])

'''异常检测结果展示'''
plt.style.use('ggplot') # print(plt.style.available)
fig = plt.figure()
ax = a3d(fig)
s1 = ax.scatter(normal_test_data[:,0],
                normal_test_data[:,1],
                normal_test_data[:,2],
                s=100,
                edgecolors='k',
                c='g',
                marker='o')

s2 = ax.scatter(outlier_test_data[:,0],
                outlier_test_data[:,1],
                outlier_test_data[:,2],
                s=100,
                edgecolors='b',
                c='r',
                marker='o')

ax.w_xaxis.set_ticklabels([]) # ax.attirute
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.legend([s1,s2],['正常点','离群点'],loc=0)
plt.title('新奇检测')
plt.show()

