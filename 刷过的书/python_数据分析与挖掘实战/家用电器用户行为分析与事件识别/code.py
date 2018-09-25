# -*- coding: utf-8 -*-
"""
创建时间 Tue Sep 25 16:16:43 2018
描述:对热水用户的历史用水数据进行选择性抽取，构建专家样本 10-1
作者:PM.liugang
本例中采用的特征构建 过于繁琐 无普及学习作用
"""

import pandas as pd
import numpy as np

'''划分一次用水事件代码'''
# 准备数据集
ifile = 'water_heater.xls'
ofile = 'dividsequence.xls'
data = pd.read_excel(ifile)

# 过滤特征
data['发生时间'] = pd.to_datetime(data['发生时间'],format='%Y%m%d%H%M%S')
data = data[data['水流量'] > 0]

# 用水事件阈值寻优模型(threshold)
n = 4  # 取4个点，计算平均斜率
threshold = pd.Timedelta(minutes=5)  # 专家推荐最优阈值为5分钟

def event_num(ts):
    '''
    根据阈值判断是否为一次用水事件
    param ts 
    return 事件编号
    '''
    d = data['发生时间'].diff() > ts
    return d.sum() + 1

'''计算斜率'''
dt = [pd.Timedelta(minutes=i) for i in np.arange(1, 9, 0.25)]
h = pd.DataFrame(dt, columns=['阈值'])
h['事件数'] = h['阈值'].apply(event_num)
h['斜率'] = h['事件数'].diff()/0.25
h['斜率指标'] = (h['斜率'].abs()).rolling(window=n).mean()
ts = h['阈值'][h['斜率指标'].idxmin() - n]


if ts > threshold:
    ts = pd.Timedelta(minutes=4)

print(ts)
'''属性构造'''
# 时长指标 频率指标 用水的量化指标 用水的波动指标

