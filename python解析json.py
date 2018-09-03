# IPython log file
get_ipython().run_line_magic('cd', 'main')
get_ipython().run_line_magic('ls', '')
#json不能储存每一种python值，它只能包含以下的值
#字符串、整型、浮点型、布尔型、列表、字典和NoneType
#json不能表示python的特有对象，例如，file对象，csv reader，writer，regex对象或 selenium webelement对象
stringOfJsonData = '{"name":"Zophie","isCat":True,"miceCaught":0,"felineIQ":null}'
import json
json_data_as_python_value = json.loads(stringOfJsonData)
stringOfJsonData = {"name":"Zophie","isCat":True,"miceCaught":0,"felineIQ":null}
stringOfJsonData = '{"name":"Zophie","isCat":True,"miceCaught":0,"felineIQ":null}'
json_data_as_python_value = json.loads(stringOfJsonData)
stringOfJsonData = '{"name":"Zophie","isCat":True,"miceCaught":0,"felineIQ":"null"}'
json_data_as_python_value = json.loads(stringOfJsonData)
json.loads("""{"obj": {"str": "ABC","int": 123,"float": -321.89,"bool_true": true,"bool_false": false,"null": null,"array": [1, 2, 3] }}""")
#[Out]# {'obj': {'str': 'ABC',
#[Out]#   'int': 123,
#[Out]#   'float': -321.89,
#[Out]#   'bool_true': True,
#[Out]#   'bool_false': False,
#[Out]#   'null': None,
#[Out]#   'array': [1, 2, 3]}}
stringOfJsonData = '{"name":"Zophie"}'
json_data_as_python_value = json.loads(stringOfJsonData)
stringOfJsonData = '{"name":"Zophie","isCat":True,"miceCaught":0}'
json_data_as_python_value = json.loads(stringOfJsonData)
stringOfJsonData = '{"name":"Zophie","isCat":true}'
json_data_as_python_value = json.loads(stringOfJsonData)
stringOfJsonData = '{"name":"Zophie","isCat":true,"miceCaught":0,"felineIQ":"null"}'
json_data_as_python_value = json.loads(stringOfJsonData)
json_data_as_python_value
#[Out]# {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': 'null'}
stringOfJsonData = '{"name":"Zophie","isCat":true,"miceCaught":0,"felineIQ":null}'
json_data_as_python_value = json.loads(stringOfJsonData)
json_data_as_python_value
#[Out]# {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}
# loads函数读取json
# dumps函数写出json
python_value = {'isCat':True,'miceCaught':0,'name':'Zophie','felineIQ':None}
stringOfJsonData = json.dumps(python_value)
stringOfJsonData
#[Out]# '{"isCat": true, "miceCaught": 0, "name": "Zophie", "felineIQ": null}'
json_data = """{
	"weatherinfo": {
		"city": "深圳",
		"city_en": "shenzhen",
		"date_y": "2014年3月4日",
		"date": "",
		"week": "星期二",
		"fchh": "11",
		"cityid": "101280601",
		"temp1": "20℃~15℃",
		"temp2": "20℃~15℃",
		"temp3": "21℃~16℃",
		"temp4": "19℃~16℃",
		"temp5": "20℃~15℃",
		"temp6": "19℃~14℃",
		"tempF1": "68℉~59℉",
		"tempF2": "68℉~59℉",
		"tempF3": "69.8℉~60.8℉",
		"tempF4": "66.2℉~60.8℉",
		"tempF5": "68℉~59℉",
		"tempF6": "66.2℉~57.2℉",
		"weather1": "多云",
		"weather2": "小雨",
		"weather3": "小雨",
		"weather4": "阴转小雨",
		"weather5": "小雨",
		"weather6": "小雨转阴",
		"img1": "1",
		"img2": "99",
		"img3": "7",
		"img4": "99",
		"img5": "7",
		"img6": "99",
		"img7": "2",
		"img8": "7",
		"img9": "7",
		"img10": "99",
		"img11": "7",
		"img12": "2",
		"img_single": "1",
		"img_title1": "多云",
		"img_title2": "多云",
		"img_title3": "小雨",
		"img_title4": "小雨",
		"img_title5": "小雨",
		"img_title6": "小雨",
		"img_title7": "阴",
		"img_title8": "小雨",
		"img_title9": "小雨",
		"img_title10": "小雨",
		"img_title11": "小雨",
		"img_title12": "阴",
		"img_title_single": "多云",
		"wind1": "微风",
		"wind2": "微风",
		"wind3": "东风3-4级",
		"wind4": "微风",
		"wind5": "微风",
		"wind6": "微风",
		"fx1": "微风",
		"fx2": "微风",
		"fl1": "小于3级",
		"fl2": "小于3级",
		"fl3": "3-4级",
		"fl4": "小于3级",
		"fl5": "小于3级",
		"fl6": "小于3级",
		"index": "较舒适",
		"index_d": "建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。",
		"index48": "较舒适",
		"index48_d": "建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。",
		"index_uv": "弱",
		"index48_uv": "最弱",
		"index_xc": "不宜",
		"index_tr": "适宜",
		"index_co": "舒适",
		"st1": "20",
		"st2": "15",
		"st3": "21",
		"st4": "15",
		"st5": "21",
		"st6": "14",
		"index_cl": "适宜",
		"index_ls": "适宜",
		"index_ag": "极易发"
	}
}
"""
weather_data = json.loads('json_data')
json_data = 
"""
{
	"weatherinfo": {
		"city": "深圳",
		"city_en": "shenzhen",
		"date_y": "2014年3月4日",
		"date": "",
		"week": "星期二",
		"fchh": "11"}
}
"""
json_data = """{
	"weatherinfo": {
		"city": "深圳",
		"city_en": "shenzhen",
		"date_y": "2014年3月4日",
		"date": "",
		"week": "星期二",
		"fchh": "11"}
}"""
weather_data = json.loads('json_data')
json_data = """{
	    "weatherinfo": null
		"city": "深圳",
		"city_en": "shenzhen",
		"date_y": "2014年3月4日",
		"date": "",
		"week": "星期二",
		"fchh": "11"
}"""
weather_data = json.loads('json_data')
json_data = """{
	    "weatherinfo": null
		"city": "深圳",
		"city_en": "shenzhen",
		"date_y": "2014年3月4日",
		"date": "20180902",
		"week": "星期二",
		"fchh": "11"
}"""
weather_data = json.loads('json_data')
weather_data = json.loads('json_data')
json_data = """{
	    "weatherinfo": "unknow",
		"city": "深圳",
		"city_en": "shenzhen",
		"date_y": "2014年3月4日",
		"date": "20180902",
		"week": "星期二",
		"fchh": "11"
}"""
weather_data = json.loads('json_data')
json_data = '{"weatherinfo": "unknow","city": "深圳","city_en": "shenzhen","date_y": "2014年3月4日","date": "20180902","week": "星期二","fchh": "11"}'
weather_data = json.loads('json_data')
json_data = '{"weatherinfo": "unknow"}'
weather_data = json.loads('json_data')
weather_data = json.loads('json_data')
json_data = '{"weatherinfo":"unknow"}'
weather_data = json.loads('json_data')
json_data = '{"weatherinfo":null}'
weather_data = json.loads('json_data')
JSONDECODE ERROR: # 有一处读不过去
# 疯狂报错 
import prettytable
table1 = prettytable.PrettyTable()
table1_row = ['Python','Json']
table_neirow = [['dict','object'],['list & tuple','array'],['str & unicode','string'],['int & long &float ','number'],['True','true'],['False' ,'false'],['None','null']]
table1.add_row(table1_row)
for i in table_neirow:
    table1.add_row(i)
