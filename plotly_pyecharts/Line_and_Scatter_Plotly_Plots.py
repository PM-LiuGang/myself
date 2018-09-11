# -*- coding: utf-8 -*-
"""
创建时间 Tue Sep 11 14:37:07 2018
描述:plotly 共Y轴 散点图 折线图
作者:PM.liugang
Plotly中绘制图像有在线和离线两种方式
因为在线绘图需要注册账号获取API key
离线绘图又有plotly.offline.plot()和plotly.offline.iplot()两种方法
前者是以离线的方式在当前工作目录下生成html格式的图像文件，并自动打开；
后者是在jupyter notebook中专用的方法，即将生成的图形嵌入到ipynb文件中
在jupyter notebook中使用plotly.offline.iplot()时，需要在之前运行plotly.offline.init_notebook_mode()以完成绘图代码的初始化，否则会报错
"""

'''
散点图与线图共X轴
'''
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
# plotly.offline.init_notebook_mode(connected=True) 离线模式 取消注释
plotly.tools.set_credentials_file(username='PM_LiuGang', api_key='PqCThIE9v9TO1e2kbpfi')
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

trace0 = go.Scatter(
    x=random_x,
    y=random_y0,
    mode='markers',
    name='markers'
)
trace1 = go.Scatter(
    x=random_x,
    y=random_y1,
    mode='lines+markers',
    name='lines+markers'
)
trace2 = go.Scatter(
    x=random_x,
    y=random_y2,
    mode='lines',
    name='lines'
)

data = [trace0,trace1,trace2]
py.iplot(data,filename='scatter-mode')

# -*- coding: utf-8 -*-

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
# plotly.offline.init_notebook_mode(connected=True)
plotly.tools.set_credentials_file(username='PM_LiuGang', api_key='PqCThIE9v9TO1e2kbpfi')
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

trace0 = go.Scatter(
    x=random_x,
    y=random_y0,
    mode='markers',
    name='markers'
)
trace1 = go.Scatter(
    x=random_x,
    y=random_y1,
    mode='lines+markers',
    name='lines+markers'
)
trace2 = go.Scatter(
    x=random_x,
    y=random_y2,
    mode='lines',
    name='lines'
)

data = [trace0,trace1,trace2]
py.iplot(data,filename='scatter-mode')


# plotly.offline.iplot(data, filename='scatter-mode') # 离线模式 取消注释

# -*- coding: utf-8 -*-
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
plotly.offline.init_notebook_mode()
# plotly.tools.set_credentials_file(username='PM_LiuGang', api_key='PqCThIE9v9TO1e2kbpfi') # 在线模式 取消注释
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

trace0 = go.Scatter(
    x=random_x,
    y=random_y0,
    mode='markers',
    name='markers'
)
trace1 = go.Scatter(
    x=random_x,
    y=random_y1,
    mode='lines+markers',
    name='lines+markers'
)
trace2 = go.Scatter(
    x=random_x,
    y=random_y2,
    mode='lines',
    name='lines'
)

data = [trace0,trace1,trace2]
#py.iplot(data,filename='scatter-mode') # 在线模式，取消注释

plotly.offline.iplot(data, filename='scatter-mode') # no use py ;use plotly

'''
箱线图的可视
'''
import plotly.plotly as py
import plotly.graph_objs as go
'''
jitter : 设置采样点中的抖动量。
如果“0”，样本点沿分布轴对齐
如果“1”，采样点以宽度等于盒的宽度的随机抖动绘制

pointpos 设置样本点相对于盒子的位置。
如果“0”，样本点位于盒子中心（ES）上。
正（负）值对应于垂直盒的右（左）位置和水平盒的上方（下）的位置

boxpoints 对所有点显示、离群点、可疑点、不显示点
enumerated : "all" | "outliers" | "suspectedoutliers" | False

outliercolor outlierwidth 
坐标轴的颜色和宽度
'''
plotly.offline.init_notebook_mode()
trace0 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='All Points',
    jitter=0.3,
    pointpos=-1.8,
    boxpoints='all',
    marker=dict(color='rgb(7,40,89)'),
    line=dict(color='rgb(7,40,89)')
)

trace1 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Only Whiskers',
    boxpoints=False,
    marker=dict(color='rgb(9,56,125)'),
    line=dict(color='rgb(9,56,125)')
)

trace2 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Suspected Outliers',
    boxpoints='suspectedoutliers',
    marker=dict(
        color='rgb(8,81,156)',
        outliercolor='rgba(219, 64, 82, 0.6)',
        line=dict(
            outliercolor='rgba(219, 64, 82, 0.6)',
            outlierwidth=2)),
    line=dict(
        color='rgb(8,81,156)')
)

