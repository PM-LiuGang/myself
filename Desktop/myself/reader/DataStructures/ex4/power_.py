# 4-11
# 调用 n 次
def power_(x, n):
    if n == 0:
        return 1
    else:
        return x * power_(x, n-1)
# 调用 n/2 + 1 or n/2
def power_1(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return ((power_1(x, n/2))**2)
    elif n % 2 != 0:
        return x * (power_1(x, (n-1)/2))**2
    else:
        print('Unknow Format or n < 0')
# 与 power_1调用次数相同
def power_2(x, n):
    if n == 0:
        return 1
    else:
        partial = power_2(x, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= x
        return result

#C422
def power_3(n):
# def power_3(n, x=2): 错误写法
    x = 2
    for i in range(n - 1):
        x *= 2
    print(x)

if __name__ == '__main__':
    # print(power_(2, 5))
    # print(power_1(2, 5))
    # print(power_1(2, 6))
    # print(power_2(2,5))
    # print(power_2(2, 6))
    print('{0:-<20}'.format('#C422'))
    power_3(5)
    power_3(10)