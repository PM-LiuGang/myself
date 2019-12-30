# C410

def func3(n, c=0):
    if n / 2 <= 1:
        return c + 1  # 这必须加1，因为需要除以2后计算
    else:
        return func3(n / 2, c + 1)

# review
def logDiv(n, result=0):
    if n == 0:
        return 0
    elif n / 2 <= 1:
        result += 1
        return result
    else:
        n = n/2
        result += 1
        return logDiv(n, result=result)
# C412 review
def asMul(m, n):
    if not isinstance(m, int) and isinstance(n, int):
        raise '请检查格式'
    elif n == 0:
        return 0
    else:
        return m + asMul(m, n-1)

if __name__ == '__main__':
    print(logDiv(12))
    print(logDiv(20))
    print(logDiv(0))
    print(asMul(3, 5))

