# -*- coding: utf-8 -*-
"""
创建时间 Tue Apr  9 10:59:00 2019
作者:PM.liugang
描述:
此脚本用于自动化测试
测试内容：自动执行采集任务，并打印采集仪生成文件中的数据码型
！需要提前下载好chromedriver.exe放到chrome浏览器下的application下
！放到python/Scripts下
#63个端口的xpath
#//*[@id="content"]/div/div/div[4]/div/div/div/div/table/tbody/tr[1]/td[1-32]/span/div/div
#//*[@id="content"]/div/div/div[4]/div/div/div/div/table/tbody/tr[2]/td[1-31]/span/div/div
============================================
版本说明：
V1:
初稿
V2:
添加自动显示校对结果；
添加判断开始键是否可以点击；
添加判断是否打开指定界面的判断；
默认参数全自动化
V3:
代码结构重构
V4:
修复Bug:数据模型为00型，content会随机生成0、00，导致校对错误；
添加路径是否存在的判断
V5:
支持每次结束后,可不停程序循环采集；
可以预先设置采集端口(非默认模式)；
可以预先定义端口映射勾选与否；(现在不勾选的功能没实现，注释掉)
输入数据模型采用方向键代替:(V6支持)
输入y or n 改成不区分大小写
修复Bug：继续测试时，没有重置选择端口
============================================
遗留：如果由于不明原因导致上次未结束（还是采集中的状态），请手动重置未开始可点击状态
"""

import time
import os
import sys

from selenium import webdriver

"""变量定义"""
wb = webdriver.Chrome()
# 测试仪连接状态
connectState = wb.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div[1]/div[1]/div')
# 打印采集文件的字节数限制
#byteCount = 0
# 采集文件的部分内容
#content = []
port1132 = [r'//*[@id="content"]/div/div/div[4]/div/div/div/div/table/tbody/tr[1]/td[' +
            str(i) + r']/span/div/div' for i in range(1, 33)]
port2131 = [r'//*[@id="content"]/div/div/div[4]/div/div/div/div/table/tbody/tr[2]/td[' +
            str(i) + r']/span/div/div' for i in range(1, 32)]
port = port1132 + port2131
# 默认参数
defaultPath = r"D:\lg"
defaultCollectTimes = "3"
defaultCollectSize = "30"
defaultPortSelect = port[:8]
# 端口全选
portAllSelect = wb.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[4]/div/div/div/div/table/tbody/tr[3]/td[2]/div[1]/div')
# 单个端口选择
singlePortSelect = wb.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[4]/div/div/div/div/table/tbody/tr[1]/td[1]/span/div')
# 端口映射
portMap = wb.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[4]/div/div/div/div/table/tbody/tr[3]/td[2]/div[2]/div')
# 文件大小
fileSize = wb.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div[1]/div[3]/input')
# 采集次数
collectTimes = wb.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div[1]/div[5]/input')
# 保存路径
savePath = wb.find_elements_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div[1]/div[7]/input')
# 开始按键
buttonStart = wb.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div[2]/button[1]')
# 获取端口全选的选中状态
portAllSelectValue = portAllSelect.get_attribute("class")
# 获取端口映射的选中状态
portMapValue = portMap.get_attribute("class")
# 开始按键
startKey = wb.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[1]/div[2]/button[1]')

"""函数定义"""


def findNewDir(testdir):
    """
    查找最新的生成的文件（夹）

    Parameters
    -----------
    testdir : 文件的绝对路径含文件

    Returns
    --------
    newfile : 文件的绝对路径含文件
    """
    list1 = os.listdir(testdir)
    list1.sort(key=lambda fn: os.path.getmtime(testdir + "\\" + fn))
    newfile = os.path.join(testdir, list1[-1])
#    print("生成采集文件(夹)的名称是："+list1[-1])
    return newfile


