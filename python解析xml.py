# -*- coding: utf-8 -*-
"""
创建时间 Thu Aug 30 10:21:16 2018
描述:用ET解析XML
作者:PM.liugang
"""

'''
练习名称 xml1
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

import xml.ETree.ElementTree as ET

tree = ET.parse('xml1.xml')
root = tree.gETroot()

print(root.tag,':',root.attrib) # 1
'''
1 print -> data:{}
'''

for child in root:
    print(child.tag,':',child.attrib) # 2
    for children in child:
        print(children.tag,':',children.attrib) # 3
        
'''
# 2
print ->
country : {'name': 'Liechtenstein'}
# 3
rank : {'updated': 'yes'}
year : {}
gdppc : {}
neighbor : {'name': 'Austria', 'direction': 'E'}
neighbor : {'name': 'Switzerland', 'direction': 'W'}
# 2
country : {'name': 'Singapore'}
# 3
rank : {'updated': 'yes'}
year : {}
gdppc : {}
neighbor : {'name': 'Malaysia', 'direction': 'N'}
# 2
country : {'name': 'Panama'}
# 3
rank : {'updated': 'yes'}
year : {}
gdppc : {}
neighbor : {'name': 'Costa Rica', 'direction': 'W'}
neighbor : {'name': 'Colombia', 'direction': 'E'}
'''

'''
遍历文本
In [  ]: root[0][1].text
Out[42]: '2008'

In [  ]: root[0][2].text
Out[43]: '141100'

In [  ]: root[0][0].text
Out[44]: '2'

In [45]: root[0][3].text
Out[45]: None

In [46]: root[0][4].text
Out[46]: None
'''

'''
ElementTree提供的方法
find(match)                  # 查找第一个匹配的子元素， match可以时tag或是xpaht路径
findall(match)               # 返回所有匹配的子元素列表
findtext(match, default=None)#
iter(tag=None)               # 以当前元素为根节点 创建树迭代器,如果tag不为None,则以tag进行过滤
iterfind(match)              #
'''

for neighbor in root.iter('neighbor'):
    print(neighbor.tag,":",neighbor.attrib) # 4
'''  
# 4
print ->
neighbor : {'name': 'Austria', 'direction': 'E'}
neighbor : {'name': 'Switzerland', 'direction': 'W'}
neighbor : {'name': 'Malaysia', 'direction': 'N'}
neighbor : {'name': 'Costa Rica', 'direction': 'W'}
neighbor : {'name': 'Colombia', 'direction': 'E'}
'''

#遍历所有的country标签
for country in root.findall('country'):
    #查找country标签下的第一个rank标签
    rank = country.find('rank').text
    #获取country标签的name属性
    name = country.gET('name')
    print(name,rank) # 5

'''
# 5  
Liechtenstein 2
Singapore 5
Panama 69
'''

#修改xml结构
##属性相关

###将所有的rank值加1，并添加属性updated为yes
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.sET('updated','yes')

###再终端显示整个xml
ET.dump(root) # 6

'''
# 6
<data>
    <country name="Liechtenstein">
        <rank updated="yes">4</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">7</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">71</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
'''

###注意 修改的内容存在内容中 尚未保存到文件中
###保存修改后的内容
tree.write('output.xml')

tree = ET.parse('output.xml')

root = tree.gETroot()

for rank in root.iter('rank'):
    del rank.attrib['updated']

ET.dump(root) # 7

'''
# 7 
<data>
    <country name="Liechtenstein">
        <rank>4</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank>7</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank>71</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
'''

for country in root.iter('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

ET.dump(root) # 8

'''
# 8
<data>
    <country name="Liechtenstein">
        <rank>4</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank>7</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    </data>
