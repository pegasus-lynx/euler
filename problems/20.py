
x = 1

for i in range(1,101):
    x = x*i

ans = 0
while x!=0:
    ans = ans + (x%10)
    x = x//10

print(ans)