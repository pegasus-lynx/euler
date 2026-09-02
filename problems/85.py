

maxn = 2000000
nums = [0]
x = 1
while nums[-1] < maxn:
    nums.append((x*(x+1))//2)
    x += 1

print(len(nums))

diff = maxn
area = 0
for r in range(1,len(nums)):
    for c in range(1, len(nums)):
        nrects = nums[r]*nums[c]
        d = abs(nrects-maxn)
        if d < diff:
            diff = d
            area = r*c

print(area)