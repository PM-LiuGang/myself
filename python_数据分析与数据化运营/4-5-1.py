# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:42:54 2018

@author: 刘刚
"""

from sklearn.svm import OneClassSVM
import numpy as np
import pyecharts
from pyecharts import Scatter3D
import os 

os.chdir('d:\\python\\python_数据分析与数据化运营\\chapter4')
raw_data = np.loadtxt('outlier.txt',delimiter=' ')
train_set = raw_data[:900,:]
test_set = raw_data[900:,:]

model_oneclasssvm = OneClassSVM(nu=0.1,kernel='rbf',random_state=0)
model_oneclasssvm.fit(train_set)
pre_test_outliers = model_oneclasssvm.predict(test_set)
total_test_data = np.hstack((test_set,pre_test_outliers.reshape(test_set.shape[0],1)))
normal_test_data = total_test_data[total_test_data[:,-1] == 1]
outlier_test_data = total_test_data[total_test_data[:,-1] == -1]
n_test_outliers = outlier_test_data.shape[0]
total_count_test = total_test_data.shape[0]
print('outliers:{0}/{1}'.format(n_test_outliers,total_count_test))
print('{:*^60}'.format('All Result Data'))
print(total_test_data[:5])

normal_data = [i for i in zip(normal_test_data[:,0],normal_test_data[:,1],normal_test_data[:,2])]
outlier_data = [i for i in zip(outlier_test_data[:,0],outlier_test_data[:,1],outlier_test_data[:,2])]

scatter3d = Scatter3D('NOVELTY DETECTION')
scatter3d.add('正常点',normal_data,is_visualmap=False,color='#DC143C')#
scatter3d.add('离群点',outlier_data,is_visualmap=False,color='#D8BFD8')
scatter3d.render('4-5-1.html')


