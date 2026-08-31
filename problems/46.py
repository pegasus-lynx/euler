import math
from maths.primes import is_prime

primes = [2]

def conforms_goldbach(x, p):
    z = (x-p) // 2
    zsr = int(math.sqrt(z))
    if z == zsr*zsr:
        return True
    return False

x = 1
flag = True
while flag:
    x += 2
    if is_prime(x):
        primes.append(x)
        continue
    is_goldbach = False
    for p in primes:
        _is_goldbach = conforms_goldbach(x,p)
        if _is_goldbach:
            is_goldbach = True
            break
    if not is_goldbach:
        flag = False
        print(x)
