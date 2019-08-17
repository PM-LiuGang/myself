# -*- coding: utf-8 -*-
"""自动化脚本：浏览器打开qq邮箱，输入用户名密码，下载滴滴发票"""

"""
19.08.15->只能下载检索出的第一封邮件的内容，后续优化一次性下载检索出所有邮件的附件
"""

__auother__ = ['PM_LiuGang']


import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException

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

num = wb.window_handles
wb.switch_to_window(num[1])
wb.switch_to.frame('login_frame')  # k

try:
    time.sleep(2)
    user = wb.find_element_by_xpath('//*[@id="u"]')
    user.send_keys('317121415@qq.com')

    time.sleep(2)
    password = wb.find_element_by_xpath('//*[@id="p"]')
    password.send_keys('lg@123123')

    time.sleep(2)
    login_button = wb.find_element_by_xpath('//*[@id="login_button"]')
    login_button.click()

except ElementNotInteractableException:
    quick_login = wb.find_element_by_xpath('//*[@id="switcher_plogin"]')
    quick_login.click()

    time.sleep(2)
    user = wb.find_element_by_xpath('//*[@id="u"]')
    user.send_keys('317121415@qq.com')

    time.sleep(2)
    password = wb.find_element_by_xpath('//*[@id="p"]')
    password.send_keys('lg@123123')

    time.sleep(2)
    login_button = wb.find_element_by_xpath('//*[@id="login_button"]')
    login_button.click()

try:
    time.sleep(2)
    add_password = wb.find_element_by_xpath('//*[@id="pp"]')
    add_login = wb.find_element_by_xpath('//*[@id="btlogin"]')

    time.sleep(2)
    add_password.send_keys('5262894aaa')
    add_login.click()

    time.sleep(2)
    mh_seach = wb.find_element_by_xpath('//*[@id="subject"]')
    mh_seach.send_keys('didifapiao')
    mh_seach.send_keys(Keys.ENTER)

    time.sleep(2)
    wb.switch_to_frame('mainFrame')  # k
    mail_content = wb.find_element_by_xpath(
        '//*[@id="div_showMonday"]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/nobr/span')
    mail_content.click()

    time.sleep(2)
#    只下载第一个发票，不会下载行程单
#    mail_fujian = wb.find_element_by_xpath('//*[@id="attachment"]/div[2]/div[3]/div[2]/div/a[2]')
#    mail_fujian.click()

    mail_all_download = wb.find_element_by_xpath(
        '//*[@id="attachment"]/div[2]/div[1]/a[1]')
    mail_all_download.click()

except NoSuchElementException:
    time.sleep(2)
    mh_seach = wb.find_element_by_xpath('//*[@id="subject"]')
    mh_seach.send_keys('发票')
    mh_seach.send_keys(Keys.ENTER)

    time.sleep(2)
    wb.switch_to_frame('mainFrame')  # k
    mail_content = wb.find_element_by_xpath(
        '//*[@id="div_showMonday"]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/nobr/span')
    mail_content.click()

    time.sleep(2)
#    mail_fujian = wb.find_element_by_xpath('//*[@id="attachment"]/div[2]/div[3]/div[2]/div/a[2]')
#    mail_fujian.click()
    mail_all_download = wb.find_element_by_xpath(
        '//*[@id="attachment"]/div[2]/div[1]/a[1]')
    mail_all_download.click()

finally:
    time.sleep(10)
    wb.close()
    wb.switch_to_window(num[0])
    wb.close()
#    sys.exit()
