#coding=utf-8
#强密码，大写字母、小写字母和数字
#
import re

text = input('Please password: ')

def just(password):
	octlowwer = re.compile(r'[a-z]+')
	octupper = re.compile(r'[A-Z]+')
	number = re.compile(r'\d+')
	if octlowwer.findall(password) != [] and octupper.findall(password) != [] and number.findall(password) != [] and len(password) >= 8:
		print('这是一个强密码')
	else:
		print('这是一个弱密码')

just(text)

x=input()


