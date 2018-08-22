# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:41:49 2018
重构 
@author:pm.liugang
"""
import sys
import pygame

def check_events():
    '''响应按键和鼠标时间'''
    for event in pygame.event.get():#pygame检测到的事件
        if event.type == pygame.QUIT:#点击窗口的关闭按钮
            pygame.quit()
            sys.exit()#利用sys的退出

def update_screen(ai_settings,screen,ship):
    '''
    更新屏幕上的图像，并切换到新屏幕
    每次循环时都重绘屏幕
    '''
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    '''让最近绘制的屏幕可见'''
    pygame.display.flip()

