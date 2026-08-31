from maths.factorization import get_prime_factors
from maths.primes import PrimeIterator

primes = []
for p in PrimeIterator():
    primes.append(p)
    if p > 100000:
        break

x = 207
npfactors = dict()
while True:
    npfac = len(get_prime_factors(x, primes))
    npfactors[x] = npfac
    if npfac == 4:
        if npfactors[x-1] == 4 and npfactors[x-2] == 4 and npfactors[x-3] == 4:
            print(x-3)
            break
    x += 1