from maths.utils import get_digits

def is_bouncy(digs):
    pos = 0
    neg = 0
    for i in range(len(digs)-1):
        d = digs[i+1]-digs[i]
        if d > 0:
            pos += 1
        elif d < 0:
            neg += 1
        if pos > 0 and neg > 0:
            return True
    return False
   

bouncy = 0
x = 101
while bouncy * 100 != (x-1) * 99:
    digs = get_digits(x)
    if is_bouncy(digs):
        bouncy += 1
    x += 1

print(x-1)