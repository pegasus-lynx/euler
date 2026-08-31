
from maths.combinatorics import PermutationIterator

for ix, x in enumerate(PermutationIterator([0,1,2,3,4,5,6,7,8,9])):
    if ix + 1 == 1000000:
        print(x)
        break