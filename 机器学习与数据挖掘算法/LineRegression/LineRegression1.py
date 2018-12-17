# -*- coding: utf-8 -*-
# Regressiong
# Created on Sun Jul 29 20:15:14 2018
# author: 刘刚
# review 18.12.17

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.svm import SVR  
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.metrics import explained_variance_score, 
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import r2_score
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
# 准备数据
raw_data = np.loadtxt('regression.txt')
x = raw_data[:, :-1]
y = raw_data[:, -1]

n_folds = 6
model_br = BayesianRidge()
model_lr = LinearRegression()
model_etc = ElasticNet()
model_svr = SVR()
model_gbr = GradientBoostingRegressor()
model_names = ['BR', 'LR', 'ETC', 'SVR', 'GBR']
model_dic = [model_br, model_lr, model_etc, model_svr, model_gbr]
# 交叉验证得分
cross_val_score_list = []  
pre_y_list = []
model_metrics_list = []
n_samples, n_features = x.shape

for model in model_dic:
    scores = cross_val_score(model, x, y, cv=n_folds)
    cross_val_score_list.append(scores)
    pre_y_list.append(model.fit(x, y).predict(x))
# 模型得分
model_metrics_name = [explained_variance_score, 
                      mean_absolute_error,
                      mean_squared_error, 
                      r2_score]  
for i in range(5):
    tmp_list = []
    for m in model_metrics_name:
        tmp_score = m(y, pre_y_list[i])
        tmp_list.append(tmp_score)
    model_metrics_list.append(tmp_list)

df1 = pd.DataFrame(cross_val_score_list, index=model_names)
df2 = pd.DataFrame(model_metrics_list, index=model_names,
                   columns=['ev', 'mae', 'mse', 'r2'])

print('samples:%d \t features:%d ' % (n_samples, n_features))
print('-' * 70)
print('title:cross validation result:')
print(df1)
print('-' * 70)
print('regression metrics:')
print(df2)
print('-' * 70)
print('''
      输出缩写 \t 全名标题
      ev \t explained_variance
      mae \t mean_absolute_error
      mse \t mean_squared_error
      r2 \t r2(判定系数)
      ''')
print('-' * 70)

plt.figure()
plt.plot(np.arange(x.shape[0]), y, color='k', label='y_true')
color_list = list('rbgyc')
linestyle_list = list('-.ov*')

for i, pre_y in enumerate(pre_y_list):
    plt.plot(np.arange(x.shape[0]), 
             pre_y_list[i],
             color_list[i], 
             label=model_names[i])
    
plt.title('regression result comparison')
plt.legend(loc='upper right')
plt.ylabel('real and predicted value')
plt.show()
print('-' * 70)
# 预测数据
print('regression prediction')
new_point_set = [[1.05393, 0., 8.14, 0., 0.538, 5.935, 29.3, 
                  4.4986, 4., 307., 21., 386.85, 6.58],
                 [0.7842, 0., 8.14, 0., 0.538, 5.99, 81.7,
                    4.2579, 4., 307., 21., 386.75, 14.67],
                 [0.80271, 0., 8.14, 0., 0.538, 5.456, 36.6,
                     3.7965, 4., 307., 21., 288.99, 11.69],
                 [0.7258, 0., 8.14, 0., 0.538, 5.727, 69.5, 
                  3.7965, 4., 307., 21., 390.95, 11.28]]
for i, new_point in enumerate(new_point_set):
    new_pre_y = model_gbr.predict(np.array(new_point).reshape(1, -1)) # (1,52)
    print('predict for new point %d is: %.2f' % (i+1, new_pre_y))
    
# echarts方式出图
from pyecharts import Line
line = Line()
for modelName in model_names:
    i = 0
    line.add(modelName,
             list(range(x.shape[0])),
             pre_y_list[i],
             line_type='dashed',
             line_width=i)
    i += 1
line.render('line.html')
