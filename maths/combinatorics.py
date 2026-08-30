import math

class FactorialIterator:
    def __init__(self, start=0, end=-1):
        self.start = start
        self.end = end
        self.curr = math.factorial(start)
        self.multiplier = start
        self._first = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.multiplier == self.end:
            raise StopIteration
        if self._first:
            self._first = False
            self.multiplier += 1
            return self.curr

        self.curr *= self.multiplier
        self.multiplier += 1
        return self.curr

class PermutationIterator:
    def __init__(self, seq):
        self._seqs = seq.copy()
        self._ix = 0
        self._first = True

    def __iter__(self):
        return self

    def __next__(self):
        if self._first:
            self._first = False
            return self._seqs.copy()

        x = len(self._seqs)-1
        while x >= 0:
            if self._seqs[x-1] > self._seqs[x]:
                x -= 1
                continue
            break
        ix = len(self._seqs)-1
        y = len(self._seqs)
        lmax = max(self._seqs)+1
        while ix >= x:
            if self._seqs[x-1] < self._seqs[ix]:
                if lmax > self._seqs[ix]:
                    lmax = self._seqs[ix]
                    y = ix
            ix -= 1
        self._seqs[x-1], self._seqs[y] = self._seqs[y], self._seqs[x-1]
        self._seqs[x:] = sorted(self._seqs[x:])
        return self._seqs.copy()
