
# x + 2*y + 5*z + 10*w + 20*p + 50*q + 100*r + 200*s = 200
# coeff of (1 + x + x*2 + ... x*200) x (1 + x*2 + x*4 + ... )

coins = [1, 2, 5, 10, 20, 50, 100, 200]

dp = [0 for x in range(201)]
for c in coins:
    if c == 1:
        dp = [1 for x in range(201)]
        continue

    ndp = [0 for x in range(201)]
    ndp[0] = 1

    for i in range(1,201):
        ndp[i] = 0
        for j in range(0,i+1,c):
            ndp[i] += dp[i-j]
    dp = ndp.copy()


print(dp[200])