

ans = 0

for x in range(1,1000000):
    s = str(x)
    b = bin(x)[2:]
    rs = s[::-1]
    rb = b[::-1]

    if s == rs and b == rb:
        ans += x

print(ans)