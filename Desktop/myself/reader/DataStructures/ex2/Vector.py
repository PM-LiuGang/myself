import unittest


class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        # return self._coords[key] = value
        self._coords[key] = value

    def dat(self):
        return self._coords

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    # R211
    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree'.title())
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords
        # return self == other

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    # R29
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree'.title())
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    # R210
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __mul__(self, other):
        # R212 C225
        if isinstance(other, int):
            for i in range(len(self)):
                self[i] = self[i] * other
            return self
        # R214
        elif isinstance(other, list):
            if len(self) != len(other):
                raise ValueError('维度不一致'.title())
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other[j]
            return sum(result)
        else:
            raise Exception('未知的数据类型.')

    # R213 C225
    def __rmul__(self, other):
        if isinstance(other, int):
            for i in range(len(self)):
                self[i] = self[i] * other
            return self
        elif isinstance(other, list):
            if len(self) != len(other):
                raise ValueError('维度不一致'.title())
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other[j]
            return sum(result)
        else:
            raise Exception('未知的数据类型.')


class TestVertor(unittest.TestCase):

    def test_add_list(self):
    # def Test_add(self):  error
        v1 = Vector(5)
        v1[2] = 3
        v1[3] = 5
        v2 = Vector(5)
        v2[3] = 4
        v2[4] = 4
        self.assertEqual(v1 + v2, [0,3,9,4,0])

    def test_radd_list(self):
        v1 = Vector(3)
        self.assertEqual([1, 2, 3] + v1, [1, 2, 3])

    def test_mul_int(self):
        v1 = Vector(3)
        for i in range(3):
            v1[i] = i + 1
        self.assertEqual(v1 * 3, [1, 2, 3])

    def test_mul_list(self):
        v1 = Vector(3)
        for i in range(3):
            v1[i] = i + 1
        self.assertEqual(v1 + v1, 12)

    def test_sub(self):
    # def Test_add(self):  error
        v1 = Vector(5)
        v1[2] = 3
        v1[3] = 5
        v2 = Vector(5)
        v2[3] = 4
        v2[4] = 4
        self.assertEqual(v1 - v2, [0,3,1,-4,0])

    def test_dimensions(self):
        v1 = Vector(5)
        v2 = Vector(6)
        with self.assertRaises(ValueError):
            v1 + v2

    def test_neg(self):
        v1 = Vector(5)
        for i in range(5):
            v1[i] = i
        self.assertEqual(-v1, [0, -1, -2, -3, -4])


if __name__ == '__main__':
    unittest.main()