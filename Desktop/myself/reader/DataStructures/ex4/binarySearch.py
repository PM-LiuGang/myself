# 4-3
'''
low high mid
0   15   7
8   15   11
8   10   9
10  10   10
'''
def binary_search(data, target, low, high):
    '''

    :param data: sorted sequence
    :param target:
    :param low:
    :param high:
    :return:
    '''
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False

if __name__ == '__main__':
    print(binary_search([i for i in range(10)], 5, 0, 9))