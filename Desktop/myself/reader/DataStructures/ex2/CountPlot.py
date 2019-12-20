# P224

import matplotlib.pyplot as plt
from collections import Counter

file = 'Vector.py'

def count_freq(s):
    n = 0
    result = []
    fc = open(s, encoding='utf8').read()    # 别忘记加encoding
    fn = Counter(fc).most_common(50)
    for i in fn:                            # 如果不用most common，应该用fn.items()
        if i[0].isalpha():                  # 判断是字母，不区分大小写
            result.append(i)
            n += 1
            if n > 15:
                break
    return result

def freq_plot(s):
    plt.bar([i[0] for i in s], [i[1] for i in s], width=.5)  # plt.bar(list, list, weights)
    plt.show()

if __name__ == '__main__':
    result = count_freq(file)
    freq_plot(result)