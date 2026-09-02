from maths.primes import is_prime

x = 1
l = 1
pcnt = 0
dcnt = 1
flag = True
while flag:
    l += 2
    for i in range(4):
        x += (l-1)
        if is_prime(x):
            pcnt += 1
        dcnt += 1
    if l > 7:
        if pcnt * 10 < dcnt:
            flag = False

print(l)