# 4-6
import timeit

def unique3(s, start, stop):
    if stop - start <= 1:
        return True
    elif not unique3(s, start, stop -1):
        return False
    elif not unique3(s, start+1, stop):
        return False
    else:
        return s[start] != s[stop - 1]

if __name__ == '__main__':
    # timeit.repeat("unique3([i for i in range(10)], 0, 9)", repeat=2, number=1000)
    print(unique3([i for i in range(10)], 0, 9))