'''

# IPython log file

import xml.etree.ElementTree as ET
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\Users\\Administrator'
get_ipython().run_line_magic('cd', 'Desktop/')
get_ipython().run_line_magic('ls', '')
tree = ET.parse('xml1.xml')
root = tree.getroot()
root[0]
#[Out]# <Element 'country' at 0x000000000768B368>
countrty = root[0]
countrty
#[Out]# <Element 'country' at 0x000000000768B368>
ET.dump(root)
list(countrty)
#[Out]# [<Element 'rank' at 0x000000000768B3B8>, <Element 'year' at 0x000000000768B408>, <Element 'gdppc' at 0x000000000768B458>, <Element 'neighbor' at 0x000000000768B4A8>, <Element 'neighbor' at 0x000000000768B4F8>]
len(list(countrty))
#[Out]# 5
countrty[4]
#[Out]# <Element 'neighbor' at 0x000000000768B4F8>
countrty[3]
#[Out]# <Element 'neighbor' at 0x000000000768B4A8>
last_ele = country[len(list(countrty）-1]
last_ele = country[len(list(countrty))-1]
last_ele = countrty[len(list(countrty))-1]
last_ele.tail = '\n\t\t'
country = root[0]
last_ele = country[len(list(country))-1]
last_ele.tail = '\n\t\t'
get_ipython().run_line_magic('pinfo', 'logstart')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\Users\\Administrator\\Desktop'
get_ipython().run_line_magic('logstart', '-0 xml_note.txt')
last_ele
#[Out]# <Element 'neighbor' at 0x000000000768B4F8>
last_ele.tail = '\n\t\t'
elem1 = ET.Element('test_append')
ET.Element('test_append')
#[Out]# <Element 'test_append' at 0x0000000007690728>
elem.text = 'elem 1'
elem1.text = 'elem 1'
countrty.append(elem1)
elem2 = ET.SubElement(country,'test_subelement')
elem2.text = 'elem 2'
elem3 = ET.Element('test_extend')
elem3.text = 'elem 3'
elem4 = ET.Element('test_extend')
elem4.text = 'elem 3'
elem5 = ET.Element('test_insert')
elem5.text = 'elem 5'
country.insert(5,elem5)
ET.dump(country)
# append(subelement)
# extend(subelement)
# insert(subelement)
import xml.etree.ElementTree as ET


def subElement(root, tag, text):
    ele = ET.SubElement(root, tag)
    ele.text = text
    ele.tail = '\n'


root = ET.Element("note")

to = root.makeelement("to", {})
to.text = "peter"
to.tail = '\n'
root.append(to)

subElement(root, "from", "marry")
subElement(root, "heading", "Reminder")
subElement(root, "body", "Don't forget the meeting!")

tree = ET.ElementTree(root)
tree.write("note.xml", encoding="utf-8", xml_declaration=True)

import xml.etree.ElementTree as ET


def subElement(root, tag, text):
    ele = ET.SubElement(root, tag)
    ele.text = text
    ele.tail = '\n'


root = ET.Element("note")

to = root.makeelement("to", {})
to.text = "peter"
to.tail = '\n'
root.append(to)

subElement(root, "from", "marry")
subElement(root, "heading", "Reminder")
subElement(root, "body", "Don't forget the meeting!")

tree = ET.ElementTree(root)
tree.write("note.xml", encoding="utf-8", xml_declaration=True)

get_ipython().run_line_magic('ls', '')
ET.dump('note.xml')
ET.dump('note.xml')
tree = ET.parse('note.xml')
root = tree.getroot()
ET.dump(root)
import xml.etree.ElementTree as ET
from xml.dom import minidom


def subElement(root, tag, text):
    ele = ET.SubElement(root, tag)
    ele.text = text


def saveXML(root, filename, indent="\t", newl="\n", encoding="utf-8"):
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)


root = ET.Element("note")

to = root.makeelement("to", {})
to.text = "peter"
root.append(to)

subElement(root, "from", "marry")
subElement(root, "heading", "Reminder")
subElement(root, "body", "Don't forget the meeting!")

# 保存xml文件
saveXML(root, "note_1.xml")

tree = ET.parse('note_1.xml')
root = tree.getroot()
ET.dump(root)
get_ipython().run_line_magic('logstop', '')
