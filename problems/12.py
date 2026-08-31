from common.timer import start_timer, stop_timer
import math

class TriangleNumberIterator:
    def __init__(self, num):
        self.num = num
        self.x = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.x >= self.num:
            raise StopIteration
        ret = (self.x * (self.x+1)) // 2
        self.x += 1
        return ret

def factors_count(x):
    if x == 1:
        return 1
    cnt = 0
    for d in range(1,int(math.sqrt(x))+1):
        if x % d == 0:
            if d < x//d:
                cnt = cnt + 2
            else:
                cnt = cnt + 1
    return cnt

start_time = start_timer()
ans = 0
for x in TriangleNumberIterator(1000000):
    if factors_count(x) > 500:
        ans = x
        break
stop_timer(start_time, "Problem 12")
print(ans) 