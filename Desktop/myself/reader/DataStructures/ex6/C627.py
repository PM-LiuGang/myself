# from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

def scan_element(s, as1):
    for i in range(len(as1)):
        h = as1.pop()
        if h == s:
            print('s-elemnt"index is {}'.format(i))
            as1.push(h)
            return True
        else:
            as1.push(h)
    return False

if __name__ == '__main__':
    as1 = ArrayStack()
    for i in 'liuganx':
        as1.push(i)
    scan_element('g', as1)
    print(as1._data)
