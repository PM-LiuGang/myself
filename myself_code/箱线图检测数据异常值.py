# -*- coding=utf-8 -*-
#异常值检查代码（箱线图）

import pandas as pd 
import matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

catering_sale = 'catering_sale.xls'

data = pd.read_excel(catering_sale,index_col='日期')

plt.figure()
p = data.boxplot()
plt.show()		

#书上有一段注释异常值的代码，报错执行不了
#请用下面的方法显示异常值和四分位数具体是多少
#####

import plotly.plotly#需要安装
import plotly.graph_objs as go 

data_values = data['销量'].values

data_show = [go.Box(y=data_values)]#type(y) == type(list)

plotly.offline.plot(data_show)