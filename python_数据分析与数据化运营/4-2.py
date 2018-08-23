# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:15:14 2018
@author: 刘刚
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.svm import SVR#svm中的回归算法
#常用回归算法
from sklearn.linear_model import BayesianRidge,LinearRegression,ElasticNet
#集成算法
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
#导入指标算法
from sklearn.metrics import explained_variance_score,\
                            mean_absolute_error,mean_squared_error,r2_score

raw_data = np.loadtxt('regression.txt')
x = raw_data[:,:-1]
y = raw_data[:,-1]

n_folds = 6 
model_br = BayesianRidge()
model_lr = LinearRegression()
#弹性网络回归模型
model_etc = ElasticNet()
model_svr = SVR()
#梯度增强回归模型
model_gbr = GradientBoostingRegressor()

model_names = ['BR','LR','ETC','SVR','GBR']#模型名称的缩写名称列表
model_dic = [model_br,model_lr,model_etc,model_svr,model_gbr]#模型实例化名称列表

cross_val_score_list = []#交叉检查结果列表
pre_y_list = []#各个回归预测的y值列表
for model in model_dic:#读取每个回归模型对象
    #交叉模型中做训练，scores各个模型的交叉得分
    scores = cross_val_score(model,x,y,cv=n_folds)
    #cross_val_score_list每个得分数 shape [[1,2,3,4,5,6],[1,2,3,4,5,6],...]
    cross_val_score_list.append(scores)
    #pre_y_list训练模型 预测结果 pre_y_list shape [[1,2,3,4,5],[1,2,3,4,5],...]
    #每个子列表对应一个模型的预测结果
    pre_y_list.append(model.fit(x,y).predict(x))
    
n_samples,n_features = x.shape
#回归指标评估对象集，用下面四个指标评估回归模型效果
model_metrics_name = [explained_variance_score,mean_absolute_error,\
                      mean_squared_error,r2_score]#回归评估指标对象集
model_metrics_list = []#回归评估指标列表

for i in range(5):
    tmp_list = []
    for m in model_metrics_name:
        #临时得分 m(y_true,y_predict),一个模型用四种指标评估
        tmp_score = m(y,pre_y_list[i])
        tmp_list.append(tmp_score)
    #model_metrics_list's shape is [[1,2,3,4],[1,2,3,4],....]
    model_metrics_list.append(tmp_list)
#df1.shape = 5,6 交叉检验的数据框 
#df2.shape = 5,4 回归指标的数据框
df1 = pd.DataFrame(cross_val_score_list,index=model_names)
df2 = pd.DataFrame(model_metrics_list,index=model_names,columns=['ev','mae','mse','r2'])

print('samples:%d \t features:%d ' % (n_samples,n_features))
print('-' * 70)
print('title:cross validation result:')
print(df1)
print('-' * 70)
print('regression metrics:')
print(df2)
print('-' * 70)
print('''
      输出缩写 \t 全名标题
      ev \t explained_variance \t 越小越差 0-1
      mae \t mean_absolute_error \t 越小越好
      mse \t mean_squared_error \t 越小越好
      r2 \t r2(判定系数) \t 越小越差 0-1
      ''')
print('-' * 70)

plt.figure()
#np.arange(x.shape[0] 用行数当横坐标
plt.plot(np.arange(x.shape[0]),y,color='k',label='y_true')
color_list = list('rbgyc')
linestyle_list = list('-.ov*')
for i,pre_y in enumerate(pre_y_list):
    #5条折线，每条折线对应一个模型的预测结果
    plt.plot(np.arange(x.shape[0]),pre_y_list[i],color_list[i],label=model_names[i])
#图中有6条折线
plt.title('regression result comparison')
plt.legend(loc='upper right')
plt.ylabel('real and predicted value')
plt.show()

print('-' * 70)
print('regression prediction')
new_point_set = [[1.05393, 0., 8.14, 0., 0.538, 5.935, 29.3, 4.4986, 4., 307., 21., 386.85, 6.58],\
                 [0.7842, 0., 8.14, 0., 0.538, 5.99, 81.7, 4.2579, 4., 307., 21., 386.75, 14.67],\
                 [0.80271, 0., 8.14, 0., 0.538, 5.456, 36.6, 3.7965, 4., 307., 21., 288.99, 11.69],\
                 [0.7258, 0., 8.14, 0., 0.538, 5.727, 69.5, 3.7965, 4., 307., 21., 390.95, 11.28]]
for i,new_point in enumerate(new_point_set):
    new_pre_y = model_gbr.predict(np.array(new_point).reshape(1,-1))
    print('predict for new point %d is: %.2f' % (i+1,new_pre_y))
    
'''
result
----------------------------------------------------------------------
samples:506      features:13 
----------------------------------------------------------------------
title:cross validation result:
            0         1         2         3         4         5
BR   0.662422  0.677079  0.549702  0.776896 -0.139738 -0.024448
LR   0.642240  0.611521  0.514471  0.785033 -0.143673 -0.015390
ETC  0.582476  0.603773  0.365912  0.625645  0.437122  0.200454
SVR -0.000799 -0.004447 -1.224386 -0.663773 -0.122252 -1.374062
GBR  0.748756  0.810248  0.768540  0.863386  0.377387  0.549626
----------------------------------------------------------------------
regression metrics:
           ev       mae        mse        r2
BR   0.731143  3.319204  22.696772  0.731143
LR   0.740608  3.272945  21.897779  0.740608
ETC  0.686094  3.592915  26.499828  0.686094
SVR  0.173548  5.447960  71.637552  0.151410
GBR  0.975126  1.151773   2.099835  0.975126
----------------------------------------------------------------------

      输出缩写       全名标题
      ev         explained_variance
      mae        mean_absolute_error
      mse        mean_squared_error
      r2         r2(判定系数)
      
----------------------------------------------------------------------
----------------------------------------------------------------------
regression prediction
predict for new point 1 is: 21.49
predict for new point 2 is: 16.84
predict for new point 3 is: 19.50
predict for new point 4 is: 19.16
'''