table1
#[Out]# <prettytable.PrettyTable at 0x1abe03c83c8>
for i in table_neirow:
    table1.add_row(i)
    
table1 = table1.add_row(table1_row)
table1
table1 = prettytable.PrettyTable()
table1.add_row(table1_row)
print(table1)
for i in table_neirow:
    table1.add_row(i)
    
print(table1)
table1.field_names = table1_row
print(table1)
tabel_names = ['Json','Python']
table_neirow = [['object','dict'],['array','list'],['string','unicode'],['number(int)','int & long'],['number(real)','float'],['true' ,'Ture'],['false','False'],['null','None']]
table1.field_names = tabel_names
for i in table_neirow:
    table1.add_row(i)
    
print(table1)
table_1 = prettytable.PrettyTable()

table_1.field_names = tabel_names
for i in table_neirow:
    table_1.add_row(i)
    
print(table_1)
# json.dumps  将python对象编码成json字符串
# json.loads 将已编码的json字符串解码为python对象
get_ipython().run_line_magic('pinfo2', 'json.dumps')
get_ipython().run_line_magic('pinfo', 'json.dumps')
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
data 
#[Out]# [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json_1 = json.dumps(data)
print( json_1)
print(json.dumps(data))
import pprint
pprint.pprint(json_1)
pprint.pformat(json_1)
#[Out]# '\'[{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}]\''
print(json_1,sort_keys=True,indent=4,separators = (',', ':'))
print({'a': 'Runoob', 'b': 7},sort_keys=True,indent=4,separators = (',', ':')) # error
print({'a': 'Runoob', 'b': 7},indent=4,separators = (',', ':')) # error 

