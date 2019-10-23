# -*- coding: utf-8 -*-
import os, random, string, tkinter
import time
import qrcode
import tkinter.filedialog

from tkinter import messagebox
from string import digits
from pystrich.ean13 import EAN13Encoder

root = tkinter.Tk()
number = "1234567890"
letter = "ABCDEFGHIJKLMNPQRSTUVWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i = 0

randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""


def mkdir(path):
    # 判断保存防伪码或补充防伪码的文件夹是否存在，如果不存在则建立文件
    isexist = os.path.exists(path)
    if not isexist:
        os.mkdir(path)
        

def openfile(filename):
    # 读取文件文本函数，读取保存产品编码和生成数量的文件mrsoft.mri，以及用户选择的已生成的编码文件
    f = open(filename)
    fllist = f.read()
    f.close()
    return  fllist


def inputbox(showstr, showorder, length):
    """
    输入验证判断函数，根据参数判断输入的是哪种类型，是否合法
    :param showstr: 输入提示
    :param showorder: 输入的类型：1->数字(长度不受限制) 2->字母 3->数字(长度受length限制)
    :param length: 对数字位数的限制，0表示不限制
    :return:
    """
    instr = input(showstr)
    if len(instr) != 0:
        if showorder == 1:
            if str.isdigit(instr):
                if instr == 0:
                    print('输入为零，请重新输入')
                    return '0'
                else:
                    return instr
            else:
                print('输入非法，请重新输入')
                return '0'

        if showorder == 2:
            if str.isalpha(instr):  # 判断输入是否为字母
                if len(instr) != length:
                    print('必须输入' + str(length) + '个字母，请重新输入！')
                    return '0'
                else:
                    return instr
            else:
                print('输入非法，请重新输入！')
                return '0'

        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print('必须输入' + str(length) + '个字母，请重新输入！')
                    return '0'
                else:
                    return instr
            else:
                print('输入非法，请重新输入！')
                return '0'
    else:
        print('输入为空，请重新输入！')
        return '0'

def wfile(sstr, sfile, typeis, smsg, datapath):
    """
    编码输出显示函数，通过屏幕输出和文件输出两种方式输出生成的防伪码信息

    :param sstr: 为生成的防伪码
    :param sfile: 保存防伪码的文件名
    :param typeis: 显示 输出完成 的信息提示框
    :param smsg: 为提示框显示的提示内容
    :param datapth: 保存防伪码的路径
    :return:

    """
    mkdir(datapath)
    # datafile = datapath + '\\' + sfile
    file = open(sfile, 'w')
    wrlist = sstr
    pdata = ''
    wdata = ''
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[','')).replace(']','')
        wdata = wdata.replace(''''', '').replace(''''','')
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print('')
    if typeis != 'no':
        messagebox.showinfo('提示',
                            smsg
                            + str(len(randstr))
                            + '\n防伪码文件存放位置：'
                            + sfile)
        root.withdraw()

