# import math

pnums = dict()
inv_pnums = dict()
pnums[0] = 0
pnums[1] = 2
pnums[2] = 10
inv_pnums[0] = 0
inv_pnums[2] = 1
inv_pnums[10] = 2
pnset = set([0,2,10])

def get_pentagonal_number(k):
    if k in pnums.keys():
        return pnums[k]
    pnums[k] = k * ((3*k)-1)
    return pnums[k]

n = 3
flag = True
ans = 10000000000000000000000
while flag:
    pnset.add(get_pentagonal_number(n))
    inv_pnums[pnums[n]] = n
    for i in range(n-1,1,-1):
        diff = pnums[n] - pnums[i]
        if diff >= pnums[i]:
            break
        if diff not in pnset:
            continue
        diff2 = pnums[i] - diff
        if diff2 not in pnset:
            continue
        if diff2 < ans:
            ans = diff2
            print(ans//2)
    n += 1
