import unittest


class Empty(Exception):
    pass


class DualArrayQueue:

    def __init__(self, maxlen=10):
        self._data = [None] * maxlen
        self._maxlen = maxlen
        self._size = 0
        self._front = 1
        self._back = None

    def is_empty(self):
        return self._size == 0

    def top(self):
        print(self._data[self._front])

    def last(self):
        print(self._data[self._back])

    def get_data(self):
        return self._data

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def clear(self):
        pass

    def rotate(self):
        pass

    def remove(self):
        pass

    def count(self):
        pass

    def add_last(self, e):
        self._back = (self._front + self._size) % len(self._data)
        self._data[self._back] = e
        self._size += 1

    def add_first(self, e):
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
