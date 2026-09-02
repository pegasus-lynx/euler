from fractions import Fraction
from maths.utils import get_digits

cnt = 0
f = Fraction(3,2)
for i in range(1,1000):
    t = Fraction(1,1) + f
    t = t ** -1
    f = Fraction(1,1) + t
    if len(get_digits(f.numerator)) > len(get_digits(f.denominator)):
        cnt += 1

print(cnt)