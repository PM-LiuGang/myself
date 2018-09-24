# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:52:44 2018
描述：
本案例使用监督式算法中的分类算法实现的异常检测应用

note1：将原始数据集中的字符串分类转换为数值分类，便于参与建模运算
note2：通过概率投票的方法，基于三种分类器建立一个组合分类器，用于实现组合投票和分配预测
作者: 刘刚
数据描述：
特征数 3 
数据记录数 134190
特征变量的说明
遗留问题： 
…………
"""

import numpy as np
import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from warnings import filterwarnings
filterwarnings('ignore')

def set_summary(df):
    '''
    查询数据集前后2条数据，数据类型，描述性统计
    :param df 数据框
    :return 无
    '''
    print('{:*^60}'.format('Data Overview'))
    print(df.tail(2))
    print('{:*^60}'.format('Data Dtypes'))
    print(df.dtypes)
    print('{:*^60}'.format('Data DESC'))
    print(df.describe().round(2).T)


def na_summary(df):
    '''
    查询数据集的缺失数据列
    :param df 数据框
    :return 无
    '''
    naCols = df.isnull().any(axis=0)
    print('{:*^60}'.format('NA Cols'))
    print(naCols)
    naLines = df.isnull().any(axis=1)
    print('Total number of NA lines is:{0}'.format(naLines.sum()))


def label_samples_summary(df):
    '''
    查询每个类的样本量分布
    :param df 数据框
    :return 无
    '''
    print('{:*^60}'.format('Lable Samples Count: '))
    print(df.ix[:, 1].groupby(df.ix[:, -1]).count())


def str2int(set,
            convert_object,
            unique_object,
            trainning=True):
    '''
    用于将分类变量中的字符串转为数值索引
    param set 数据集
    param convert object DictVectorize转换对象 默认为空 trainning=False时 从使用训练集获得对象
    param unique object 唯一值列表 默认为空 trainning=False时 使用训练阶段得到的唯一值列表
    param trainning 是否未训练阶段
    return 训练阶段返回 model_dvtransform unique_list traing_part_data
           预测阶段返回 predict_part_data
    '''
    convert_cols = ['cat',
                    'attribution',
                    'pro_id',
                    'pro_brand',
                    'order_source',
                    'pay_type',
                    'use_id',
                    'city']  # 定义要转的列
    final_convert_matrix = set[convert_cols]  # 获得新建转换数据集
    lines = set.shape[0]  # 获取总记录数
    dict_list = []  # 总空列表 用于存放字符串与对应索引组成的字典
    if trainning == True:  # 训练阶段
        unique_list = []  # 储存每个列的唯一值列表
        for col_name in convert_cols:
            cols_unique_value = set[col_name].unique().tolist()  # 唯一值列表
            unique_list.append(cols_unique_value)
        for line_index in range(lines):
            each_record = final_convert_matrix.iloc[line_index]  # Series
            for each_index, each_data in enumerate(each_record):
                list_value = unique_list[each_index]
                each_record[each_index] = list_value.index(each_data)
            each_dict = dict(zip(convert_cols, each_record))
            dict_list.append(each_dict)
        model_dvtransform = DictVectorizer(sparse=False, dtype=np.int64)
        model_dvtransform.fit(dict_list)
        trainning_part_data = model_dvtransform.transform(dict_list)
        return model_dvtransform, unique_list, trainning_part_data
    else:
        for line_index in range(lines):
            each_record = final_convert_matrix.iloc[line_index]
            for each_index, each_data in enumerate(each_record):
                list_value = unique_object[each_index]
                each_record[each_index] = list_value.index(each_data)
            each_dict = dict(zip(convert_cols, each_record))
            dict_list.append(each_dict)
        predict_part_data = convert_object.transform(dict_list)
        return predict_part_data


def datetime2int(set):
    '''
    将日期和时间拓展出其他属性，例如星期几，周几，小时，分钟等
    param set 数据集
    return 拓展后的属性矩阵
    '''
    date_set = map(lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d'),
                   set['order_date'])
    weekday_data = map(lambda data: data.weekday(), date_set)
    daysinmonth_data = map(lambda data: data.day, date_set)
    month_data = map(lambda data: data.month, date_set)

    time_set = map(lambda times: pd.datetime.strptime(times,
                                                      '%H:%M:%S'),
                   set['order_time'])
    second_data = map(lambda data: data.second, time_set)
    minute_data = map(lambda data: data.minute, time_set)
    hour_data = map(lambda data: data.hour, time_set)

    final_set = []
    final_set.extend((weekday_data,
                      daysinmonth_data,
                      month_data,
                      second_data,
                      minute_data,
                      hour_data))
    final_matrix = np.array(final_set).T
    return final_matrix


def sample_balance(X, y):
    '''
    使用SMOTE方法对不均衡样本做过抽样处理
    param X 输入特征变量X
    param y 目标变量y
    return 均衡后的X和y
    '''
    model_smote = SMOTE()
    x_smote_resampled, y_smote_resampled = model_smote.\
        fit_sample(X, y)
    return x_smote_resampled, y_smote_resampled

'''数据应用过程'''
dtypes = {'order_id':np.object,
          'pro_id':np.object,
          'use_id':np.object}
raw_data = pd.read_table('abnormal_orders.txt',
                         delimiter=',',
                         dtype=dtypes)

'''数据审查'''
# set_summary(raw_data) 三列都是字符串
# na_summary(raw_data) cat pro_brand total_money city有缺失值
# label_samples_summary(raw_data) 标签均衡

'''数据预处理'''
drop_na_set = raw_data.dropna() # 丢弃任何包含有na值的行
X_raw = drop_na_set.ix[:,1:-1] #
y_raw = drop_na_set.ix[:,-1]
model_dvtransform,unique_object,str2int_data = str2int(X_raw,
                                                       None,
                                                       None,
                                                       trainning=True)
datetime2int_data = datetime2int(X_raw)
combine_set = np.hstack((str2int_data,
                        datetime2int_data)) # error 维数不等
constant_set = X_raw[['total_money','total_quantity']]
X_combine = np.hstack((combine_set,constant_set))
X,y = sample_balance(X_combine,y_raw)

'''组合分类模型交叉检验'''
# 常用的集成方法 RandomForest Bagging AdaBoost Gradient-Boosting
# sklearn.ensemble中还提供了extra-trees Isolation-Forest 多种集成
model_rf = RandomForestClassifier(n_estimators=20,random_state=0)
model_lf = LogisticRegression(random_state=0)
model_BagC = BaggingClassifier(n_estimators=20,random_state=0)

estimators = [('randomforest',model_rf),
              ('Logistic',model_lf),
              ('bagging',model_BagC)]
model_vot = VotingClassifier(estimators=estimators,
                             voting='soft', # soft 分类器概率做投票统计 hard 得票做多的label预测
                             weights=[0.9,1.2,1.1], # 权重 分类概率和权重做加权求和
                             n_jobs=-1) # 基于投票方法的组合分类模型器
cv = StratifiedKFold(8)
cv_score = cross_val_score(model_vot,X,y,cv=cv)
print('{:*^60}'.format('Cross Val Scores'))
print(cv_score)
print('Mean scores is: %.2f' % cv_score.mean())
model_vot.fit(X,y)

'''对新数据集做预测'''
X_raw_data = pd.read_csv('new_abnormal_order.csv',dtype=dtypes)
X_raw_new = X_raw_data.ix[:,1:]
str2int_data_new = str2int(X_raw_new,
                           model_dvtransform,
                           unique_object,
                           trainning=False)
datetime2int_data_new = datetime2int(X_raw_new)
combine_set_new = np.hstack((str2int_data_new,
                             datetime2int_data_new))
constant_set_new = X_raw_new[['total_money','total_quantity']]
X_combine_new = np.hstack((combine_set_new,constant_set_new))
y_predict = model_vot.predict(X_combine_new)
print('{:*^60}'.format('Predict Labels'))
print(y_predict)

