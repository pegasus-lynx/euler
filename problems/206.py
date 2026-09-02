from maths.utils import get_digits
import math

p = 101010103  # int(math.sqrt(10203040506070809))
q = int(math.sqrt(19293949596979899))

while p < q:
    psq = p*p
    digs = get_digits(psq)
    found = True
    for i in range(0,len(digs),2):
        if digs[i] != (i//2)+1:
            found = False
            break
    if found:
        print(p)
        break
    p += 4 if p%10 == 3 else 6

print(p*p)