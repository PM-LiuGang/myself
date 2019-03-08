# -*- coding: UTF-8 -*-
"""
此脚本用于展示如何使用statsmodels搭建线性回归模型
review:190307
"""


# 保证脚本与Python3兼容

#import sys
#import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

from statsmodels.sandbox.regression.predstd import wls_prediction_std

plt.rcParams['font.sans-serif']=['SimHei']

def modelSummary(re):
    """
    分析线性回归模型的统计性质
    
    Parameters
    ----------
    re : model
        fitted linear model
    """
    print(re.summary())
    print("检验假设x的系数等于0：")
    print(re.f_test("x=0"))
#    print('{:*^80}'.format('分割线'))
    print("检测假设const的系数等于0：") # 用f test检测常量b是否显著
    print(re.f_test("const=0"))
#    print('{:*^80}'.format('分割线'))
    print("检测假设x的系数等于1和const的系数等于0同时成立：")
    print(re.f_test(["x=1", "const=0"]))
    print('{:*^80}'.format('分割线'))

def visualizeModel(re, data, features, labels, title=None):
    """
    模型参数和效果可视化
    
    Parameters
    ----------
    re : model
        fitted linear model
    data : pd.DataFrame
        datasets
    features : str or [str,str,str....]
        data features
    labels : pd.Series or np.array([])
        data labels
        
    Returns
    -------
    matplotlib.pyplot.Axes
        
    """
    prstd, preLow, preUp = wls_prediction_std(re, alpha=0.05)   
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_subplot(111)
    ax.set_title('线性回归统计分析实例%s' % title )
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    # 原数据
    ax.scatter(data[features], data[labels],
               color='r',
               label='%s: $y = x + \epsilon$' % "真实值")
    # 上界和下界
    ax.plot(data[features], preUp, "c--", label=u"%s" % "95%置信区间(上)")
    ax.plot(data[features], preLow, "m--", label=u"%s" % "95%置信区间(下)")
    # 预测值
    ax.plot(data[features], re.predict(data[features]), 
            color='y', 
            label='%s: $y = %.3fx$' % ("预测值", re.params[features]))
    legend = plt.legend(shadow=True)
    legend.get_frame().set_facecolor('#6F93AE')
    plt.show()


def trainModel(X, Y):
    """
    最小二乘法训练模型
    
    Paramters
    ---------
    X : pd.DataFrame
        training data
    Y : pd.DataFrame or pd.Series
        training data's labels
        
    Returns
    -------
    re : model
        OLS fitted model
    """
    model = sm.OLS(Y, X)
    re = model.fit()
    return re


def linearModel(data):
    """
    线性回归统计性质分析步骤展示

    参数
    ----
    data : DataFrame，建模数据
    """
    features = ["x"]
    labels = ["y"]
    Y = data[labels]
    
    print('{:*^65}'.format('添加常数项，打印模型参数'))
    X = sm.add_constant(data[features])
    re = trainModel(X, Y) # 特征维度是2维
    print(modelSummary(re))
    print('{:*^65}'.format('不添加常数项，打印模型参数'))
    resNew = trainModel(data[features], Y)
    print(resNew.summary())
    visualizeModel(resNew, data, features, labels, title="(不添加常数项)")


def readData(path):
    """
    使用pandas读取数据
    """
    data = pd.read_csv(path)
    return data


if __name__ == '__main__':
    dataPath = 'simple_example.csv'
    data = readData(dataPath)
    linearModel(data)
