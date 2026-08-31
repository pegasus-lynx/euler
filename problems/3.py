
num = 600851475143

pf = []

for p in range(2,num):
    if num == 1:
        break
    
    if num % p == 0:
        pf.append(p)
        while num % p == 0:
            num = num / p

print(pf[-1])