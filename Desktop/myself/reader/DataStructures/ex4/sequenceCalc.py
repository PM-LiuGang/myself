# 4-10
# 1 + n/2


def reverse(s, start, stop):
    if start < stop - 1:
        s[start], s[stop - 1] = s[stop - 1], s[start]
        reverse(s, start + 1, stop - 1)
        return s


def reverse_iterative(s):
    start, stop = 0, len(s)
    while start < stop - 1:
        s[start], s[stop - 1] = s[stop - 1], s[start]
        start, stop = start + 1, stop - 1

# 4-9


def linear_sum(s, n):
    if n == 0:
        return 0
    else:
        return linear_sum(s, n - 1) + s[n - 1]

# 4-7
# 4-8


def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)


def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)

# 46


def unique3(s, start, stop):
    # 查找元素是否均唯一
    if stop - start <= 1:
        return True
    elif not unique3(s, start, stop - 1):
        return False
    elif not unique3(s, start + 1, stop):
        return False
    else:
        return s[start] != s[stop - 1]

# R48
# len(s) == 2**n


def sumFun(s, sums=[], i=0):
    if i > len(s) / 2 - 1:
        if i != 1:
            return sums
        elif i == 1:
            return sums[0]
    else:
        sums.append(s[2 * i] + s[2 * i + 1])
        i += 1
    return sumFun(s, sums=sums, i=i)

# R46
# 计算第n个调和级数


def harmonicSeries(n):
    if n == 1:
        return 1 / 1
    else:
        return 1 / n + harmonicSeries(n - 1)

# C419 队列 所有偶数值出现所在奇数值的前面


def joSequence(s, j=[], o=[]):
    if len(s) == 0:
        return o + j
    else:
        if s[0] % 2 == 0:
            o.append(s[0])
        else:
            j.append(s[0])
        return joSequence(s[1:], j=j, o=o)

# C420


def kSequence(s, k, dk=[], xk=[], midk=[]):
    if len(s) == 0:
        return dk + midk + xk
    else:
        if s[0] > k:
            dk.append(s[0])
        elif s[0] < k:
            xk.append(s[0])
        elif s[0] == k:
            midk.append(s[0])
        else:
            raise ('未识别的格式')
        return kSequence(s[1:], 5, dk=dk, xk=xk, midk=midk)

# C421
# s 是递增序列 不包含重复元素


def kSumSequence_iterative(s, k, result=[]):
    for i in range(len(s) - 1):
        if len(s) < 2:
            if s[0] == k:
                result.append(s[0])
            else:
                return result
        else:
            for h in s[1:]:
                if s[0] + h == k:
                    result.append((s[0], h))
                    s.pop(s.index(h))
                    break
            s = s[1:]

# C421
# 遗留问题 连续两次打印后出现关联现象


def kSumSequence(s, k, result=[]):
    if len(s) < 3:
        if s[0] == k:
            result.append(s[0])
        return result
    else:
        oneSumResult = oneSum(s)
        if k in oneSumResult:
            result.append((s[0], k - s[0]))
            s.pop(s.index(k - s[0]))
        return kSumSequence(s[1:], k)

# 用递归实现列表中第一个数与其他的和，输出格式为列表


def oneSum(s):
    # def oneSum(s, result): 这样会出现result叠加的情况
    result_ = []
    initial = s[0]
    for k, v in enumerate(s):
        if k == len(s) - 1:
            break
        else:
            result_.append(initial + s[k + 1])
    return result_


if __name__ == '__main__':
    # print(reverse([i for i in range(10)], 2, 8))
    # print(linear_sum([i for i in range(10)], 8))
    # print(good_fibonacci(10))
    # print(unique3([i for i in range(10)], 0, 9))
    # print(unique3([1,2,3,4,5,1,7,8,9], 0, 8))
    # print(sumFun([1, 2, 3, 7, 8, 9, 10, 11]))
    # print(sumFun([1, 2]))
    # print(harmonicSeries(8))
    #
    # print('{0:-<20}'.format('#C419'))
    # print(joSequence([i for i in range(12)]))
    #
    # print('{0:-<20}'.format('#C420'))
    # print(kSequence([i for i in range(12)] + [5, 5, 5], 5))
    #
    # print('{0:-<20}'.format('#C421'))
    # print(kSumSequence_iterative([i for i in range(11)], 6))
    # print(kSumSequence_iterative([i for i in range(0, 12, 2)], 6))
    # print(kSumSequence_iterative([1,3,4,8,10,11,12,14,15], 18))
    # print(kSumSequence([1,3,4,8,10,11,12,14,15,22], 18))
    print(kSumSequence([1, 3, 4, 8, 10, 11, 12, 14, 15, 18, 22], 18))
    # print(oneSum([i for i in range(10)]))
    # print(oneSum([i for i in range(10)]))
