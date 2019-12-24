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

if __name__ == '__main__':
    print(findMaxInerative([i for i in range(8)]))
    print(findMaxInerative([1,22,333,21,44,6,7,8,9]))
    print(findMax([i for i in range(8)]))
    print(findMax([1,22,333,21,44,6,7,8,9]))
