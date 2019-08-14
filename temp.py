# -*- coding: utf-8 -*-
"""
Spyder编辑器

这是一个临时脚本文件.
"""
# -*- coding: utf-8 -*-

import time
import os
import sys
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wb = webdriver.Chrome()
wb.maximize_window()
wb.get("http:\\www.baidu.com")

baidu_text = wb.find_element_by_xpath('//*[@id="kw"]')
baidu_text.send_keys('QQ邮箱')
time.sleep(1)
baidu_text.send_keys(Keys.ENTER)

time.sleep(2)
email_link = wb.find_element_by_xpath('//*[@id="1"]/h3/a[1]')
email_link.click()

'''
if email_link.text != 'QQ邮箱':
    raise 'link is not QQmail'
elif email_link.text == 'QQ邮箱':
    email_link.click()
else:
    raise 'Unknow link'
'''
num=wb.window_handles
wb.switch_to_window(num[1])
wb.switch_to.frame('login_frame')
user = wb.find_element_by_xpath('//*[@id="u"]')
user.send_keys('317121415@qq.com')

password = wb.find_element_by_xpath('//*[@id="p"]')
password.send_keys('lg@123123')

login_button = wb.find_element_by_xpath('//*[@id="login_button"]')
login_button.click()

add_password = wb.find_element_by_xpath('//*[@id="pp"]')
add_login = wb.find_element_by_xpath('//*[@id="btlogin"]')

add_password.send_keys('5262894aaa')
add_login.click()

mh_seach = wb.find_element_by_xpath('//*[@id="subject"]')
mh_seach.send_keys('发票')
mh_seach.send_keys(Keys.ENTER)


