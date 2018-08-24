# -*- coding: utf-8 -*-
"""
创建时间 Fri Aug 24 14:19:08 2018
描述:一个飞船发射的字段进行管理的类
作者:PM.liugang
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        '''
        pygame.Rect从空白开始创建一个矩形
        self.rect.centerx,self.rect.top移动矩形的位置
        color, speed从ai_setting中获取的
        '''
        super(Bullet,self).__init__()
        self.screen = screen 
        # 在(0,0_处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)# 小数表示子弹位置
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        '''
        向上移动子弹
        更新表示子弹位置的小数值
        更新表示子弹的rect位置
        '''
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        #在屏幕上绘制子弹
        pygame.draw.rect(self.screen,self.color,self.rect)
    
    