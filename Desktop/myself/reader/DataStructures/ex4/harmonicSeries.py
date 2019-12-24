# R46
# 计算第n个调和级数

def harmonicSeries(n):
    if n == 1:
        return 1/1
    else:
        return 1/n + harmonicSeries(n-1)

if __name__ == '__main__':
    print(harmonicSeries(8))