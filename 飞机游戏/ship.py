# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:57:19 2018
管理飞船的大部分行为
@author:PM.liugang
"""
import pygame

class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置初始位置'''
        self.screen = screen
        '''加载飞船图像并获取其外接矩形'''
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()#获取相应surface的属性rect
        self.screen_rect = screen.get_rect()
        '''将每艘飞船放在屏幕底部中央'''
        self.rect.centerx = self.screen_rect.centerx#飞船中心的x坐标
        self.rect.bottom = self.screen_rect.bottom#飞机下边缘的y坐标
        
    def blitme(self):
        '''根据self.rect指定的位置绘制飞船在屏幕中的位置'''
        self.screen.blit(self.image,self.rect)
        
    
