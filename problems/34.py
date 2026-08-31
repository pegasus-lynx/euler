
from maths.utils import get_digits
from maths.combinatorics import FactorialIterator

facts = [x for x in FactorialIterator(0,10)]

ans = 0
for x in range(11,10000000):
    digs = get_digits(x)
    fsum = sum([facts[x] for x in digs])
    if fsum == x:
        ans += x

print(ans)
