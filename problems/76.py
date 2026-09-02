
n = 100
dp = [1 for x in range(n+1)]

for x in range(2,n):
    ndp = dp.copy()
    for i in range(x,n+1):
        ndp[i] = sum([dp[i-j] for j in range(0,i+1,x)])
    dp = ndp.copy()

print(dp[n])