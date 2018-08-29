# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:57:19 2018
管理飞机位置update
在屏幕上绘制飞船的方法blitme
作者：PM.liugang
Bug：移动过程不流畅，而且不知道为什么总失灵
"""
import pygame,os
cur_pwd = os.getcwd()
dec_file = os.path.join(cur_pwd,'images','ship.bmp')

class Ship():
    def __init__(self,ai_settings,screen):
        '''初始化飞船并设置初始位置'''
        self.screen = screen
        self.ai_setting = ai_settings#让飞船能够获取其速度设置
        '''加载飞船图像并获取其外接矩形'''
        self.image = pygame.image.load(dec_file)
        self.rect = self.image.get_rect()#获取相应surface的属性rect
        self.screen_rect = screen.get_rect()
        '''将每艘飞船放在屏幕底部中央'''
        self.rect.centerx = self.screen_rect.centerx#飞船中心的x坐标
        self.rect.bottom = self.screen_rect.bottom#飞机下边缘的y坐标
        self.center = float(self.rect.centerx)
        '''移动标志'''
        self.moving_right = False
        self.moving_left = False
    def blitme(self):
        '''根据self.rect指定的位置绘制飞船在屏幕中的位置'''
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        '''
        检查moving rigth的状态，根据移动标志调整飞船的位置
        更新飞船的center的值，而不是rect
        最后更新rect对象
        self.rect.right 返回飞机外界矩形的右边缘的x坐标
        < 说明飞机未触及屏幕右边缘
        > 说明飞机未触及屏幕左边缘
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        '''不能用elif，同时按左右出现bug，右箭头始终处于优先地位'''
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        
