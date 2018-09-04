import bisect
import random

# 往已排序的列表插入新值，而不影响列表的已排序

SIZE = 7
random.seed(1729)

my_list = []

for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d -> ' % new_item, my_list)
