from maths.combinatorics import FactorialIterator

facts = [x for x in FactorialIterator(0,101)]

cnt = 0
for n in range(1,101):
    if facts[n] < 1000000:
        continue
    for r in range(n+1):
        if r > n-r:
            break

        comb = facts[n] // (facts[r]*facts[n-r])
        if comb > 1000000:
            if r < n-r:
                cnt += 2
            else:
                cnt += 1

print(cnt)