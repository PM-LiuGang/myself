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

if __name__ == '__main__':
    print(str2int('1230124')) # 9580468
    print(str2int('998902'))
    print(str2int('120'))