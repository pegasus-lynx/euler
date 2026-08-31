
from maths.factorization import get_divisors
from common.timer import start_timer, stop_timer

start_time = start_timer()
amicable = []
for x in range(2, 10000):
    if x in amicable:
        continue
    y = sum(get_divisors(x))-x
    if x == y:
        continue
    z = sum(get_divisors(y))-y
    if x == z:
        amicable.append(x)
        amicable.append(y)

stop_timer(start_time, "Problem 21")
print(amicable)
print(sum(amicable))