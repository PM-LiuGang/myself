
#便利一个目录，看看哪个文件夹下的文件最多

import os 

def find_100m_file_Size(filepath):
	for folders,subfolders,filenames in os.walk(filepath):
		for file in filenames:
			if os.path.getsize(os.path.join(folders,file)) > 25000 * 200 * 102:
				print(os.path.join(folders,file))


if __name__ == '__main__':
	find_100m_file_Size('d:\\')



'''
获取文件的大小,结果保留两位小数，单位为MB
def get_FileSize(filePath):
　　filePath = unicode(filePath,'utf8')
　　fsize = os.path.getsize(filePath)
　　fsize = fsize/float(1024*1024)
　　return round(fsize,2)
'''