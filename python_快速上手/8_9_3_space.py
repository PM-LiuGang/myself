##coding=utf-8
#python
#去掉txt的空格行

def delblankline(infile, outfile):
	""" Delete blanklines of infile """
	infp = open(infile, "r")
	outfp = open(outfile, "w")
	lines = infp.readlines()
	for li in lines:
		if li.split():
			outfp.writelines(li)
	infp.close()
	outfp.close()
 
#调用示例
if __name__ == "__main__":
	delblankline("capitalsquiz33.txt","new_capitalsquiz33.txt")

