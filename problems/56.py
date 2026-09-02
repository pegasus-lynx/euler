from maths.utils import get_digits

maxdsum = 0

for a in range(1,100):
    prod = 1
    for b in range(1,100):
        prod *= a
        dsum = sum(get_digits(prod))
        if dsum > maxdsum:
            maxdsum = dsum

print(maxdsum)