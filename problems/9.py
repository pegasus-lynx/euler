from common.timer import start_timer, stop_timer

start_time = start_timer()

ans = 0
for a in range(1,334):
    for b in range(a+1,1001):
        c = 1000 - (a+b)
        if c <= b:
            break
        x = pow(a,2)+pow(b,2)
        if(pow(c,2)==x):
            ans = a*(b*c)
            break
    if ans != 0:
        break

stop_timer(start_time, "Problem 9")

print(ans)
