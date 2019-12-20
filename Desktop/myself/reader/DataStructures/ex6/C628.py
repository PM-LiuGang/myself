class Full(Exception):
    pass


class Empty(Exception):
    pass


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self, maxlen=None):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY  # 指一个固定容量的列表实例
        self._size = 0   # 是一个整数，代表当前储存在队列内的元素的数量，与_data列表的长度正好相对
        self._front = 0  # 是一个整数，代表_data实例队列中的第一个元素的索引，假设这个队列不为空
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""

        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._front]

    def front(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._front

    def dequeue(self):
        """Remove and return the first element of the queue

        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty.')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            print(self._front)
            raise Full('Queue is full.')
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

if __name__ == '__main__':
    aq1 = ArrayQueue()
    for i in range(5):
        aq1.enqueue(i)
    print('unFull~')
    for i in range(11):
        aq1.enqueue(i)