def scode1(schoice):
    incount = inputbox('请输入您要生成验证码的数量:', 1, 0)
    while int(incount) == 0:
        incount = inputbox('请输入您要生成验证码的数量:', 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ''
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + '\n'
        randstr.append(randfir)
    wfile(randstr,
          'scode' + str(schoice) + '.txt',
          '',
          '已生成6位防伪码共计：',
          'codepath')


def scode2(schoice):
    ordstart = inputbox('请输入系列产品的数字起始号(3位)：',1, 0)
    while int(ordstart) == 0:
        ordstart = inputbox('请输入系列产品的数字起始号(3位)', 1, 0)
    ordcount = inputbox('请输入产品系列的数量：', 1, 0)
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount = inputbox('请输入产品系列的数量：', 1, 0)
    incount = inputbox('请输入要生成的每个系列产品的防伪码数量', 1, 0)
    while int(incount) == 0:
        incount = inputbox('请输入要生成的每个系列产品的防伪码数量', 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir = ''
            for i in range(6):
                randfir = randfir + random.choice(number)
            randstr.append(str(int(ordstart) + m) + randfir + '\n')
    wfile(randstr, 'scode' + str(schoice) + '.txt', '', '已生成9位系列产品防伪码共计：', 'codepath')


def scode3(schoice):
    incount = inputbox('请输入要生成的25位混合产品序列号数量', 1, 0)
    while int(incount) == 0:
        incount = inputbox('请输入要生成的25位混合产品序列号数量', 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        strone = ''
        for i in range(25):
            strone = strone + random.choice(letter)
        strtwo = strone[:5] + '-' + strone[5:10] + '-' + strone[10:15] + '-' + strone[15:20] + '-' + strone[20:25] + '\n'
        randstr.append(strtwo)
    wfile(randstr, 'scode' + str(schoice) + '.txt', '已生成25混合防伪序列码共计：', '', 'codepath')


def scode4(schoice):
    """
    生成含数据分析功能防伪码编码函数

    :param schoice: 设置输出的文件名称
    :return:
    """

    intype = inputbox('请输入数据分析编号（3位字母）:', 2, 3)
    while not str.isalpha((intype) or len(intype) != 3):
        intype = inputbox('请输入数据分析编号（3位字母）:', 2, 3)
    incount = inputbox('请输入要生成的带数据分析功能的验证码数量:', 1, 0)
    while int(incount) == 0:
        incount = inputbox('请输入要生成的带数据分析功能的验证码数量:', 1, 0)
    ffcode(incount, intype, '', schoice)


def scode5(schoice):
    # 智能批量生成带数据分析功能的防伪码
    default_dir = r'codeauto.mri'
    file_path = tkinter.filedialog.askopenfilename(filetypes=[('Text file', '*.mri')], # Text file(*.mri) 没有
                                                   title='请选择智能批处理文件:',
                                                   initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)
    print("前：", codelist)
    codelist = codelist.split('\n')
    print(codelist)
    print("后：", codelist)
    for item in codelist:  # ['abc,10', 'qwe,5']
        codea = item.split(',')[0]
        codeb = item.split(',')[1]
        ffcode(codeb, codea, 'no', schoice)


def scode6(schoice):
    # 防伪码补充生成
    default_dir = r'C:\Users\admin\Desktop\myself\python_project_highlights\2\abcscode5.txt'
    file_path = tkinter.filedialog.askopenfilename(title='请选择已经生成的防伪码文件:',
                                                   initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)
    codelist = codelist.split('\n')
    codelist.remove('')  # 移除空列表中的空元素
    strset = codelist[0]
    # maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式
    # 第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
    # 两个字符串的长度必须相同，为一一对应的关系
    remove_digits = strset.maketrans('', '', digits)
    res_letter = strset.translate(remove_digits) # -> only letter

    nres_letter = list(res_letter)
    strpro = nres_letter[0]
    strtype = nres_letter[1]
    strclass = nres_letter[2]
    nres_letter = strpro.replace(''''','').replace(''''', '') \
                  + strtype.replace(''''','').replace(''''', '') \
                  + strclass.replace(''''','').replace(''''', '')
    card = set(codelist)  # 原防伪码的集合
    messagebox.showinfo('提示', '之前的防伪码共计:' + str(len(card)))
    root.withdraw()
    incount = inputbox('请输入补充防伪码生成的数量：', 1, 0)
    for i in range(int(incount) * 2):
        randfir = random.sample(number, 3)  # 随机产生3位不重复的数字
        randsec = sorted(randfir)  # 对产色的数字排序，相当于确定插入字母的索引
        addcount = len(card)  # 原文件的防伪码数量
        strone = ''
        for i in range(9):  # 生成9位的数字防伪码
            strone = strone + random.choice(number)
        sim = str(strone[0 : int(randsec[0])]) \
              + strpro \
              + str(strone[int(randsec[0]) : int(randsec[1])]) \
              + strtype \
              + str(strone[int(randsec[1]) : int(randsec[2])]) \
              + strclass \
              + str(strone[int(randsec[2]) : 9]) \
              + '\n'
        card.add(sim)  # 添加新生成的防伪码到集合
        #  根据查看是否添加成功，判断防伪码于原有的防伪码是否有重复
        if len(card) > addcount:
            randstr.append(sim) # 添加新防伪码到新的防伪码列表
            addcount = len(card)  # 记录新生成防伪码集合的防伪码的数量
        if len(randstr) >= int(incount):
            print(len(randstr))  # 输出新生成的防伪码的数量
            break
    wfile(randstr,
          nres_letter + 'ncode' + str(choice) + '.txt',
          nres_letter,
          '生成后补防伪码共计：',
          'codeadd')


def scode7(schoice):
    # 条形码批量生成的函数
    mainid = inputbox('请输入EN13的国家代码（3位） :', 1, 0)
    while int(mainid) < 1 or len(mainid) !=3:
        mainid = inputbox('请输入EN13的国家代码（3位） :', 1, 0)

    compid = inputbox('请输入EAN13的企业代码（4位）:', 1, 0)
    while int(compid) < 1 or len(compid) != 4:
        compid = inputbox('请输入EAN13的企业代码（4位）:', 1, 0)

    incount = inputbox(' 请输入要生成的条形码数量:', 1, 0)
    while int(incount) == 0:
        incount = inputbox(' 请输入要生成的条形码数量:', 1, 0)

    mkdir('barcode')
    for j in range(int(incount)):
        strone = ''
        for i in range(5):
            strone = strone + str(random.choice(number))
        barcode = mainid + compid + strone
        # 计算条形码的校验位
        evensum = int(barcode[1])  \
                  + int(barcode[3])  \
                  + int(barcode[5]) \
                  + int(barcode[7])  \
                  + int(barcode[9])  \
                  + int(barcode[11]) # 偶数位
        oddsum =int( barcode[0])\
                + int(barcode[2])\
                + int(barcode[4])\
                + int(barcode[6]) \
                + int(barcode[8]) \
                + int(barcode[10])
        # checkbit=int(10-(evensum *3 + oddsum)%10)
        checkbit = int((10 - (evensum * 3 + oddsum) %10)% 10)
        barcode=barcode+str(checkbit)  # 组成完整的EAN13条形码的13位数字
        print (barcode)
        encoder = EAN13Encoder(barcode)  # 调用EAN13Encoder生成条形码
        encoder.save("barcode\\" + barcode  + ".png")  # 保存条形码信息图片到文件


def scode8(schoice):
    # 输入要生成的二维码数量
    incount = inputbox("请输入要生成的12位数字二维码数量:", 1, 0)
    while int(incount) == 0:  # 如果输入不是大于0的数字，重新输入
        incount = inputbox("请输入要生成的12位数字二维码数量:", 1, 0)

    mkdir("qrcode")  # 判断保存二维码的文件夹是否存在，不存在，则创建该文件夹
    for j in range(int(incount)):  # 批量生成二维码
        strone = ''  # 清空存储单条二维码的变量
        for i in range(12):  # 生成单条二维码数字
            strone = strone + str(random.choice(number))
        encoder = qrcode.make(strone)  # 生成二维码
        encoder.save("qrcode\\" + strone + ".png")  # 保存二维码图片到文件


def scode9(schoice):
    default_dir = r'lottery.ini'
    file_path = tkinter.filedialog.askopenfilename(filetypes=[('Ini file', '*.ini')],
                                                   title='请选择智能批处理文件',
                                                   initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)
    codelist = codelist.split('\n')
    incount = inputbox('', 1, 0)
    while int(incount) == 0 or len(codelist) < int(incount):
        incount = inputbox('', 1, 0)
        strone = random.sample(codelist, int(incount))
        for i in range(int(incount)):
            wdata = str(strone[i].replace('[','')).replace(']', '')
            wdata = wdata.replace("'''",'').replace("''",'')
            print(wdata)

def ffcode(scount, typestr, ismessage, schoice):
    """
    生成含数据分析功能防伪编码函数，参数scount为要生成的防伪码数量
    :param scount: 防伪码数量
    :param typestr: 数据分析字符
    :param ismessage: 输出完成时是否显示信息 no->不显示
    :param schoice: 输出的文件名称
    :return:
    """
    randstr.clear()
    for j in range(int(scount)):
        strpro = typestr[0].upper()
        strtype = typestr[1].upper()
        strclass = typestr[2].upper()
        randfir = random.sample(number, 3)
        randsec = sorted(randfir)
        letterone = ''
        for i in range(9):
            letterone = letterone + random.choice(number)
        sim = str(letterone[0 : int(randsec[0])]) \
              + strpro \
              + str(letterone[int(randsec[0]) : int(randsec[1])]) \
              + strtype \
              + str(letterone[int(randsec[1]) : int(randsec[2])]) \
              + strclass \
              + str(letterone[int(randsec[2]) : 9]) \
              + '\n'
        randstr.append(sim)
    wfile(randstr, typestr + 'scode' + str(schoice) + '.txt', ismessage, '', 'codepath')


def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print('输入非法，请重新输入！！')
            return 0
        else:
            return insel
    else:
        print('输入非法，请重新输入！！')
        return 0


# 企业编码管理系统主菜单
def mainmenu():
    # os.system("clear")
    print("""
      ****************************************************************
                            企业编码生成系统
      ****************************************************************
          1.生成6位数字防伪编码 （213563型）
          2.生成9位系列产品数字防伪编码(879-335439型)
          3.生成25位混合产品序列号(B2R12-N7TE8-9IET2-FE35O-DW2K4型)
          4.生成含数据分析功能的防伪编码(5A61M0583D2)
          5.智能批量生成带数据分析功能的防伪码
          6.后续补加生成防伪码(5A61M0583D2)
          7.EAN-13条形码批量生成
          8.二维码批量输出          
          9.企业粉丝防伪码抽奖
          0.退出系统
      ================================================================
      说明：通过数字键选择菜单
      ================================================================
    """)


while i < 9:
    # 调入程序主界面菜单
    mainmenu()
    # 键盘输入需要操作的选项
    choice = input("请输入您要操作的菜单选项:")
    if len(choice) != 0:  # 输入如果不为空
        choice = input_validation(choice)  # 验证输入是否为数字
        choice = int(choice)
        if choice == 1:
           scode1( str(choice))  # 如果输入大于零的整数，调用scode1()函数生成注册码
        # 选择菜单2,调用scode2()函数生成9位系列产品数字防伪编码
        if choice == 2:
            scode2(choice)
        # 选择菜单3,调用scode3()函数生成25位混合产品序列号
        if choice == 3:
            scode3(choice)
        # 选择菜单4,调用scode4()函数生成含数据分析功能的防伪编码
        if choice == 4:
            scode4(choice)
        # 选择菜单5,调用scode5()函数智能批量生成带数据分析功能的防伪码
        if choice == 5:
            scode5(choice)
        # 选择菜单６,调用scode6()函数后续补加生成防伪码
        if choice == 6:
            scode6(choice)
        # 选择菜单7,调用scode7()函数批量生成条形码
        if choice == 7:
            scode7( choice)
        # 选择菜单8,调用scode8()函数批量生成二维码
        if choice == 8:
            scode8( choice)
        # 选择菜单9,调用scode9()函数生成企业粉丝抽奖程序
        if choice == 9:
            scode9( choice)
        # 选择菜单0,退出系统
        if choice == 0:
            i = 0
            print("正在退出系统!!")
            break
    else:
        print(" 输入非法，请重新输入！！")
        time.sleep(2)

