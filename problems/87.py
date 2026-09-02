from maths.primes import PrimeIterator

maxn = 50000000
psqs = dict()
pcbs = dict()
pfts = dict()

for p in PrimeIterator():
    sq = p*p
    if sq > maxn:
        break
    psqs[p] = sq
    cb = sq*p
    if cb > maxn:
        continue
    pcbs[p] = cb
    ft = cb*p
    if ft > maxn:
        continue
    pfts[p] = ft

psums = set()
for f in pfts.values():
    for c in pcbs.values():
        for s in psqs.values():
            psum = f+c+s
            if psum < maxn:
                psums.add(psum)

print(len(psums))