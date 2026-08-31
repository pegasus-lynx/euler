from maths.utils import get_digits, digits_to_num
from maths.combinatorics import PermutationIterator

# d4 is even
# d3+d4+d5 % 3 == 0
# d6 is 0 or 5
# d6+d8 - d7 % 11 == 0

total = 10*9*8*7*6*5*4*3*2*1
divisibility = { 7:17, 6:13, 5:11, 4:7, 3:5, 2:3, 1:2, 0:1 }

nums = []
for i, seq in enumerate(PermutationIterator([0,1,2,3,4,5,6,7,8,9])):
    if i == total:
        break
    flag = True
    for pos in range(7,-1,-1):
        x = digits_to_num(seq[pos:pos+3])
        if x % divisibility[pos] != 0:
            flag = False
            break
    if flag:
        nums.append(digits_to_num(seq))
        print(nums[-1])

print(sum(nums))
