import math

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