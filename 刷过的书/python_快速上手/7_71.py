#coding=utf-8
#快速入门
#py130
#python3
#liugang
import re,pyperclip
#获取剪贴板的内容
text = pyperclip.paste()
#电话号码规则
phone = re.compile(r'\d{3}\.\d{3}\.\d{4}')
#获取符合正则表达式的列表
phonerex = phone.findall(text)
#将电话号码的.替换成-，写出规则
phonesub = re.compile(r'\.')

print('Copied to clipboard:')
#遍历电话号码的列表，并替换.
for i in phonerex:
	print(phonesub.sub('-',i))
#邮箱正则表示规则
mail  = re.compile(r'[a-zA-Z]+@nostarch\.com')
#遍历列表中的邮箱地址
for i in mail.findall(text):
	print(i)


