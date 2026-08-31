
tnums = dict()
pnums = dict()
hnums = dict()

def get_tnum(x):
    if x in tnums:
        return tnums[x]
    tnums[x] = (x * (x+1)) // 2
    return tnums[x]

def get_pnum(x):
    if x in pnums:
        return pnums[x]
    pnums[x] = (x * ((3*x)-1)) // 2
    return pnums[x]

def get_hnum(x):
    if x in hnums:
        return hnums[x]
    hnums[x] = x * ((2*x)-1)
    return hnums[x]

c = 143
b = 165
cflag = True
while cflag:
    c += 1
    a = (2*c) -1
    hnum = get_hnum(c)
    bflag = True
    while bflag:
        b += 1
        pnum = get_pnum(b)
        if pnum == hnum:
            cflag = False
            bflag = False
            break
        if pnum > hnum:
            b -= 1
            break
print(get_tnum(a))