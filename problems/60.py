from maths.primes import PrimeIterator
from maths.utils import get_digits

mr1 = [3]
mr2 = [3]
mr1set = set([3])
mr2set = set([3])

for p in PrimeIterator():
    if p < 6:
        continue
    if p > 10000000:
        break
    if p % 3 == 1:
        mr1.append(p)
        mr1set.add(p)
    else:
        mr2.append(p)
        mr2set.add(p)

mr1pairs = []
for i in range(len(mr1set)):
    for j in range(i+1, len(mr1set)):
