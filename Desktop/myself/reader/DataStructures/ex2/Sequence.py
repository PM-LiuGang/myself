from abc import abstractmethod
import abc

# class Sequence(metaclass=ABCMeta):
class Sequence(abc.ABC):

    @abstractmethod
    def __len__(self):
        """
        获取列表长度
        """

    @abstractmethod
    def __getitem__(self, item):
        """
        索引下标读取对应值
        """

    def __contains__(self, item):
        for j in range(len(self)):
            if self[j] == item:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('Value not in sequence.')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        """
        对比两个列表是否完全相同
        """

class myself(Sequence):

    def __init__(self, d):
        self._data = [0] * d

    @staticmethod
    def __len__(self):
        return len(self)

    @staticmethod
    def __getitem__(self, item):
        return self[item]

    # @staticmethod
    def __eq__(self, other):
        if len(self) != len(other):
            raise Exception('Len is not equal.')
        else:
            for i in range(len(self)):
                if self[i] == other[i]:
                    continue
                else:
                    return False
            return True

if __name__ == '__main__':
    l1 = myself(5)
    l2 = myself(5)
    print(l1 == l2)
