
from maths.primes import PrimeIterator

primes = []

for p in PrimeIterator():
    if p < 1000:
        continue
    if p > 9999:
        break
    primes.append(p)

found = 0
for j in range(1, len(primes)-1):
    i = j-1
    k = j+1
    while i >-1 and k < len(primes):
        if primes[i] + primes[k] == 2*primes[j]:
            i_str = sorted(str(primes[i]))
            j_str = sorted(str(primes[j]))
            k_str = sorted(str(primes[k]))
            if i_str == j_str and j_str == k_str:
                print(primes[i],primes[j],primes[k])
                found += 1
            i -= 1
            k += 1
        elif primes[j]-primes[i] < primes[k]-primes[j]:
            i -= 1
        else:
            k += 1

        if found == 2:
            break
    if found == 2:
        break