def dataModelJust(dataModel, content):
    """
    判断采集中的数据模型是否与输入的数据模型一致

    Parameters
    ----------
    dataModel : 用户输入的数据模型

    content ： 采集文件中的数据模型

    Returns
    -------
    None
    """
    if dataModel == "55" or dataModel == "↓":
        if dataModel in content:
            print("采集文件中的数据模型符合预期输入,righT,√√√")
        else:
            print("采集文件中的数据模型不符合预期输入,wrong,xxx")
    elif dataModel == "AA" or dataModel == "←":
        if dataModel in content:
            print("采集文件中的数据模型符合预期输入,righT,√√√")
        else:
            print("采集文件中的数据模型不符合预期输入,wrong,xxx")
    elif dataModel == "00" or dataModel == "↑":
        if dataModel[0] in content:
            print("采集文件中的数据模型符合预期输入,righT,√√√")
        else:
            print("采集文件中的数据模型不符合预期输入,wrong,xxx")
    elif dataModel == "FF" or dataModel == "→":
        if dataModel in content:
            print("采集文件中的数据模型符合预期输入,righT,√√√")
        else:
            print("采集文件中的数据模型不符合预期输入,wrong,xxx")
    elif dataModel == "PRBS23" or dataModel == "PP":
        print(content)


def getContent(path, threshold=200):
    """
    获取采集文件的内容，同时以十六进制格式输入到列表

    Parameters
    ----------
    path : 文件的绝对路径

    threshold ： 采集文件的前多少个字节（十六进制）

    Returns
    -------
    content : 采集文件内容(十六进制格式)
    """
    with open(path, 'rb') as f:
        byteCount = 0
        while True:
            a = f.read(1)
            byteCount += 1
            if byteCount > threshold:
                break
            content.append(("%x" % (ord(a)) + '').upper())
    return content


"""开始采集流程"""
try:
    print("打开指定采集界面....")
    wb.get("localhost:8180/testing")
    wb.minimize_window()
    print(r"√已打开采集界面'localhost:8180/testing'")
    print("检查采集测试仪与笔记本的连接状态.........")
except BaseException:
    print("打开localhost:8180/testing失败")
    print("5秒后程序退出.......")
    time.sleep(5)
    wb.close()
    sys.exit()

if connectState.text == "未连接测试仪":
    print("采集测试仪与笔记本的连接状态为'未连接测试仪'")
    print("5秒后程序退出")
    time.sleep(5)
    wb.close()
    sys.exit()
    os.exit()
else:
    print("√采集测试仪与笔记本的连接状态为'已连接'")
    print('检查"开始"按键的可点击状态....')

while True:
    if startKey.get_attribute("class") == "ui tiny compact button":
        print("开始按键处于不可点击的状态")
        print("请手动恢复至可点击状态，恢复后点击回车键继续")
    else:
        print("开始按键处于可点击状态")
        break

time.sleep(5)  # 等待测试仪状态更新出来

