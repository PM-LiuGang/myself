# -*-coding:utf-8-*-
"""
Created on Tue Aug 21 17:17:19 2018
空战游戏
author: PM.liugang
创建一系列整个游戏都要用到的对象
存储在ai settings中的设置
存储在screen中的主显示surface以及一个飞船实例
包含游戏的主循环，条用check_events,ship_update,update_screen的while循环
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group

import game_function as gf

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()#初始化背景设置
    ai_settings = Settings() 
    #pygame.display.set_model Initialize a window or screen for display
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    bullets = Group()
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230,230,230)#设置背景色 RGB
    '''开始游戏的主循环'''
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)#检查键盘输入
        ship.update()#更新飞船位置
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
        for event in pygame.event.get():#pygame检测到的事件
            if event.type == pygame.QUIT:#点击窗口的关闭按钮
                pygame.quit()
                sys.exit()#利用sys的退出
        screen.fill(ai_settings.bg_color)#每次循环时都重绘屏幕颜色
        ship.blitme()#将飞机绘制到屏幕上，确保它出现在背景前面
        pygame.display.flip()#update the full display surface to the screen
        
run_game()
    
	