from maths.factorization import get_divisors
from common.timer import start_timer, stop_timer

abundants = []

for x in range(1,28124):
    if sum(get_divisors(x)) > 2*x:
        abundants.append(x)

sabu = set()
for x in abundants:
    for y in abundants:
        if x+y > 28123:
            continue
        sabu.add(x+y)


ans = 0
for x in range(1, 28124):
    if x not in sabu:
        ans += x

print(ans)