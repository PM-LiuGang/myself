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

if __name__ == '__main__':
    print(binary_sum([i for i in range(2,30,3)], 1,9))