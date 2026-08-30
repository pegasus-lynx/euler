import math

class PrimeIterator:
    def __init__(self):
        self._x = 2
        self._is_first = True
        self._is_second = True

    def __iter__(self):
        return self

    def __next__(self):
        if self._is_first:
            self._is_first = False
            return self._x

        if self._is_second:
            self._is_second = False
            self._x += 1
            return self._x

        r = 2
        while not is_prime(self._x + r):
            r += 2
        self._x += r
        return self._x


def is_prime(x):
    if x<1:
        return False
        
    for p in range(2, int(math.sqrt(x))+1):
        if x % p == 0:
            return False
    return True