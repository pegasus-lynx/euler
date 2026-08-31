from maths.primes import PrimeIterator, is_prime
from maths.utils import get_digits, digits_to_num

def rotate(digs):
    digs.append(digs[0])
    return digs[1:]

cnt = 0
primes = set()
for x in PrimeIterator():
    if x >= 1000000:
        break
    
    if x < 10:
        cnt += 1
        continue

    digs = get_digits(x, True)
    ndigs = len(digs)
    is_circular = True
    
    for d in digs:
        if d % 2 == 0 or d == 5:
            is_circular = False
            break

    if not is_circular:
        continue

    for i in range(ndigs-1):
        digs = rotate(digs)
        rnum = digits_to_num(digs, True)
        if not is_prime(rnum):
            is_circular = False
            break

    if is_circular:
        cnt += 1

print(cnt)