#coding=utf-8
#便利一个目录，看看哪个文件夹下的文件最多

import os 
max_file_number = []
for folders,subfolders,filenames in os.walk(os.getcwd()):
	max_file_number.append(len(filenames))
	print('cur dir is:',folders,'file numbers is:',(str(len(filenames))).rjust('-',5))
print(max(max_file_number))