print(json.dumps({'a': 'Runoob', 'b':7},sort_keys=True,indent=4,separators = (',', ':')))
get_ipython().run_line_magic('pinfo', 'json.loads')

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
json_data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = json.loads(json_data)
print(text)
json_data = {
  "rule":{
    "namespace":"strategy",
    "name":"test_exp_1496234234223400",
    "version":0,
    "last_modify_time":1434234236819000,
    "log_rate":1023300,
    "schema_version":"hello_world!"
  }
}
json_data 
#[Out]# {'rule': {'namespace': 'strategy',
#[Out]#   'name': 'test_exp_1496234234223400',
#[Out]#   'version': 0,
#[Out]#   'last_modify_time': 1434234236819000,
#[Out]#   'log_rate': 1023300,
#[Out]#   'schema_version': 'hello_world!'}}
temp = json.loads(json_data)

json_data = '{
  "rule":{
    "namespace":"strategy",
    "name":"test_exp_1496234234223400",
    "version":0,
    "last_modify_time":1434234236819000,
    "log_rate":1023300,
    "schema_version":"hello_world!"
  }
}'
json_data = '''{
  "rule":{
    "namespace":"strategy",
    "name":"test_exp_1496234234223400",
    "version":0,
    "last_modify_time":1434234236819000,
    "log_rate":1023300,
    "schema_version":"hello_world!"
  }
}'''
temp = json.loads(json_data)
print(temp)
temp
#[Out]# {'rule': {'namespace': 'strategy',
#[Out]#   'name': 'test_exp_1496234234223400',
#[Out]#   'version': 0,
#[Out]#   'last_modify_time': 1434234236819000,
#[Out]#   'log_rate': 1023300,
#[Out]#   'schema_version': 'hello_world!'}}
temp['rule']
#[Out]# {'namespace': 'strategy',
#[Out]#  'name': 'test_exp_1496234234223400',
#[Out]#  'version': 0,
#[Out]#  'last_modify_time': 1434234236819000,
#[Out]#  'log_rate': 1023300,
#[Out]#  'schema_version': 'hello_world!'}
temp['rule']['namespace']
#[Out]# 'strategy'

import re
import requests
#下面的属性？
__author__ = 'liugang'
__project__ 'python_json'
__project__ = 'python_json'
__doc__ = 'myself'
__mail__ = '317121415@qq.com'

