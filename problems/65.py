from fractions import Fraction
from maths.utils import get_digits

e = [2]
for i in range(1,34):
    e.append(1)
    e.append(2*i)
    e.append(1)

e.pop()
e.reverse()

f = Fraction(1,1)
for x in e:
    f = f ** -1
    f += Fraction(x,1)

print(f)
print(sum(get_digits(f.numerator)))