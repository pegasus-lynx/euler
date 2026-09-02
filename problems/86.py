import math



# def count_sols(M):
#     cnt = 0
#     for a in range(1,M+1):
#         for b in range(a,M+1):
#             for c in range(b,M+1):
#                 sqs = pow(c,2)+pow(a+b,2)
#                 h = int(math.sqrt(sqs))
#                 if h*h == sqs:
#                     cnt += 1
#     return cnt

def count_sols(M):
    cnt = 0
    sols = []
    for c in range(1,M+1):
        for ab in range(2,(2*c)+1):
            sqs = pow(c,2)+pow(ab,2)
            h = int(math.sqrt(sqs))
            if h*h == sqs:
                sols.append((c,ab)) 
                if ab <= c:
                    cnt += (ab // 2)
                else:   
                    cnt += c-((ab-1)//2)
    return cnt

print("M =", 99, count_sols(99))
print("M =", 100, count_sols(100))


ms = []
m = 100
sols = 0
msol = 1000000

while sols < msol:
    sols = count_sols(m)
    ms.append(m)
    m *= 10

st = ms[-2]
en = ms[-1]

while st < en:
    mid = (st+en) // 2
    sol = count_sols(mid)
    print(st, en, mid, sol)
    if sol < msol:
        st = mid
    elif sol > msol:
        en = mid
    else:
        st = mid
        break

    if en-st == 1:
        break

print(st,en)
