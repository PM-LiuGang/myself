# -*- coding: utf-8 -*-
"""
创建时间 Sun Sep  9 16:36:30 2018
描述:
作者:PM.liugang
问题：
很坐标不能按照%显示，纵坐标可以
不能按照降序排列，即使我的输入变量是降序的
"""

from pyecharts import Bar, Line, Grid, Pie

a_1 = ["北京移动", "新浪微博", "腾讯微博", "优酷", "爱奇艺", "奇艺网", "咪咕", "QQ音乐"]
v1 = [int(i) for i in list(range(1, 100, 13))]
v1.reverse()
# title_pos = '70%',title_top = '2%'
# 距离左侧的位置 距离顶部的位置
# is convert 交换X轴和Y轴
# xaxis_formatter 设置坐标的显示格式 数值+单位
bar_1 = Bar("网页点击率",title_pos = '70%',title_top = '2%' )
bar_1.add('', a_1, v1, is_convert=True,xaxis_formatter='%')

a_2 = ["快手", "火山", "抖音", "微视", "美拍", "头条", "美图", "默默"]
v2 = [int(i) for i in list(range(10, 90, 11))]
v2.reverse()
bar_2 = Bar("APP流量",title_pos = '20%',title_top = '2%')
bar_2.add('', a_2, v2, is_convert=True,xaxis_formatter='%')
bar_2.render()

a_3 = ["腾讯公司", "新浪公司", "搜狐公司", "网易公司", "百度公司", "阿里公司"]
v_3 = [18, 22, 31, 9, 11, 14]
pie = Pie("流量归属分布",title_pos = '70%',title_top = '50%')
# Radius 内圆和外圆半径 
# center 圆中心的位置
# rostype 玫瑰图形
pie.add("", a_3, v_3, radius=[20, 35], center=[75, 80],\
        rosetype="area",is_legend_show=False,is_label_show=True)

a_4 = ['周一', '周二', '周三', '周四', '周五', '周六', '今日']
v_4 = [5, 2, 7, 5, 10, 7, 6]
line_1 = Line("接口总流量/日",title_pos = '20%',title_top = '50%')
line_1.add("", a_4, v_4, yaxis_formatter="PB", is_smooth=True)
'''
a_5 = ['第一周', '第二周', '第三周', '第四周', '第五周', '第六周', '第七周']
v_5 = [1, 2, 3, 4, 5, 6, 7]
line_2 = Line("接口总流量/周",title_pos = '70%',title_top = '50%')
line_2.add("", a_5, v_5, yaxis_formatter="PB", is_smooth=True)
'''
# grid bottom 距离底部的距离
# grid left 距离左侧的距离
grid = Grid(height=650, width=1150)
grid.add(bar_1, grid_bottom="60%", grid_left="60%")
grid.add(bar_2, grid_bottom="60%", grid_right="60%")
grid.add(line_1, grid_top="60%", grid_right="60%")
grid.add(pie, grid_top="60%", grid_left="60%")
grid.render()
