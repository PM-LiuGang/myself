class SequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError
        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step -1) // stop)
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        if item < 0:
            item += len(self)

        if not 0 <= item < self._length:
            raise IndexError('Index out of range')

        return self._start + item * self._step

    # C227
    def __contains__(self, item):
        if item % self._step == 0:
            return True
        else:
            return False


# C226
class SequenceIteratorReversed(SequenceIterator):
    def __init__(self, sequence):
        super().__init__(sequence)
        self._k = 0

    def __next__(self):
        self._k -= 1
        if  -1 >= self._k >= -len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration


if __name__ == '__main__':
    r1 = Range(10000000)
    print(2 in r1)

    r2 = Range(10000000)
    print(9999999 in r2)

    r3 = Range(0, 10000000, 333)
    print(333*11 in r3)

    r4 = Range(0, 10000000, 444)
    print(333*11 in r4)

    r5 = SequenceIteratorReversed([n for n in range(5)])
    print(next(r5))
    print(next(r5))
    print(next(r5))