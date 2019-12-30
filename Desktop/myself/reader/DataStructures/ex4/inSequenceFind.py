# R41

def findMax(sequence, maxSequence=0):
    # if len(sequence) != 0 :
    #     if maxSequence < sequence[0]:
    #         maxSequence = sequence[0]
    #     findMax(sequence[1:], maxSequence=maxSequence) # 这一定不要忘记加入return，不然出现返回值是None的情况
    # else:
    #     return result

    if len(sequence) != 0 :
        if maxSequence < sequence[0]:
            maxSequence = sequence[0]
        return findMax(sequence[1:], maxSequence=maxSequence)
    else:
        return maxSequence

def findMaxInerative(seq):
    n = seq[0]
    for i in range(len(seq) - 1):
        if n >= seq[i+1]:
            pass
        elif n < seq[i+1]:
            n = seq[i+1]
    return n

# C415 三角
# [] + [1] = [1]
# extend的用法
# items=[5] item[1]->error item[1:]->[]
def findSubSet_inerative(items):
    # 空集的默认有一个空集元素
    result = [[]]
    for x in items:
        result.extend([subset + [x] for subset in result])
    return result

def findSubSet(items):
    if len(items) == 0:
        # 如果列表是空的，返回空集
        return [[]]

    subsets = []
    first_elt = items[0]  # 第一个元素
    rest_list = items[1:]  # 这剩一个元素的时候不会报错么

    for partial_sebset in findSubSet(rest_list):
        subsets.append(partial_sebset)
        next_subset = partial_sebset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets


if __name__ == '__main__':
    print(findMaxInerative([i for i in range(8)]))
    print(findMaxInerative([1,22,333,21,44,6,7,8,9]))
    print(findMax([i for i in range(8)]))
    print(findMax([1,22,333,21,44,6,7,8,9]))
    print(findSubSet_inerative([1,2,3,4]))
    print(findSubSet([1, 2, 3, 4, 5]))