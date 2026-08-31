
from maths.primes import PrimeIterator, is_prime

# b
# 1 - b = a

def generate_series(n, a, b):
    return pow(n,2) + (a*n) + b

maxn = 0
ans = 0

for b in PrimeIterator():
    if b > 1000:
        break
    for a in range(1-b, 1000):
        n = 0
        while is_prime(generate_series(n,a,b)):
            n += 1
        if n > maxn:
            ans = a*b
            maxn = n

print(ans)
    