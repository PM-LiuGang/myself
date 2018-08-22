# -*- coding = utf-8 -*-
#-----------------------------
#时间序列的一个经典应用
#分析一座桥的人流量情况
#-----------------------------
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('FremontBridge.csv',index_col='Date',parse_dates=True)
data.columns = ['West','East']
data['Total'] = data.eval('West + East')
#data_desc = data.dropna().describe()
data.plot()
plt.ylabel('Hourly Bicycle Count')
plt.show()
#plt.show() #ipython --pylab

#以每周为基础统计单位，求和
weekly = data.resample('W').sum()
weekly.plot(style=[':','--','-'])
plt.ylabel('weekly bicycle count')
plt.show()
#以每天为基础统计单位，求和
daily = data.resample('D').sum()
#滑动窗口大小30，分别求平均和值
daily.rolling(30,center=True).mean().plot(style=[':','--','-'])
plt.ylabel('mean of 30 days count')
#高斯窗口使其线更平滑
daily.rolling(50,center=True,win_type='gaussian').sum(std=10).plot(style=[':','--','-'])
plt.show()
#date.index.time datetime.time(0,12),24小时单位
by_time = data.groupby(data.index.time).mean()
#刻度标签[4h*0,4h*1,4h*2,4h*3,4h*4,4h*5,4h*6]
hourly_ticks = 4*60*60*np.arange(6)
by_time.plot(xticks=hourly_ticks,style=[':','--','-'])
plt.ylabel('每小时的自行车流量')
plt.show()
#一周每天的情况
by_weekday = data.groupby(data.index.dayofweek).mean()
by_weekday.index = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
by_weekday.plot(style=[':','--','-'])
plt.ylabel('每周每天的自行车流量')
plt.show()
#区分一周内非工作日和工作日的情况对比
week_end = np.where(data.index.weekday < 5,'weekday','weekend')
#第一级索引工作日和非工作日，二级索引24小时区分，求平均
by_time = data.groupby([week_end,data.index.time]).mean()

fig,ax = plt.subplots(1,2,figsize=(14,5))
by_time.loc['weekday'].plot(ax=ax[0],title='weekdays',xticks=hourly_ticks,style=[':','--','-'])
by_time.loc['weekend'].plot(ax=ax[1],title='weekend',xticks=hourly_ticks,style=[':','--','-'])
ax[0].set_ylabel('weekday')
ax[1].set_ylabel('weekend')
plt.show()