trace3 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Whiskers and Outliers',
    boxpoints='outliers',
    marker=dict(
        color='rgb(107,174,214)'),
    line=dict(
        color='rgb(107,174,214)')
)
    
data = [trace0,trace1,trace2,trace3]
layout = go.Layout(
        title = 'Box Plot Styling Outlines')

fig = go.Figure(data=data,layout=layout)
# py.iplot(fig,filename = 'Box_Plot_Styling_Outliers')
plotly.offline.iplot(data, filename='Box_Plot_Styling_Outliers')

import plotly.plotly as py
import plotly.graph_objs as go

plotly.offline.init_notebook_mode()
trace0 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='All Points',# 显示所有点
    jitter=0.3,
    pointpos=-1.8,
    boxpoints='all',
    marker=dict(color='rgb(220,20,60)'),# 控制 all points的颜色
    line=dict(color='rgb(0,0,255)') # 控制 箱线图 线的颜色
)

trace1 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Only Whiskers',
    boxpoints=False, # 只显示箱线图
    marker=dict(color='rgb(9,56,125)'),
    line=dict(color='rgb(9,56,125)')
)

trace2 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Suspected Outliers',
    boxpoints='suspectedoutliers', # 显示箱线图和可疑点
    marker=dict( # 对图中的点进行设置
        color='rgb(255,0,0)',
        outliercolor='rgba(255,0,0, 0.6)', # 为什么他们算离群点，应该都算离群点，统一标识颜色
        line=dict(
            outliercolor='rgba(219, 64, 82, 0.6)',
            outlierwidth=6)), # 控制离群 点 的大小
    line=dict( # 对图中的线进行设置
        color='rgb(8,81,156)',
        width=6 # 控制箱线图 线的宽度
        )
)

trace3 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Whiskers and Outliers',
    boxpoints='outliers',
    marker=dict(
        color='rgb(255,0,0)'),
    line=dict(
        color='rgb(107,174,214)')
)
    
data = [trace0,trace1,trace2,trace3]
layout = go.Layout(
       title = 'Box Plot Styling Outlines')

fig = go.Figure(data=data,layout=layout)
# fig = go.Figure(data=data)
# py.iplot(fig,filename = 'Box_Plot_Styling_Outliers')
plotly.offline.iplot(data, filename='Box_Plot_Styling_Outliers')

import plotly.plotly as py
import plotly.graph_objs as go

plotly.offline.init_notebook_mode()
trace0 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='All Points',  # 显示所有点
    jitter=0.3,
    pointpos=-1.8,
    boxpoints='all',
    marker=dict(color='rgb(220,20,60)'),  # 控制 all points的颜色
    line=dict(color='rgb(0,0,255)')  # 控制 箱线图 线的颜色
)

trace1 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Only Whiskers',
    boxpoints=False,  # 只显示箱线图
    marker=dict(color='rgb(9,56,125)'),
    line=dict(color='rgb(9,56,125)')
)

trace2 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Suspected Outliers',
    boxpoints='suspectedoutliers',  # 显示箱线图和可疑点
    marker=dict(  # 对图中的点进行设置
        color='rgb(255,0,0)',
        outliercolor='rgba(255,0,0, 0.6)',  # 为什么他们算离群点，应该都算离群点，统一标识颜色
        line=dict(
            outliercolor='rgba(219, 64, 82, 0.6)',
            outlierwidth=6)),  # 控制离群 点 的大小
    line=dict(  # 对图中的线进行设置
        color='rgb(8,81,156)',
        width=6  # 控制箱线图 线的宽度
    )
)

trace3 = go.Box(
    y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5,
       7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10,
       10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
    name='Whiskers and Outliers',
    boxpoints='outliers',
    marker=dict(
        color='rgb(255,0,0)'),
    line=dict(
        color='rgb(107,174,214)')
)

data = [trace0, trace1, trace2, trace3]
'''
plotly中图像的图层元素与底层的背景、坐标轴等是独立开来的
定义Layout()对象，包括字体，坐标轴，图例等
'''
layout = go.Layout(
    title='Box Plot Styling Outlines',
    font={
        'size': 22,
        'family': 'sans-serif',
        'color': 'rgb(250,250,210)'})

fig = go.Figure(data=data, layout=layout)
# fig = go.Figure(data=data) # 取消注释 取消Layout 也可以执行
# py.iplot(fig,filename = 'Box_Plot_Styling_Outliers')
plotly.offline.iplot(data, filename='Box_Plot_Styling_Outliers')
