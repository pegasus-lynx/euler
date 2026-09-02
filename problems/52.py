

found = False

p = 10
q=16
while not found:
    for d in range(p,q+1):
        flag = True
        s = sorted(str(d))
        for m in range(2,7):
            if s != sorted(str(m*d)):
                flag = False
                break
        if flag:
            found = True
            print(d)
    p *= 10
    q = (q*10)+6