#coding=utf-8
#便利一个目录，看看哪个文件夹下的文件最多

import os 
max_file_size = []
filenames_namelist = []

for folders,subfolders,filenames in os.walk(os.getcwd()):
	for file in filenames:
		print(os.path.join(folders,file),os.path.getsize(os.path.join(folders,file)))
		max_file_size.append(os.path.getsize(os.path.join(folders,file)))
		filenames_namelist.append(os.path.join(folders,file))
max_size      = max(max_file_size)
max_size_name = filenames_namelist[max_file_size.index(max(max_file_size))]
print('---max---',max_size_name,'---max---',max_size)

'''
获取文件的大小,结果保留两位小数，单位为MB
def get_FileSize(filePath):
　　filePath = unicode(filePath,'utf8')
　　fsize = os.path.getsize(filePath)
　　fsize = fsize/float(1024*1024)
　　return round(fsize,2)
'''