
n = 100

ans = pow(((n*(n+1))//2),2)
for i in range(1,n+1):
    # print(i)
    ans = ans - pow(i,2)

print(ans)