# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:17:19 2018
初始化控制游戏外观和飞船速度的属性
@author: PM.liugang
"""
class Settings():
    def __init__(self):
        '''初始化游戏的设置'''
        '''屏幕设置'''
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5#单位是像素        
        # 子弹的设置 速度 宽 高 颜色
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        
        
