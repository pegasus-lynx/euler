


class FibonacciIterator:
    def __init__(self):
        self._f0 = -1
        self._f1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        ret = self._f0 + self._f1
        self._f0 = self._f1
        self._f1 = ret
        return ret