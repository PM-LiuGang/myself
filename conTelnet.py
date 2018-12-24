# -*-coding = utf-8 -*-
# liugang
# 已知bug，打印出的东西不能格式化

import telnetlib
import pprint
import sys

print('='*70)
print('''
欢迎你使用~~~
该脚本能在window系统下telnet到指定IP地址后
执行指定路径下的脚本，并打印输出
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!该脚本默认是登录不需要无密码!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	  ''')
print('='*70)

goon = input('如果继续，请按y键,其他键中止运行: ')

if goon != 'y':
	print('程序即将退出')
	sys.exit()

host = input('请输入你想telnet的IP地址：')
host = host.encode('utf-8')

username = input('请输入你的用户名：')
username = (username + '\n').encode('utf-8')

path = input('脚本的路径地址(绝对路径)： ')
path = ('cd ' + path + '\n').encode('utf-8')

fileName = input('脚本的名称(带后缀名)： ')
fileName = ('./' + fileName + '\n').encode('utf-8')

tishifu = input('请输入linux系统的提示符样式 ')
tishifu = tishifu.encode('utf-8')

tn = telnetlib.Telnet(host,timeout=20)
tn.set_debuglevel(1)

tn.read_until('login:'.encode('utf-8'))
tn.write(username)

tn.read_until(tishifu)
tn.write(path)

tn.read_until(tishifu)
tn.write(fileName)

tn.read_until(tishifu)
tn.write('exit\n'.encode('utf-8'))

pprint.pprint(tn.read_all())
