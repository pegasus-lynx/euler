import math
from common.timer import start_timer, stop_timer

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

start_time = start_timer()

nprimes = 0
x = 2
prime = 0

while(nprimes < 10001):
    if(is_prime(x)):
        nprimes = nprimes+1
        prime = x
    x = x+1

print(prime)
stop_timer(start_time, "Problem 7")