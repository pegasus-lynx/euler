
from maths.fibonacci import FibonacciIterator

def count_digits(n):
    cnt = 0
    while n != 0:
        cnt = cnt+1
        n = n // 10
    return cnt

ans = 0
for ix, n in enumerate(FibonacciIterator()):
    cnt = count_digits(n)
    if count_digits(n) == 1000:
        ans = ix
        break

print(ans)