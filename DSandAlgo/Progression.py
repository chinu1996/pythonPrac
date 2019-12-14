class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current = + 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):
    def __init__(self, base=None, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    print('Arithmetic Progression with increment of 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Geometric Progression with base of 3:')
    GeometricProgression(2).print_progression(10)

    print('Fibonacci series of 10 numbers:')
    FibonacciProgression().print_progression(10)
