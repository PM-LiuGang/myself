# 4-9

def linear_sum(s, n):
    if n == 0:
        return 0
    else:
        return linear_sum(s, n-1) + s[n-1]

if __name__ == '__main__':
    print(linear_sum([i for i in range(10)], 8))

    