url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=552369102522&spuId=853893286&sellerId=701751992&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvv9vJvJgvUpCkvvvvvjiPP2SWljn8nLLhsjrCPmPhzjt8PLqw6jDUR2SW6jiURIhCvCLNqtoaWxdNzA2kZM1wCYM1zQjwQUhCvvsNvVxYZDdNzAmkraACvpvWzQmDSxE4zYG97u5wdphvmpvZEQfH1oLg4FyCvvpvvvvvRphvCvvvvvmCvpvWzQ2HcPB4zYG9RBdwdphvmpvZmpEd4AoZj86Cvvyvm8GmwzWwEBVrvpvBUvQT940rHEHx84GuUZWE3wervpvEvv2Q9fAG2mqYiQhvCvvv9UUCvpvVvmvvvhCvmphvLvkD69vjcWL9a4QB%2BFZc%2BEj6sCywJxcXS47BhC3qVUcnDOmOezIUDajxALwpEcqhtjc6eX1z7tj61WkfV7Q4S47B9CkaU6bnDO2hjC0tvpvIvvvvvhCvvvvvvUUdphvv%2B9vv9krvpvQvvvmm86CvmVWvvUUsphvUIgyCvvOWvvVvaZRivpvUvvmvbqZr%2F%2FZPvpvhJ2X572yCvvpvvvvv3QhvCvvhvvmrvpvBUv9wvyCvvWMD84GuUZWE3wervpvEvvASvFwzCm7kdphvmpvUfpUhCCQiPT6Cvvyv22UmwjvwXN%2FrvpvEvvsKv3O7EjvE9phv2nGv1xQ07rMNUhybzUhCvvsNvWxGaldNzACBIaQtvpvhvvvvvUhCvvsNvmXazxdNzA2XZnACvpvWzQmDSB34zYG975dw&isg=Ag4O1UVS26FtwG4En5NuROh9XuQQJ7YR1hBPrjhRe5DJm471oBzumTMZpfwJ&needFold=0&_ksTS=1507359613080_4232&callback=jsonp4233'
content = requests.get(url)# 获取指定网页的书
print(content.text)# 获取指定网页的json数据
web_content = content.text
#正则表达是除去网页中json数据多余的部分
content = re.findall(r'\w+[(]{1}(.*)[)]{1}',web_content,re.S)
# \w 匹配 字母 数字 下划线
# 12|ww|12w_ + (一个或多个 匹配一次 中间可以任意字符) 匹配一次
# 12(ds12fsdf)  能匹配这样的数据，我还是没弄懂是如何跟json数据多余的部分联系一起
# re.S匹配 换行符 特殊符号
content
#[Out]# ['{"rateDetail":{"rateCount":{"total":29422,"shop":0,"picNum":6421,"used":2152},"rateDanceInfo":{"storeType":4,"currentMilles":1535901504661,"showChooseTopic":false,"intervalMilles":12395659220},"rateList":[{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-30 17:22:54","rateContent":"无论从价位、质量、售后这几个方面来说，还是从鞋子的设计，穿着感受来说，都让我感到十分的喜欢。所以再来买一双。对于这个价位的鞋子来说真的很棒了！ 鞋型的设计，用料都好棒！穿着也很舒服，特别是鞋底，没有从来没穿过这么软，现在穿其他的鞋子还不习惯呢，32个赞。","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015346603928,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2_A1mulnTBKNjSZPfXXbf1XXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/TB2rgb3avQypeRjt_bXXXaZuXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/TB2zSADuljTBKNjSZFDXXbVgVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/TB2GJdKucUrBKNjSZPxXXX00pXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:42","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":30,"hours":14,"seconds":30,"month":7,"timezoneOffset":-480,"year":118,"minutes":43,"time":1535611410000,"day":4},"headExtraPic":"","aucNumId":0,"displayUserNick":"爽***t","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"726-11-97,107;920-11-35,45;620-12-108,121;126-12-19,27;50526-12-91,96;920-11-122,126;620-12-6,8;520-12-0,5;20120-12-9,18;726-11-78,83;426-11-84,90;520-11-54,70;126-12-72,77;1026-12-28,34;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":30,"hours":17,"seconds":54,"month":7,"timezoneOffset":-480,"year":118,"minutes":22,"time":1535620974000,"day":4},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":{"commentId":0,"days":16,"reply":"","commentTime":"2018-08-20 21:58:22","pics":["//img.alicdn.com/bao/uploaded/i2/TB28nlQq5MnBKNjSZFoXXbOSFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/TB29cJ8qZj_B1NjSZFHXXaDWpXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/TB2mB_HqFooBKNjSZPhXXc2CXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/TB2ZpCcq_qWBKNjSZFAXXanSpXa_!!0-rate.jpg"],"content":"鞋子收到了 老公蛮喜欢的 蛮好搭配的 高大上的感觉 而且穿着很舒服不会磨脚 满意"},"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-19 16:52:05","rateContent":"此用户没有填写评论!","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014201653518,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:44","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":4,"hours":16,"seconds":5,"month":7,"timezoneOffset":-480,"year":118,"minutes":52,"time":1533372725000,"day":6},"headExtraPic":"","aucNumId":0,"displayUserNick":"t***2","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":19,"hours":16,"seconds":5,"month":7,"timezoneOffset":-480,"year":118,"minutes":52,"time":1534668725000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-29 10:41:01","rateContent":"虽然自己鞋子已经挺多了，但是总是在换季的时候喜欢来马登逛逛，看到好看的鞋子都忍不住想打开链接看看，就会抑制不住要买的心，这不又买了一双，又想剁手了，快递很给力，没到三天，鞋子就收到了，每一次都有不同的惊喜，鞋头是渐变擦色，橡胶大底，很柔软，可以用手去对折一下，试试柔软度，穿着走路很舒服，鞋垫是用的高迁面料，听客服说是猪皮的，不懂皮料，用手指延边上轻按会看到皮料的毛孔，透气性很高，很搭牛仔裤，显腿长，让我变成长腿欧巴，在福叔家用诚意十足的价格，享受过往绝佳的购物体验，已经中了福叔的毒，也不打算解了，话不多说，肯定好评撒！","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015047144823,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2u4yut5AnBKNjSZFvXXaTKXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/TB2VOv7tRnTBKNjSZPfXXbf1XXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/TB2r0yntYZnBKNjSZFKXXcGOVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/TB2Nf_ptHwrBKNjSZPcXXXpapXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/TB253F7tZj_B1NjSZFHXXaDWpXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:40","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":29,"hours":10,"seconds":19,"month":7,"timezoneOffset":-480,"year":118,"minutes":38,"time":1535510299000,"day":3},"headExtraPic":"","aucNumId":0,"displayUserNick":"y***6","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"426-11-136,143;10526-12-103,110;10120-11-154,162;420-11-74,79;520-12-210,222;726-12-163,167;920-12-185,190;920-11-116,119;19-11-168,184;126-11-30,48;726-12-144,153;726-12-111,115;726-12-168,184;626-12-144,153;620-12-85,91;920-12-197,200;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":29,"hours":10,"seconds":1,"month":7,"timezoneOffset":-480,"year":118,"minutes":41,"time":1535510461000,"day":3},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-26 20:12:55","rateContent":"第二次购买了，老公的脚比较大比较宽，穿这种款式还不错，上次买了灰色也好看，比较百搭，所以这次换这个颜色试试，这个颜色也不错，什么衣服裤子都可以搭配，主要是也比较好穿，而且质量也还可以，相对这个价钱买到这样的鞋真心划算，以后会再来的！希望款式越来越多！","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014787484584,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2STgCs8smBKNjSZFFXXcT9VXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:41","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":26,"hours":20,"seconds":12,"month":7,"timezoneOffset":-480,"year":118,"minutes":8,"time":1535285292000,"day":0},"headExtraPic":"","aucNumId":0,"displayUserNick":"彤***2","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"520-11-92,108;226-11-27,36;126-11-37,41;126-11-18,26;620-11-83,91;226-12-42,53;920-12-7,17;226-11-54,61;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":26,"hours":20,"seconds":55,"month":7,"timezoneOffset":-480,"year":118,"minutes":12,"time":1535285575000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-04 13:50:59","rateContent":"鞋头渐变擦色非常有格调，黄棕色的橡胶鞋底保留了橡胶原本的颜色，和渐变鞋面整体和谐，细节做的到位，很少有休闲鞋鞋跟上有环带的，这款鞋有，方便晾晒和提鞋，确实非常正的一双鞋，包括性价比，不过只给99分，自己拍的跟我姐给我拍的完全就是天壤之别啊，大家将就看看啊","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1012497238703,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2VY.FIQyWBuNjy0FpXXassXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/TB2x9VvIY1YBuNjSszhXXcUsFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/TB2PRJLI1ySBuNjy1zdXXXPxFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/TB2FTQ9IKSSBuNjy0FlXXbBpVXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:40","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":3,"hours":19,"seconds":55,"month":7,"timezoneOffset":-480,"year":118,"minutes":13,"time":1533294835000,"day":5},"headExtraPic":"","aucNumId":0,"displayUserNick":"d***6","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"226-12-12,30;620-11-75,84;526-11-41,47;620-12-62,66;920-11-31,40;920-12-48,61;10526-12-0,11;620-12-67,74;20520-12-85,90;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":4,"hours":13,"seconds":59,"month":7,"timezoneOffset":-480,"year":118,"minutes":50,"time":1533361859000,"day":6},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-26 21:55:33","rateContent":"这应该是第三双了，试了下脚感不错，比较软，颜色样式也和预期差不多，希望耐穿","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014839573647,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2iuJbtljTBKNjSZFwXXcG4XXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:41","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":26,"hours":21,"seconds":54,"month":7,"timezoneOffset":-480,"year":118,"minutes":53,"time":1535291634000,"day":0},"headExtraPic":"","aucNumId":0,"displayUserNick":"z***4","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"726-11-17,20;426-11-9,16;126-11-21,32;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":26,"hours":21,"seconds":33,"month":7,"timezoneOffset":-480,"year":118,"minutes":55,"time":1535291733000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-21 23:37:20","rateContent":"不错，上脚挺好看的，就是不透气，有点热..过几天穿正合适。质量做工都可以，价格也便宜..喜欢的朋友值得入手.","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014320961602,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i3/TB2RvdCrpooBKNjSZFPXXXa2XXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:38","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":21,"hours":23,"seconds":59,"month":7,"timezoneOffset":-480,"year":118,"minutes":34,"time":1534865699000,"day":2},"headExtraPic":"","aucNumId":0,"displayUserNick":"f***9","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,2;926-11-29,36;620-11-29,36;1026-11-3,9;920-12-16,19;520-11-37,42;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":21,"hours":23,"seconds":20,"month":7,"timezoneOffset":-480,"year":118,"minutes":37,"time":1534865840000,"day":2},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-31 19:03:54","rateContent":"不拍图了，有点懒，鞋子很好，精致，简约。大气，时尚。说假话不是人的。很好，掌柜的也很耐心，建议的尺码准确。第二次买鞋子了。","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015467307136,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:41","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":31,"hours":19,"seconds":31,"month":7,"timezoneOffset":-480,"year":118,"minutes":1,"time":1535713291000,"day":5},"headExtraPic":"","aucNumId":0,"displayUserNick":"l***4","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"620-11-9,13;920-13-5,8;126-11-20,22;10120-11-37,44;126-11-23,25;620-12-53,60;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":31,"hours":19,"seconds":54,"month":7,"timezoneOffset":-480,"year":118,"minutes":3,"time":1535713434000,"day":5},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-31 12:32:06","rateContent":"领卷买的更划算✌️质量很好，皮质也很软，老公出差了，等回来就可以穿了！物流也很快哟😊","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015420435006,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i3/TB2UCtXuBnTBKNjSZPfXXbf1XXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/TB2bigquaQoBKNjSZJnXXaw9VXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:40","anony":true,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":31,"hours":12,"seconds":24,"month":7,"timezoneOffset":-480,"year":118,"minutes":29,"time":1535689764000,"day":5},"headExtraPic":"","aucNumId":0,"displayUserNick":"c***2","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"620-11-9,13;726-11-14,19;520-11-0,7;420-11-35,41;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":31,"hours":12,"seconds":6,"month":7,"timezoneOffset":-480,"year":118,"minutes":32,"time":1535689926000,"day":5},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-25 23:03:02","rateContent":"很不错，又结实，大气，100多块钱花的值，下次还会在来买个黑色的，大力支持，大力推荐，盒子看起来就高大上","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014844307434,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/TB2V4glsOAnBKNjSZFvXXaTKXXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:42","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":25,"hours":23,"seconds":37,"month":7,"timezoneOffset":-480,"year":118,"minutes":1,"time":1535209297000,"day":6},"headExtraPic":"","aucNumId":0,"displayUserNick":"我***芝","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-33,37;920-11-0,3;126-11-8,10;920-11-11,20;920-11-4,7;920-11-38,42;126-11-43,52;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":25,"hours":23,"seconds":2,"month":7,"timezoneOffset":-480,"year":118,"minutes":3,"time":1535209382000,"day":6},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-30 11:08:46","rateContent":"鞋子很满意，就是第一次客户推荐错了尺码，退换之后很合脚","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015257510692,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:42","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":30,"hours":11,"seconds":57,"month":7,"timezoneOffset":-480,"year":118,"minutes":7,"time":1535598477000,"day":4},"headExtraPic":"","aucNumId":0,"displayUserNick":"t***2","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"20120-11-20,27;620-11-0,5;326-12-6,19;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":30,"hours":11,"seconds":46,"month":7,"timezoneOffset":-480,"year":118,"minutes":8,"time":1535598526000,"day":4},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-31 19:53:44","rateContent":"宝贝跟描述的一样，舒适，很不错的","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015361545427,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/TB2wIijuz7nBKNjSZLeXXbxCFXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:40","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":30,"hours":18,"seconds":48,"month":7,"timezoneOffset":-480,"year":118,"minutes":46,"time":1535626008000,"day":4},"headExtraPic":"","aucNumId":0,"displayUserNick":"h***8","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"426-11-9,11;920-11-12,16;720-11-0,8;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":31,"hours":19,"seconds":44,"month":7,"timezoneOffset":-480,"year":118,"minutes":53,"time":1535716424000,"day":5},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-21 13:51:53","rateContent":"物超所值，质量很好。今天由于穿的裤子和这双鞋子不搭配，所以没有拍照片。你是否很疑惑，这是百搭的鞋子为什么和我的裤子不配。泥马你穿超短跑步的裤子和这双鞋配一个试试看。","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014358927304,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2ZU1GqZIrBKNjSZK9XXagoVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/TB2t_KThhtnkeRjSZSgXXXAuXXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:灰色 偏大一码（推荐指数★★★★★）;尺码:40","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":20,"hours":14,"seconds":19,"month":7,"timezoneOffset":-480,"year":118,"minutes":27,"time":1534746439000,"day":1},"headExtraPic":"","aucNumId":0,"displayUserNick":"l***g","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"620-12-10,26;520-11-0,4;920-12-60,81;620-11-5,9;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":21,"hours":13,"seconds":53,"month":7,"timezoneOffset":-480,"year":118,"minutes":51,"time":1534830713000,"day":2},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-30 17:36:55","rateContent":"鞋子非常棒，客服人员也很贴心，一直忙着，没来得及评价，希望店家看到不要怪罪客服，完全我的问题。","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015302826184,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/TB2QRhxuyQnBKNjSZFmXXcApVXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黑色 偏大一码（推荐指数★★★★★）;尺码:40","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":25,"hours":17,"seconds":8,"month":7,"timezoneOffset":-480,"year":118,"minutes":52,"time":1535190728000,"day":6},"headExtraPic":"","aucNumId":0,"displayUserNick":"喂***升","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"10120-11-6,14;920-12-15,19;620-11-0,5;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":30,"hours":17,"seconds":55,"month":7,"timezoneOffset":-480,"year":118,"minutes":36,"time":1535621815000,"day":4},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-27 10:44:23","rateContent":"鞋子非常喜欢，Very good ！","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014977647979,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2XSwss0knBKNjSZKPXXX6OFXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:38","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":27,"hours":10,"seconds":7,"month":7,"timezoneOffset":-480,"year":118,"minutes":39,"time":1535337547000,"day":1},"headExtraPic":"","aucNumId":0,"displayUserNick":"d***0","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-12,16;620-11-0,6;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":27,"hours":10,"seconds":23,"month":7,"timezoneOffset":-480,"year":118,"minutes":44,"time":1535337863000,"day":1},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-30 12:48:24","rateContent":"蛮好的，跟店家描述一致！难得在网上一次愉快的买鞋！看图。。。","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015314083911,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2s..ckhtnkeRjSZSgXXXAuXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/TB2_dIIt0knBKNjSZKPXXX6OFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/TB2azEmuiQnBKNjSZFmXXcApVXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:灰色 偏大一码（推荐指数★★★★★）;尺码:39","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":30,"hours":12,"seconds":1,"month":7,"timezoneOffset":-480,"year":118,"minutes":43,"time":1535604181000,"day":4},"headExtraPic":"","aucNumId":0,"displayUserNick":"j***x","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,3;720-11-4,11;620-11-12,24;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":30,"hours":12,"seconds":24,"month":7,"timezoneOffset":-480,"year":118,"minutes":48,"time":1535604504000,"day":4},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-31 19:41:02","rateContent":"鞋子码很正，真的比皮鞋要买小一码，穿着舒服，值得买","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015360557009,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:42","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":30,"hours":16,"seconds":3,"month":7,"timezoneOffset":-480,"year":118,"minutes":22,"time":1535617323000,"day":4},"headExtraPic":"","aucNumId":0,"displayUserNick":"t***6","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"426-11-17,21;520-11-22,25;326-11-0,5;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":31,"hours":19,"seconds":2,"month":7,"timezoneOffset":-480,"year":118,"minutes":41,"time":1535715662000,"day":5},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-27 15:11:50","rateContent":"第二次买了，还是那么好","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014862420970,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/TB2v5wKtXkoBKNjSZFEXXbrEVXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:41","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":27,"hours":15,"seconds":2,"month":7,"timezoneOffset":-480,"year":118,"minutes":11,"time":1535353862000,"day":1},"headExtraPic":"","aucNumId":0,"displayUserNick":"被***2","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-6,11;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":27,"hours":15,"seconds":50,"month":7,"timezoneOffset":-480,"year":118,"minutes":11,"time":1535353910000,"day":1},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t2-18.png","rateDate":"2018-08-31 16:35:21","rateContent":"鞋子不错，很喜欢，就是有一点偏小，我感觉还是本来脚多大就买多大的","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1015301588106,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:41","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":31,"hours":16,"seconds":20,"month":7,"timezoneOffset":-480,"year":118,"minutes":34,"time":1535704460000,"day":5},"headExtraPic":"","aucNumId":0,"displayUserNick":"乱***生","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"326-13-9,16;620-11-0,4;920-11-5,8;","cmsSource":"天猫","tamllSweetLevel":2,"gmtCreateTime":{"date":31,"hours":16,"seconds":21,"month":7,"timezoneOffset":-480,"year":118,"minutes":35,"time":1535704521000,"day":5},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2018-08-22 18:09:47","rateContent":"很好：特别满意,第一次购买到自己满意的鞋子,穿了很舒服！值得大家购买,真的不错哦！","fromMall":true,"userIdEncryption":"","sellerId":701751992,"displayUserLink":"","id":1014398025717,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i2/TB2NTGrrFooBKNjSZFPXXXa2XXa_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"颜色分类:黄棕色 偏大一码（推荐指数★★★★★）;尺码:38","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":22,"hours":18,"seconds":40,"month":7,"timezoneOffset":-480,"year":118,"minutes":5,"time":1534932340000,"day":3},"headExtraPic":"","aucNumId":0,"displayUserNick":"t***8","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,2;620-11-8,21;920-11-3,7;426-11-22,27;920-11-35,40;920-11-28,34;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":22,"hours":18,"seconds":47,"month":7,"timezoneOffset":-480,"year":118,"minutes":9,"time":1534932587000,"day":3},"useful":true,"displayUserRateLink":""}],"searchinfo":"","paginator":{"lastPage":99,"page":1,"items":28526},"tags":[]}}']
content[0]
#[Out]# 
# content[0] 和 content 内容一样，因为content就一个元素
len(content)
#[Out]# 1
type(content)
#[Out]# list
content = re.findall(r'\w+[(]{1}(.*)[)]{1}',web_content,re.S)
# 正则表达书没起作用啊，就找到一个包含的
python_content = json.loads(content[0])
count = len(python_content['rateDetail']['rateList'])
count
#[Out]# 20

for i in range(count):
    print(python_content['rateDetail']['rateList'][i]['rateContent'])

python_content

type(python_content)
#[Out]# dict
get_ipython().run_line_magic('logstop', '')
count = len(python_content['rateDetail']['rateList'])

for i in range(count):
    print(python_content['rateDetail']['rateList'][i]['rateContent'])
	

# 样例json的结构
	
{
	"rateDetail":
	{
		"rateCount":
		{
			"...":...,
			"...":...,
			"...":...,
			"...":...,
		}
		"rateDanceInfo":
		{
			"...":...,
			"...":...,
			"...":...,
			"...":...,
		}
		"rateList":[
		{
		"auctionPicUrl":...,
		...,
		"rateContent":评论内容-1,
		...
		}
		{
		"auctionPicUrl":...,
		...,
		"rateContent":评论内容-2,
		...		
		},
		{},
		{},
		{},
		{},
		//count([]) = 20
		//每个{}都有rateContent
		]
		"searchinfo":"",
		...,
		"tags":[]//多个{}用[]枚举
	}
}

