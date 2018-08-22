# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:41:49 2018
重构 
@author:pm.liugang
"""
import sys
import pygame

def check_events(ship):
    '''响应按键和鼠标时间'''
    for event in pygame.event.get():#pygame检测到的事件
        if event.type == pygame.QUIT:#点击窗口的关闭按钮
            pygame.quit()
            sys.exit()#利用sys的退出
        elif event.type == pygame.KEYDOWN:#按下键
            if event.key == pygame.K_RIGHT:
                '''不直接移动飞船，只是改变moving right的状态'''
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                
        elif event.type == pygame.KEYUP:#松开键
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
def update_screen(ai_settings,screen,ship):
    '''
    更新屏幕上的图像，并切换到新屏幕
    每次循环时都重绘屏幕
    '''
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    '''让最近绘制的屏幕可见'''
    pygame.display.flip()

