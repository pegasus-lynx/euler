
num = 1
base = 2
p = 7830457
mod = pow(10,10)

while p > 1:
    if p % 2 == 1:
        num *= base
        num = num % mod
    base = base*base
    base = base % mod
    p = p // 2

num = (num*base) % mod
num = (num*28433) % mod
num += 1

print(num)