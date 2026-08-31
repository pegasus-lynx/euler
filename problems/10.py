import math
from common.timer import start_timer, stop_timer


def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

num = 2000000
ans = 0

start_time = start_timer()
for x in range(2,num):
    if is_prime(x):
        ans += x
stop_timer(start_time, "Problem 10")
print(ans)