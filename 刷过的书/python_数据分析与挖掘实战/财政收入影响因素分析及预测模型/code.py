# -*- coding: utf-8 -*-
"""
创建时间 Fri Oct 19 14:54:01 2018
描述:
作者:PM.liugang
"""
import numpy as np


def GM11(x0):
    '''
    param x0
    retrun 
    '''
    x0_cumsum = x0.cumsum()
    z1_mean = (x0_cumsum[:len(x0_cumsum)-1] + x0_cumsum[1:]) / 2.0
    z1_mean = z1_mean.reshape((len(z1_mean), 1))
    B = np.append(-z1_mean, np.ones_like(z1_mean), axis=1)

    Yn = x0[1:].reshape((len(x0)-1, 1))

    [[a], [b]] = np.dot(
        np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Yn)

    def f(k):
        return (x0_cumsum[0]-b/a)*np.exp(-a*(k-1))-(x0_cumsum[0]-b/a)*np.exp(-a*(k-2))
    delta = np.abs(x0-np.array([f(i) for i in range(1, len(x0)+1)]))
    C = delta.std()/x0.std()
    P = 1.0*(np.abs(delta - delta.mean()) < 0.6745 * x0.std()).sum()/len(x0)
    return f, a, b, x0[0], C, P


for i in h:
    gm = GM11(data[i][list(range(1994, 2014))].as_matrix())
    f = gm[0]
    P = gm[-1]
    C = gm[-2]
    data[i][2014] = f(len(data)-1)
    data[i][2015] = f(len(data))
    data[i] = data[i].round(2)
    if (C < 0.35 and P > 0.95):  # 评测后验差判别
        print('对于模型%s，该模型精度为---好' % i)
    elif (C < 0.5 and P > 0.8):
        print('对于模型%s，该模型精度为---合格' % i)
    elif (C < 0.65 and P > 0.7):
        print('对于模型%s，该模型精度为---勉强合格' % i)
    else:
        print('对于模型%s，该模型精度为---不合格' % i)
