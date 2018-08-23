# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 21:10:55 2018

@author: 刘刚
"""

import numpy as np
import os
from sklearn.linear_model import BayesianRidge,LinearRegression,ElasticNet
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score
from sklearn.metrics import explained_variance_score,mean_absolute_error,mean_squared_error,r2_score
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('D:\\python\\python_数据分析与数据化运营\\chapter4')
raw_data = np.loadtxt('regression.txt')
x = raw_data[:,:-1]
y = raw_data[:,-1]

n_folds = 6
model_br = BayesianRidge()
model_lr = LinearRegression()
model_etc = ElasticNet()
model_svr = SVR()
model_gbr = GradientBoostingRegressor()
model_names = ['BayesianRidge','LinearRegression','ElasticNet','SVR','GradientBoostingRegressor']
model_dic = [model_br,model_lr,model_etc,model_svr,model_gbr]

cv_score_list = []
pre_y_list = []
for model in model_dic:
    scores = cross_val_score(model,x,y,cv=n_folds)
    cv_score_list.append(scores)
    pre_y_list.append(model.fit(x,y).predict(x))
    
n_samples,n_features = x.shape
model_metrics_name = [explained_variance_score,mean_absolute_error,mean_squared_error,r2_score]
model_metrics_list = []
for i in range(5):
    tmp_list = []
    for m in model_metrics_name:
        tmp_score = m(y,pre_y_list[i])
        tmp_list.append(tmp_score)
    model_metrics_list.append(tmp_list)
    
df1 = pd.DataFrame(cv_score_list,index=model_names)
df2 = pd.DataFrame(model_metrics_list,index=model_names,columns=['ev','mae','mse','r2'])

print('sample:%d \t features:%d ' % (n_samples,n_features))
print(70*'-')
print('cross validation result:')
print(df1)
print(70*'-')
print('regression metrics')
print(df2)
print(70*'-')

plt.figure()
plt.plot(np.arange(x.shape[0]),y,color='k',label='True y')
color_list = list('rbgyc')
linestyle_list = list('-.ov*')
for i,pre_y in enumerate(pre_y_list):
    plt.plot(np.arange(x.shape[0]),pre_y_list[i],color_list[i],label=model_names[i])
plt.title('REGRESSION RESULT COMPARISON')
plt.legend(loc='upper right')
plt.ylabel('REAL AND PREDICTED VALUE')
plt.show()

print('REGRESSION PREDICT')
new_point_set = [[1.05393, 0., 8.14, 0., 0.538, 5.935, 29.3, 4.4986, 4., 307., 21., 386.85, 6.58],
                 [0.7842, 0., 8.14, 0., 0.538, 5.99, 81.7, 4.2579, 4., 307., 21., 386.75, 14.67],
                 [0.80271, 0., 8.14, 0., 0.538, 5.456, 36.6, 3.7965, 4., 307., 21., 288.99, 11.69],
                 [0.7258, 0., 8.14, 0., 0.538, 5.727, 69.5, 3.7965, 4., 307., 21., 390.95, 11.28]]
for i,new_point in enumerate(new_point_set):
    new_pre_y = model_gbr.predict(np.array(new_point).reshape(1,-1))
    print('PREDICT FOR NEW POINT %d is %.2f' %((i+1),new_pre_y))
   
    
