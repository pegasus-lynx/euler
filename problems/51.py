# from maths.primes import PrimeIterator
# from maths.utils import get_digits, digits_to_num

# end = 100000
# bases = [1, 10, 100, 1000, 10000]
# bases.reverse()

# primes = []
# pset = set()

# found = False
# for p in PrimeIterator():
#     primes.append(p)
#     pset.add(p)
#     if p > end:
#         print(f"End : {end}")
#         for i in range(len(primes)-2, 0, -1):
#             if primes[i] < end // 10:
#                 break

#             freqs = [0] * 10
#             x = p
#             while x != 0:
#                 freqs[x%10] += 1
#                 x = x // 10

#             fd = []
#             for i in range(10):
#                 if freqs[i] == 3:
#                     fd.append(i)

#             if len(fd) == 0:
#                 continue
#             if len(fd) > 1:
#                 print("fd > 1")

#             rd = fd[0]
#             inc = 0
#             digs = get_digits(p)   
#             ixs = []
#             for i,d in enumerate(digs):
#                 if d == rd:
#                     ixs.append(i)
#                     inc += bases[i]

#             ndigs = digs.copy()
#             for i in ixs:
#                 ndigs[i] = 0
#             rp = digits_to_num(ndigs)
#             npcnt = 0
#             for x in range(10):
#                 np = rp + (x*inc)
#                 if np not in pset:
#                     npcnt += 1

#             if npcnt <= 3:
#                 print(p)
#                 found = True
#                 break
#         end *= 10
#         bases = [end//10] + bases
#         if found:
#             break

