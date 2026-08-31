
from maths.fibonacci import FibonacciIterator

ans = 0
for n in FibonacciIterator():
    if n >= 4000000:
        break
    if n % 2 == 0:
        ans += n

print(ans)