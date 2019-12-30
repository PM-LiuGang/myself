# 4-3
'''
low high mid
0   15   7
8   15   11
8   10   9
10  10   10
'''
def binary_search(data, target, low, high):
    '''

    :param data: sorted sequence
    :param target:
    :param low:
    :param high:
    :return:
    '''
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False

# 4-13
def binary_sum(s, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(s, start, mid) \
               + binary_sum(s, mid, stop)

# R47
# '12345' to 12345

def str2int(strt):
    mid = 0
    if len(strt) == 0:
        return 0
    elif len(strt) > 1:
        n = len(strt)
        a = int(strt[0])
        for i in range(n-1):
             a *= 10
        mid += a
    elif len(strt) == 1:
        mid += int(strt[0])
    return mid + str2int(strt[1:])
    # return mid + str2int(strt[1:], mid)  错误写法 绘制流程图发现不对

#C416
def reveserdStr(s):
    if len(s) == 0:
        return ''
    else:
        return s[-1] + reveserdStr(s[:-1])

#C417
def hwStrJudge(s, h):
    if reveserdStr(s) == h:
        return True
    else:
        return False

#C418
def aeStrJudge(s, aa=0, nn=0):
    if len(s) == 0:
        return aa > nn
    else:
        if s[0] in ('a','e', 'i', 'o', 'u'):
            aa += 1
        else:
            nn += 1
        return aeStrJudge(s[1:], aa=aa, nn=nn)

#C419

if __name__ == '__main__':
    print(binary_search([i for i in range(10)], 5, 0, 9))
    print(binary_sum([i for i in range(2, 30, 3)], 1, 9))
    print(str2int('1230124')) # 9580468
    print(str2int('998902'))
    print(str2int('120'))

    print('{0:-<20}'.format('C416'))
    print(reveserdStr('pots&pans'))
    print(reveserdStr('pots'))
    print(reveserdStr('12345'))

    print('{0:-<20}'.format('C417'))
    print(hwStrJudge('pots&pans','snap&stop'))

    print('{0:-<20}'.format('C418'))
    print(aeStrJudge('aeioutyghbn'))

