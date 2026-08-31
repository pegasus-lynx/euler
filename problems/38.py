from maths.utils import get_digits

ans = 0

def is_pandigital(s):
    if len(s) != 9:
        return False
    x = int(s)
    xdigs = get_digits(x)
    freqs = [0 for i in range(10)]
    for p in xdigs:
        freqs[p] += 1
    if freqs[0] != 0:
        return False
    for i in range(1,10):
        if freqs[i] != 1:
            return False
    return True

# n = 2
for x in range(5000,10000):
    s = ""
    for i in range(1,3):
        s += str(x*i)
        if is_pandigital(s):
            ans = max(ans, int(s))
    
# n = 3
for x in range(100,334):
    s = ""
    for i in range(1,4):
        s += str(x*i)
        if is_pandigital(s):
            ans = max(ans, int(s))

# n = 4 
for x in range(25, 34):
    s = ""
    for i in range(1,5):
        s += str(x*i)
        if is_pandigital(s):
            ans = max(ans, int(s))

# n = 5
for x in range(5,10):
    s = ""
    for i in range(1,6):
        s += str(x*i)
        if is_pandigital(s):
            ans = max(ans, int(s))

print(ans)