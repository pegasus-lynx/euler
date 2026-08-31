

pos = 1
slen = 0
ans = 1

for x in range(1,1000001):
    s = str(x)
    for i, c in enumerate(s):
        if slen+i+1 == pos:
            pos *= 10
            ans = ans*int(c)
            if pos == 10000000:
                break

    slen += len(s)
    if pos == 10000000:
        break

print(ans)

