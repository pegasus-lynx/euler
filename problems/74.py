from maths.utils import get_digits
from math import factorial

fac_sum = dict()
fac_chain = dict()

for i in range(1,10000000):
    fac_sum[i] = sum(list(map(factorial, get_digits(i))))
    if i < 100:
        print(i, fac_sum[i])


cnt = 0
for x in range(1,1000000):
    chain = [x]
    nx = x
    for i in range(60):
        nx = fac_sum[nx]
        if nx in chain:
            chain.append(x)
            break
        chain.append(nx)
    if len(chain) == 61:
        cnt += 1

print(cnt)