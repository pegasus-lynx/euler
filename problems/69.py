from maths.primes import PrimeIterator
from math import gcd

px = 1
for p in PrimeIterator():
    px *= p
    if px > 1000000:
        break
    phi = 0
    for d in range(1, px+1):
        if gcd(px,d) == 1:
            phi += 1
    tot = px / phi
    print(px, tot)