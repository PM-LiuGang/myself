import unittest


class Empty(Exception):
    pass


class DualArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * DualArrayQueue.DEFAULT_CAPACITY  # 指一个固定容量的列表实例
        self._size = 0  # 是一个整数，代表当前储存在队列内的元素的数量，与_data列表的长度正好相对
        self._front = 1  # 是一个整数，代表_data实例队列中的第一个元素的索引，假设这个队列不为空
        self._back = None

    def is_empty(self):
        return self._size == 0

    def get_data(self):
        return self._data

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._back = (self._front + self._size) % len(self._data)
        self._data[self._back] = e
        self._size += 1

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def del_last(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        answer = self._data[self._back]
        self._data[self._back] = None
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer

    def del_first(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


class TestDualQueue(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_add(self):
        das = DualArrayQueue()
        for i in range(4):
            das.add_first(i)
        for i in 'liu':
            das.add_last(i)
        self.assertEqual(
            das.get_data(), [
                0, 'l', 'i', 'u', None, None, None, 3, 2, 1])

    def test_add_full(self):
        das = DualArrayQueue()
        for i in range(5):
            das.add_first(i)
        for i in 'liugang':
            das.add_last(i)
        # self.assertEqual(das.get_data(),[0, 'l', 'i', 'u', 'g', 'a', 'n',4 ,3 ,2, 1])
        self.assertEqual(das.get_data(),
                         [4,
                          3,
                          2,
                          1,
                          0,
                          'l',
                          'i',
                          'u',
                          'g',
                          'a',
                          'n',
                          'g',
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None])

    def test_del(self):
        das = DualArrayQueue()
        for i in range(4):
            das.add_first(i)
        for i in 'liu':
            das.add_last(i)
        das.del_first()
        das.del_last()
        self.assertEqual(
            das.get_data(), [
                0, 'l', 'i', None, None, None, None, None, 2, 1])

    def test_empty(self):
        das = DualArrayQueue()
        for i in range(4):
            das.add_first(i)
        for i in range(4):
            das.del_first()
        with self.assertRaises(Empty):
            das.del_first()


if __name__ == '__main__':
    unittest.main()
