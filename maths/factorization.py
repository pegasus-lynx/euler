import math
from maths.primes import PrimeIterator

def get_divisors(x):
    if x == 1:
        return [1]

    divisors = []
    rev_divisors = []
    for d in range(1, int(math.sqrt(x))+1):
        if x % d == 0:
            divisors.append(d)
            if d != x//d:
                rev_divisors.append(x//d)

    rev_divisors.reverse()
    return divisors + rev_divisors

def get_prime_factors(x):
    prime_factors = dict()
    for p in PrimeIterator():
        if x == 1:
            break
        if x % p == 0:
            prime_factors[p] = 0
            while x % p == 0:
                prime_factors[p] += 1
                x = x // p
    return prime_factors

def get_prime_factors(x, primes):
    prime_factors = dict()
    for p in primes:
        if x == 1:
            break
        if x % p == 0:
            prime_factors[p] = 0
            while x % p == 0:
                prime_factors[p] += 1
                x = x // p
    return prime_factors