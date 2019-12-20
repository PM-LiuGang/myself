class Full(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Empty(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY  # 指一个固定容量的列表实例
        self._size = 0  # 是一个整数，代表当前储存在队列内的元素的数量，与_data列表的长度正好相对
        self._front = 0  # 是一个整数，代表_data实例队列中的第一个元素的索引，假设这个队列不为空
        # myself
        self._back = 0  # int, 代表_data队列中的最后一个元素的索引

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._front]

    # myself
    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._back]

    def back(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._back

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
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        #         self._back = (len(self._data) - self._size + 1) len(self._data)
        self._back = (self._front + self._size - 1) % len(self._data)

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0