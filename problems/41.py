
from maths.combinatorics import PermutationIterator
from maths.utils import digits_to_num
from maths.primes import is_prime
from math import factorial

hprime = -1
for n in range(7,6,-1):
    if hprime != -1:
        break
    seq = [x for x in range(1,n+1)]
    for ix, p in enumerate(PermutationIterator(seq)):
        if ix == factorial(n):
            break
        num = digits_to_num(p)
        if is_prime(num):
            hprime = max(hprime, num)

print(hprime)