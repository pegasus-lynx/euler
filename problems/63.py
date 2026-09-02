from maths.utils import get_digits

cnt = 0
n = 1
while True:
    inc = False
    for d in range(1, 10):
        x = pow(d,n)
        digs = get_digits(x)
        if len(digs) == n:
            inc = True
            cnt += 1
    if not inc:
        break 
    n += 1

print(cnt)   