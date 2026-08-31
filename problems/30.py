

from maths.utils import get_digits

fifth_powers = [ pow(x,5) for x in range(10)]

ans = 0
for x in range(11, 1000000):
    digits = get_digits(x)
    rsum = sum([fifth_powers[d] for d in digits])
    if rsum == x:
        ans += x

print(ans)