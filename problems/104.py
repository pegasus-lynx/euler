from maths.fibonacci import FibonacciIterator
from maths.utils import get_digits
from common.timer import start_timer, stop_timer

time = start_timer()
maxn = pow(10,9)
maxnn = pow(10,18)

for ix,f in enumerate(FibonacciIterator()):

    if ix % 500 == 0:
        print(f"Current Index : {ix}")

    if f < maxnn:
        continue

    is_pand = True
    freqs = [0] * 10
    l10 = f % maxn
    while l10 != 0:
        d = l10 % 10
        freqs[d] += 1
        if d==0 or freqs[d] > 1:
            is_pand = False
            break
        l10 = l10 // 10

    if not is_pand:
        continue

    fc = f
    rc = 0
    while fc > maxn:
        rc = fc % maxn
        fc = fc // maxn

    digs = get_digits((fc*maxn)+rc, reversed_list=True)
    l = len(digs)-1
    for i in range(9):
        d = digs[l-i]
        freqs[d] += 1
        if d==0 or freqs[d] > 2:
            is_pand = False
            break
    
    if not is_pand:
         continue

    print(ix)
    break

stop_timer(time, "Problem 104")