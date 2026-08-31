

def get_recursice_chain(num, den):
    rem = num % den
    rem_chain = []
    while rem != 0 and rem not in rem_chain:
        rem_chain.append(rem)
        rem = rem * 10
        rem = rem % den
    rem_chain.append(rem)
    return rem_chain

ans = 0
maxr = 0
for d in range(2,1000):
    rem_chain = get_recursice_chain(1,d)
    last_rem = rem_chain[-1]
    start = 0
    end = len(rem_chain) - 1
    for i in range(len(rem_chain)):
        if rem_chain[i] == last_rem:
            start = i
            break
    if end-start > maxr:
        ans = d
        maxr = end-start

print(ans)