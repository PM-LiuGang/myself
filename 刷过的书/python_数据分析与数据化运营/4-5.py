# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 00:15:58 2018

@author: 刘刚
"""
#ocsvm适用于高纬度的分布评估
#EllipticEnvelope后者只能适用于高斯分布数据集的异常检查
from sklearn.svm import OneClassSVM as ocsvm
import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as a3d
from pyecharts import Scatter3D

raw_data = np.loadtxt('C:\\python\\python_数据分析与数据化运营\\chapter4\\outlier.txt',delimiter=' ')
train_set = raw_data[:900,:]
test_set = raw_data[900:,:]#书中有错误，测试和训练集有重叠
#默认的kernel=‘rbf’
model_ocsvm = ocsvm(nu=0.1,kernel='rbf',random_state=0)
model_ocsvm.fit(train_set)
pre_test_outliers = model_ocsvm.predict(test_set)#只有1,-1两种值
#np.hstack((np.array(a),np.array(b)))
total_test_data = np.hstack((test_set,pre_test_outliers.reshape(test_set.shape[0],1)))
normal_test_data =total_test_data[total_test_data[:,-1] == 1]
outlier_test_data =total_test_data[total_test_data[:,-1] == -1]

n_test_outliers = outlier_test_data.shape[0]#书中有错误，【1】
total_count_test = total_test_data.shape[0]

print('outliers:{0}/{1}'.format(n_test_outliers,total_count_test))#format的用法
print('{:*^60}'.format(n_test_outliers,total_count_test))#{:*^60}长度60，中间对齐，用*填充
print(total_test_data[:5])

#不采用plt作图
#pyecharts的数据[(1,2,3).(4,5,6),....]
#列表推导式转换成pyecharts能接受的格式
normal_data = [i for i in zip(normal_test_data[:,0],normal_test_data[:,1],normal_test_data[:,2])]
outlier_data = [i for i in zip(outlier_test_data[:,0],outlier_test_data[:,1],outlier_test_data[:,2])]

scatter3d = Scatter3D('NOVELTY DETECTION')
scatter3d.add('正常点',normal_data,is_visualmap=True)#is_visualmap调色柱
scatter3d.add('离群点',outlier_data,is_visualmap=True)
scatter3d.render()


