# -*-coding:utf-8-*-
"""
Created on Tue Aug 21 17:17:19 2018
空战游戏
author: PM.liugang
"""
import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()#初始化背景设置
    ai_settings = Settings()    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#创建指定大小的游戏窗口
    ship = Ship(screen)
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230,230,230)#设置背景色
    '''开始游戏的主循环'''
    while True:#绘制一个空屏幕，擦去旧屏幕
        '''game_function完成大部分工作，而不是run_game'''
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)
        '''监视鼠标和键盘时间'''
        for event in pygame.event.get():#pygame检测到的事件
            if event.type == pygame.QUIT:#点击窗口的关闭按钮
                pygame.quit()
                sys.exit()#利用sys的退出
        '''让最近绘制的屏幕可见'''
        screen.fill(ai_settings.bg_color)#每次循环时都重绘屏幕颜色
        ship.blitme()#将飞机绘制到屏幕上，确保它出现在背景前面
        pygame.display.flip()#更新屏幕
        
run_game()
    
	