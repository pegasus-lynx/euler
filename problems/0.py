
def squares(x):
    return x*x

ans = 0
for i in range(1,196000):
    sq = squares(i)
    if sq % 2 == 1:
        ans += sq

print(ans)