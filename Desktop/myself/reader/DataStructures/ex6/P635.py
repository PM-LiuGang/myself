import unittest


class Full(Exception):
    pass


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen=12):
        """Create an empty stack."""
        self._data = []
        self._maxlen = maxlen

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def get_data(self):
        return self._data

    def push(self, e):
        if len(self._data) == self._maxlen:
            self._data.pop(0)
            self._data.append(e)
        else:
            self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()


class TestStack(unittest.TestCase):

    def test_push(self):
        as635 = ArrayStack()
        for i in range(12):
            as635.push(i)
        as635.push('liugang')
        self.assertEqual(as635.get_data(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'liugang'])


if __name__ == '__main__':
    unittest.main()
