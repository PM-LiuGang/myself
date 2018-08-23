# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:00:44 2018
描述：
作者: 刘刚
order.xlsx文件概述 sheet1位本次案例的训练集，sheet2位本次案例的预测集
文件中字段描述
age 年龄 int
total pageview 总页面的浏览量 int
edu 教育程度 1-10
edu age受教育年龄 
user level 用户等级 1-7
industry 用户行业划分 1-15
value level 用户价值度分类 1-6
act level 用户活跃度分类 1-5
sex 性别
bule money 历史订单的蓝券用券订单金额，int
red money 同上
work hours 工作时间长度 int
region 地区 分类型变量 1-4
response 标签 1 有响应 0 无响应
"""

import time
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder#将分类变量和顺序变量转换为二值化变量
'''
stratifiedkfold,cross val score前者用来将数据分为训练集和测试集，后者用来做交叉检验，这里选择的stra能够
有效的结合分类样本标签数据做数据集分割，而不是完全的随机选择和分割，这种方法在应对分类样本不均匀时尤为有效
'''
from sklearn.model_selection import StratifiedKFold,cross_val_score
#前者用来做特征选择的数量控制，后者用来确定特征选择的得分计算标准
from sklearn.feature_selection import SelectPercentile,f_classif
from sklearn.ensemble import AdaBoostClassifier#集成算法，用来做分类模型训练
from sklearn.pipeline import Pipeline#管道
from sklearn.metrics import accuracy_score#准确率评估指标，用户分类算法？只适用于分类算法？

def set_summary(df):
    '''
    查看数据集的记录数，维度数，前2条数据，描述性统计和数据类型
    :param df 数据框
    :return 无
    '''
    print('Data Overviewer')
    print('Records: {0}\tDimension{1}'.format(df.shape[0],(df.shape[1]-1)))
    print('-'*30)
    print(df.head(2))
    print('-'*30)
    print('Data DESCT')
    print('-'*30)
    print(df.describe())
    print('Data Dtype')
    print(df.dtypes)
    print('-'*60)
    
def na_summary(df):
    '''
    查看数据集的缺失数据列，行记录数
    ：param df 数据框
    ：return 无
    '''
    na_cols = df.isnull().any(axis=0)
    print('NA Cols:')
    print(na_cols)
    print('-'*30)
    print('Valid Records For Each Cols:')
    print(df.count()) # 每一列有效值（非NA）的记录数据
    print('-'*30)
    na_lines = df.isnull().any(axis=1)
    print('Total number of NA lines is: {0}'.format(na_lines.sum()))
    print('-'*30)
    
def label_summary(df):
    '''
    查看每个类的样本量分布
    :param df
    :return 无
    '''
    print('Labels sample count:')
    print(df['value_level'].groupby(df['response']).count())
    print('-' * 60)

def type_con(df):
    '''
    :param df 数据框
    :return 类型转换后的数据框
    '''
    var_list = {'edu':'int32',
                'user_level':'int32',
                'industry':'int32',
                'value_level':'int32',
                'act_level':'int32',
                'sex':'int32',
                'region':'int32'}
    for var,type in var_list.iteritems():
        df[var] = df[var].astype(type)
    print('Data Types')
    print(df.dtypes)
    print('-'*30)
    return df

def na_replace(df):
    '''
    :将数据集中的NA值使用自定义方法替换
    :param df 数据框
    :return NA值替换后的数据框
    '''
    na_rules = {'age': df['age'].mean(),
                'total_pageviews': df['total_pageviews'].mean(),
                'edu': df['edu'].median(),
                'edu_ages': df['edu_ages'].median(),
                'user_level': df['user_level'].median(),
                'industry': df['user_level'].median(),
                'act_level': df['act_level'].median(),
                'sex': df['sex'].median(),
                'red_money': df['red_money'].mean(),
                'region': df['region'].median()}# 字典：定义各个列数据转换方法
    #中位数用于字符串，均值用于数值变量，之前不是集体转成整数型变量么？
    df = df.fillna(na_rules)#支持字典填充
    print('Check NA exists')
    print(df.isnull().any().sum())#如果0位表示没有缺失值，如果不为0表示还有缺失值
    print('-'*30)
    return df 

def symbol_con(df,enc_object=None,train=True):
    '''
    将分类和顺序变量转换为二值化的标志变量
    :enc_object sklearn的标志转换对象 训练阶段默认设置为None，预测阶段使用从训练阶段获得的转换对象？
    :param train 是否为训练阶段的判断状态，训练阶段为True，预测阶段为False
    :return 标志转换后的数据框，标志转换对象
    '''
    convert_cols = ['edu','user_level','industry','value_level','act_level','sex','region']
    df_con = df[convert_cols]
    df_org = df[['age','total_pageviews','edu_ages','blue_money','red_money','work_hours']].values
    if train == True:
        enc = OneHotEncoder()
        enc.fit(df_con)
        df_con_new = enc.transform(df_con).toarray()
        new_matrix = np.hstack((df_con_new,df_org))
        return new_matrix, enc
    else:
        df_con_new = enc_object.transform(df_con).toarray()
        new_matrix = np.hstack((df_con_new,df_org))
        return new_matrix
                