while True:
    content = []
    print('检查步骤已完成，开始执行采集')
    print("输入发射端的数据模型是")
    dataModel = input("00、55、AA、FF、PRBS23(PP)？")
    ft = input("""
        是否按照*默认参数*的参数进行自动化(采集)测试?
        ===================
        默认采集次数为3次
        默认采集大小为30Mb
        默认保存路径为d:\lg
        默认采集端口1-8；
        不勾选端口全选
        勾选端口映射
        ===================
        y(Y) or n(N)：""")
    if ft == "y" or ft == "Y":
        fileSize.clear()
        fileSize.send_keys(defaultCollectSize)
        collectTimes.clear()
        collectTimes.send_keys(defaultCollectTimes)
        savePath[0].clear()
        savePath[0].send_keys(defaultPath)
        if portMapValue == "ui checked checkbox components-PortusVC12-style__chk_history--1nCln":  # 已选中
            portMap.click()
            portMap.click()  # 将所有端口重置为白色未选中
            for i in defaultPortSelect:
                portSelect = wb.find_element_by_xpath(i)
                portSelect.click()
        elif portMapValue == 'ui checkbox components-PortusVC12-style__chk_history--1nCln':  # 未选中
            portMap.click()
            for i in defaultPortSelect:
                portSelect = wb.find_element_by_xpath(i)
                portSelect.click()
        try:
            buttonStart.click()
        except BaseException:
            print("开始按键不能点击，3秒后退出程序")
            time.sleep(3)
            wb.close()
            os.exit()
        print("√...........采集中.............")
        time.sleep(int(defaultCollectSize) * int(defaultCollectTimes) / 2)
        try:
            path = findNewDir(defaultPath)
            path = findNewDir(path)
            print("√随机抽取用于验证的采集文件名称是： ", path)
        except BaseException:
            print("无法找到指定文件夹，3秒后退出程序")
            time.sleep(3)
            wb.close()
            sys.exit()
        content = getContent(path, threshold=200)
        dataModelJust(dataModel, content)
    elif ft == "n" or ft == "N":
        try:
            buttonStart.click()
        except BaseException:
            print("开始按键不能点击，3秒后退出程序")
            time.sleep(3)
        print('请准确按照格式输入格式准确的参数，输入错误请ctrl+c中断')
        modifyCollectTimes = input("请输入采集次数（1-99）：")
        modifyCollectSize = input("请输入采集文件的大小（1-99）Mb：")
        modifyCollectPath = input("请输入准确的绝对路径：")
        modifyCollectSelect = input(
            r"""'-'表示连续选择，','(英文输入法)表示单个选择
        举例：
        1-8代表选择1到8端口
        1,8代表选择了1和8端口
        请输入你想采集的端口号: """)
        if portMapValue == "ui checked checkbox components-PortusVC12-style__chk_history--1nCln":  # 已选中
            portMap.click()
            portMap.click()  # 将所有端口重置为白色未选中
        elif portMapValue == 'ui checkbox components-PortusVC12-style__chk_history--1nCln':  # 未选中
            portMap.click()
        if ',' in modifyCollectSelect:
            portSelect = modifyCollectSelect.split(',')
            portSelect = [port[int(i) - 1] for i in portSelect]
            for i in portSelect:
                portSelect = wb.find_element_by_xpath(i)
                portSelect.click()
        elif '-' in modifyCollectSelect:
            portSelect = modifyCollectSelect.split('-')
            portSelectStart = int(portSelect[0]) - 1
            portSelectEnd = int(portSelect[1])
            for i in port[portSelectStart: portSelectEnd]:
                portSelect = wb.find_element_by_xpath(i)
                portSelect.click()
        fileSize.clear()
        fileSize.send_keys(modifyCollectSize)
        collectTimes.clear()
        collectTimes.send_keys(modifyCollectTimes)
        savePath[0].clear()
        savePath[0].send_keys(modifyCollectPath)
        try:
            buttonStart.click()
        except BaseException:
            print("开始按键不能点击，退出程序")
        print("√采集中.............")
        time.sleep(int(modifyCollectTimes) * int(modifyCollectSize) / 2)

        try:
            path = findNewDir(modifyCollectPath)
            path = findNewDir(path)
            print("√随机抽取用于验证的采集文件名称是： ", path)
        except BaseException:
            print("无法找到指定文件夹，3秒后退出程序")
            time.sleep(3)
            wb.close()
            sys.exit()
        content = getContent(path, threshold=200)
        dataModelJust(dataModel, content)
    continueTest = input("是否继续测试？  y(Y) or n(N)?")
    if continueTest == "y" or continueTest == "Y":
        portMap.click()
        portMap.click()  # 将所有端口重置为白色未选中
    elif continueTest == "n" or continueTest == "N":
        break
wb.close()
#conitue = input("请按回车键，退出窗口~")
sys.exit()
os.exit()
