# -*-coding:utf8-*-
# 求代数多项式的一阶导数
# 标准输入：75x^4+5x^2+1
# 预期输出：300x^3+10x
import re
import unittest

# numlist = []

def strsplit(s):
    fuhaolist = []
    numlist = []
    for i in s:
        if i == '+' or i == '-':
            fuhaolist.append(i)
    # review 这是冗余严重代码 - 19.12.19
    # if '+' in s or '-' in s:
    #     for i in [i.strip() for i in re.split('[+-]', s)]:
    #         if i == '+' or i == '-':
    #             fuhaolist.append(i)
    #         else:
    #             numlist.append(i)
    # else:
    #     numlist = [s]
    numlist = [i.strip() for i in re.split('[+-]', s)]
    return fuhaolist, numlist

def derivation(s):
    fuhaolist, numlist = strsplit(s)
    # fuhaolist.append('')
    result = ''
    processlist = []
    for i in numlist:
        index = i.find('^')
        if index != -1:                              # 找到含有平方的代数式
            mi = int(i[index+1:]) - 1
            xishu = int(i[ :index-1]) * int(i[index+1: ])
            processlist.append(str(xishu)  + 'x^' + str(mi))
        elif index == -1:
            if i.find('x') == -1:
                continue
            elif i.find('x') != -1:
                index_1 = i.find('x')
                processlist.append(i[ :index_1])
        else:
            raise Exception('多项式中存在异常格式的代数式.')

    if  len(fuhaolist) == 0:
        fuhaolist.append('')

    for z, k in zip(processlist, fuhaolist):
        result = result + z
        result = result + k
    # result = result.rstrip('+')
    result = result.strip('+')
    result = result.strip('-')
    return result  # 这个千万不能忘记


class TestPoly(unittest.TestCase):

    def test_strsplit(self):
        self.assertEqual(strsplit('14x^15'),([], ['14x^15']))

    def test_strsplit_1(self):
        self.assertEqual(strsplit('14x^15+3x^3-2x+1'),(['+', '-', '+'], ['14x^15','3x^3','2x','1']))

    def test_strsplit_2(self):
        self.assertEqual(strsplit('14x^15+1'), (['+'], ['14x^15', '1']))

    def test_derivation_1(self):
        self.assertEqual(derivation('14x^15+3x^3-2x+1'),'210x^14+9x^2-2')

    def test_derivation_2(self):
        self.assertEqual(derivation('14x^15'),'210x^14')

    def test_derivation_3(self):
        self.assertEqual(derivation('14x^15+1'),'210x^14')

    def test_derivation_4(self):
        self.assertEqual(derivation('1'),'')


if __name__ == '__main__':
    unittest.main()