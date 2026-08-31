from common.timer import start_timer, stop_timer
import math

collatz = dict()
collatz[1] = 1
collatz[2] = 2

def get_collatze_len(x):
    cnt = 0
    orig = x    
    while x != 1:
        if x in collatz:
            collatz[orig] = cnt + collatz[x]
            return collatz[orig]
        
        cnt = cnt+1
        if x % 2 == 0:
            x = x//2
        else:
            x = (3*x)+1
        
    collatz[orig] = cnt
    return collatz[orig]

start_time = start_timer()
ans = 2
mlen = 2
for x in range(3,1000000):
    l = get_collatze_len(x)
    if l > mlen:
        ans = x
        mlen = l
stop_timer(start_time, "Problem 14")
print(ans)