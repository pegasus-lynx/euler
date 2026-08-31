
from maths.utils import get_digits
from common.timer import start_timer, stop_timer

start_time = start_timer()

nums = set()

for a in range(1,10000):
    a_digits = get_digits(a)
    a_set = set(a_digits)
    if len(a_digits) != len(a_set) or 0 in a_set:
        continue
    
    for b in range(a+1,10000):

        freqs = [0 for x in range(10)]

        b_digits = get_digits(b)
        c_digits = get_digits(a*b)

        for x in a_digits:
            freqs[x] += 1
        for x in b_digits:
            freqs[x] += 1
        for x in c_digits:
            freqs[x] += 1

        is_pand = not freqs[0] != 0
        for x in range(1,10):
            if freqs[x] != 1:
                is_pand = False
                break

        if is_pand:
            nums.add(a*b)


stop_timer(start_time, "Problem 32")
print(sum(list(nums)))