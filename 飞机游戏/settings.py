# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:17:19 2018
储存游戏所有设置的类
@author: PM.liugang
"""
class Settings():
    '''存储游戏中的所有设置的类'''
    def __init__(self,ai_settings,screen):
        '''初始化游戏的设置'''
        '''屏幕设置'''
        self.ai_settings = ai_settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5#单位是像素
        self.center = float(self.rect.centerx)#在飞船的属性center中存储最小数值
        
        
        
