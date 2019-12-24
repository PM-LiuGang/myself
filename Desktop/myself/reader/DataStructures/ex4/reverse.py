# 4-10
# 1 + n/2
def reverse(s, start, stop):
    if start < stop - 1:
        s[start], s[stop-1] = s[stop-1], s[start]
        reverse(s, start+1, stop-1)
        return s

def reverse_iterative(s):
    start, stop = 0, len(s)
    while start < stop - 1:
        s[start], s[stop-1] = s[stop-1], s[start]
        start, stop = start + 1, stop - 1
        
if __name__ == '__main__':
    print(reverse([i for i in range(10)], 2, 8))
