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
import warnings

warnings.filterwarnings('ignore')
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
    for var,type in var_list.items():
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

def get_best_model(x,y):
    '''
    结合交叉检验得到不同参数下的分类模型结果
    param x 输入x（特征变量）
    param y 输入y（目标变量）
    return 特征选择模型对象
    '''
    #SelectPercentile 按照指定方法选择特定数量或比例的特征变量
    #f_classif 计算数据集的方差P值
    transform = SelectPercentile(f_classif,percentile=50)
    model_adaboost = AdaBoostClassifier()
    #管道对象 语法 Pipline(steps=元组组成的列表，元组名称，模型对象)
    model_pipe = Pipeline(steps=[('ANOAV',transform),('model_adaboost',model_adaboost)])
    cv = StratifiedKFold(5)
    n_estimators = [20,50,80,100]
    score_methods = ['accuracy','f1','precision','recall','roc_auc']
    mean_list = list()
    std_list = list()
    for parameter in n_estimators:
        t1 = time.time()
        score_list = list()
        print('Set Parameters: %s' % parameter)
        for score_method in score_methods:
            '''
            步骤名称 + __ +参数对象的方法设置
            这里的步骤名称是在建立管道时定义的字符串名称
            __ 表示连接对应步骤对象的参数 后面接具体参数的名称
            model_adaboost__n_estimators=parameter的意思是：
            model_adaboost的n_estimators参数的值为parameter，parameter为从外层循环读取的值
            '''
            model_pipe.set_params(model_adaboost__n_estimators=parameter)#通过 管道 设置分类模型参数
            score_tmp = cross_val_score(model_pipe,x,y,scoring=score_method,cv=cv)
            score_list.append(score_tmp)
        score_matrix = pd.DataFrame(np.array(score_list),index=score_methods)
        score_mean = score_matrix.mean(axis=1).rename('mean')
        score_std = score_matrix.std(axis=1).rename('std')
        score_pd = pd.concat([score_matrix,score_mean,score_std],axis=1)
        mean_list.append(score_mean)
        std_list.append(score_std)
        print(score_pd.round(2))
        print('-' * 60)
        t2 = time.time()
        tt = t2 - t1
        print('time: %s' % str(tt))
    mean_matrix = np.array(mean_list).T
    std_matrix = np.array(std_list).T
    mean_pd = pd.DataFrame(mean_matrix,index=score_methods,columns=n_estimators)
    std_pd = pd.DataFrame(std_matrix,index=score_methods,columns=n_estimators)
    print('Mean values for each parameter')
    print(mean_pd)
    print('Std values for each parameter:')
    print(std_pd)
    print('-' * 60)
    return transform

#程序应用
raw_data = pd.read_excel(r'D:\python\python_数据分析与数据化运营\chapter5\order.xlsx',sheet_name=0)
x = raw_data.drop('response',axis=1)
y = raw_data['response']

set_summary(raw_data)
na_summary(raw_data)
label_summary(raw_data)

x_t1 = na_replace(x)
x_t2 = type_con(x_t1)

na_summary(x_t1)
#label_summary(x_t2) x_t2是没有response
#将分类和顺序数据转换为标志
x_new,enc = symbol_con(x_t2,enc_object=None,train=True)
transform = get_best_model(x_new,y)
transform.fit(x_new,y)
x_final = transform.transform(x_new)
final_model = AdaBoostClassifier(n_estimators=100)
final_model.fit(x_final,y)
#新数据集做预测
new_data = pd.read_excel(r'D:\python\python_数据分析与数据化运营\chapter5\order.xlsx',sheet_name=1)
final_reponse = new_data['final_response']
new_data = new_data.drop('final_response',axis=1)
set_summary(new_data)
na_summary(new_data)
new_x_t1 = na_replace(new_data)
new_x_t2 = type_con(new_x_t1)
new_x_t3 = symbol_con(new_x_t2,enc_object=enc,train=False)
new_x_final = transform.transform(new_x_t3)
#预测
predict_labels = pd.DataFrame(final_model.predict(new_x_final),columns=['lables'])
predict_labels_pro = pd.DataFrame(final_model.predict_proba(new_x_final),columns=['pro1','pro2'])
predict_pd = pd.concat((new_data,predict_labels,predict_labels_pro),axis=1)
print('Predict Info')
print(predict_pd.head(2))
print('-' * 60)
#将结果写入到excel里
writer = pd.ExcelWriter('D:\python\python_数据分析与数据化运营\chapter5\order_predict_result_myself.xlsx')
predict_pd.to_excel(writer,'Sheet1')
writer.save()

