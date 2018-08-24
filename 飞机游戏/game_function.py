# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:41:49 2018
一系列函数，大部分工作都是由他们完成的
@author:pm.liugang
"""
import sys
import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一颗子弹，并加入到编组bullets中
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)#添加到Group中
        
def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ai_settings,screen,ship,bullets):
    '''
    响应按键和鼠标事件
    检测相关的事件
    '''
    for event in pygame.event.get():#pygame检测到的事件
        if event.type == pygame.QUIT:#点击窗口的关闭按钮
            pygame.quit()
            sys.exit()#利用sys的退出
        elif event.type == pygame.KEYDOWN:#按下键
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:#松开键
            check_keyup_events(event,ship)
            
def update_screen(ai_settings,screen,ship,bullets):
    '''
    更新屏幕上的图像，并切换到新屏幕
    每次循环时都重绘屏幕
    '''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    '''让最近绘制的屏幕可见'''
    pygame.display.flip()

