
maxp = 0
sols = 0
for p in range(12,1001):
    cnt = 0
    for a in range(1, p//3 + 1):
        for b in range(a+1, p):
            c = p-(a+b)
            if c < b:
                break
            if (a*a)+(b*b) == c*c:
                cnt += 1
    if cnt > sols:
        sols = cnt
        maxp = p

print(sols, maxp)