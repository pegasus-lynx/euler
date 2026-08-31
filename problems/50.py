
from maths.primes import PrimeIterator, is_prime


primes = []
for p in PrimeIterator():
    if p > 1000000:
        break
    primes.append(p)

pre = [0] * len(primes)
pre[0] = primes[0]

for i in range(1, len(primes)):
    pre[i] = pre[i-1] + primes[i]

pre = [0] + pre
pset = set(primes)

slen = 6
maxp = 0
for p in range(len(pre)):
    if p + slen + 1 >= len(pre):
        break

    q = p + slen + 1
    while q < len(pre):
        diff = pre[q]-pre[p]
        if diff not in pset:
            q += 1
            continue
        slen = q-p
        maxp = diff
        print(p, q, slen, maxp)
        q += 1

print(maxp) 