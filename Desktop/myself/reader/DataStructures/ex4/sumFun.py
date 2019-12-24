# R48
# len(s) == 2**n
def sumFun(s, sums=[], i=0):
    if i > len(s)/2 - 1:
        if i != 1:
            return sums
        elif i == 1:
            return sums[0]
    else:
        sums.append(s[2*i] + s[2*i + 1])
        i += 1
    return sumFun(s, sums=sums, i=i)

if __name__ == '__main__':
    print(sumFun([1, 2, 3, 7, 8, 9, 10, 11]))
    print(sumFun([1, 2]))