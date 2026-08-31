from maths.primes import is_prime
from maths.utils import get_digits
from maths.primes import PrimeIterator as PI2

class PrimeIterator:
    def __init__(self):
        self._x = 29
        self._arr = [30, 70]
        self._ix = 0
        self._range = 10

    def __iter__(self):
        return self

    def in_range(self):
        return self._x > self._arr[self._ix] and self._x < self._arr[self._ix] + self._range

    def __next__(self):        
        while True:
            self._x = self._x + 2
            if self._x % 5 == 0:
                continue

            if not self.in_range():
                self._ix += 1
                if self._ix == 2:
                    self._arr = [10*x for x in self._arr]
                    self._range *= 10
                    self._ix = 0 
                self._x = self._arr[self._ix] + 1

            if is_prime(self._x):
                break
        return self._x


truncatable = []

def is_truncatable(pdigs):
    x = 0
    for d in pdigs:
        x = x*10 + d
        if x in primes:
            continue
        if not is_prime(x):
            return False
        else:
            primes.add(x)

    x = 0
    for ix, d in enumerate(pdigs[::-1]):
        x += d * pow(10,ix)
        if x in primes:
            continue
        if not is_prime(x):
            return False
        else:
            primes.add(x)

    return True

primes = set([3,7, 13, 17, 31, 37])
for p in PI2():
    primes.add(p)    
    pdigs = get_digits(p)
    if p < 10:
        continue
    if len(pdigs) > 2:
        if (pdigs[0] != 3 and pdigs[0] != 7) or (pdigs[-1] != 3 and pdigs[-1] != 7):
            continue

        flag = True
        for x in pdigs:
            if x % 2 ==0 or x == 5:
                flag = False
                break
        
        if not flag:
            continue
    
    if is_truncatable(pdigs):
        truncatable.append(p)
        print(truncatable)

    if len(truncatable) == 11:
        break

print(truncatable)
print(sum(truncatable))