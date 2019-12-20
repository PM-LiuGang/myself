import math
from Progression import Progression

class ArithmeticProgress(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment
    # R219
    def call_nums(self, target):
        if target % self._increment == 0:
            seconds = (target - self._current) // self._increment
            return seconds
        else:
            seconds = (target - self._current) // self._increment
            return seconds + 1

class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):

    def __init__(self, first=0, seconod=1):
        super().__init__(first)
        self._prev = seconod - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

#C231
class AbsProgression(Progression):

    def __init__(self, first=2, second=200):
        super().__init__(first)  # 这为什么可以继承主类的start？
        self._prev = second + first

    def _advance(self):
        self._prev, self._current = self._current, abs(self._prev - self._current)

# C232
class PowerProgression(Progression):

    def __init__(self, first=65535):
        super().__init__(first)

    def _advance(self):
        self._current = round(math.sqrt(self._current), 4)


if __name__ == '__main__':
    ap1 = ArithmeticProgress(increment=4)
    ap1.print_progression(6)
    # R219
    ap11 = ArithmeticProgress(increment=128)
    print(ap11.call_nums(2**63))

    ap2 = GeometricProgression(base=3)
    ap2.print_progression(6)

    ap3 = FibonacciProgression()
    ap3.print_progression(10)

    # R218
    ap4 = FibonacciProgression(2, 2)
    ap4.print_progression(8)

    ap5 = AbsProgression(2, 200)
    ap5.print_progression(10)

    ap6 = PowerProgression(65536)
    ap6.print_progression(10)