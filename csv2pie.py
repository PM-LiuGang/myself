ha# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 06:54:16 2018
描述：
作者: 刘刚
修改：提示b'xx' isnot exist的bug
"""
from pyecharts import Pie  # pip install pyecharts
import pandas as pd # pip install pandas 
import os 

path = input('请输入文件目录（绝对路径）：') # C:\Users\Administrator\Desktop\
filename = input('请输入文件名称（带后缀名）： ') # yshd_111.csv
topN = input('请输入top几小区(整数):  ') # 

df = pd.read_csv(os.path.join(path,filename), 
                 sep='|',
                 header=None,
                 encoding='ISO-8859-15',
                 )

df[57] = df[57].fillna('unknow')
dfCount = df[57].value_counts()
del dfCount['unknow']

pie = Pie('青海移动用户访问TOP10分析',
          width=900,
          height=500,
          title_pos='center',
          )
pie.add("", dfCount[:int(topN)].index, dfCount[:int(topN)].values,  # [:10] top几
        is_label_show=True,
        legend_orient='horizontal',
        legend_pos='left',
        legend_top='bottom')
pie.render()
