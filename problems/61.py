

# quad_nums = dict()
# for i in range(3,9):
#     quad_nums[i] = [0 for x in range(201)]

# def get_quad_number(type, n):
#     if quad_nums[type][n] != 0:
#         return quad_nums[type][n]

#     if type == 3:
#         quad_nums[type][n] = (n*(n+1)) // 2
#     elif type == 4:
#         quad_nums[type][n] = n*n
#     elif type == 5:
#         quad_nums[type][n] = (n*((3*n)-1)) // 2
#     elif type == 6:
#         quad_nums[type][n] = n*((2*n)-1)
#     elif type == 4:
#         quad_nums[type][n] = (n*((5*n)-1)) // 2
#     else:
#         quad_nums[type][n] = n*((3*n)-1)

#     return quad_nums[type][n]

# def find_next_quad(nums, l2, used, types):
#     if sum(used) == 6:
#         nx = (l2[-1]*100) + l2[0]
#         if nx in nums:
#             return True
#         return False

#     found = False
#     for x in range(100):
#         nx = (l2[-1]*100) + x
#         for i in range(6):
#             if used[i] == 1:
#                 continue
#             t = i + 3
#             if nx not in quad_nums[t]:
#                 continue
#             nums.append(nx)
#             l2.append(nx%100)
#             used[i] = 1
#             types.append(t)
#             found = find_next_quad(nums, l2, used, types)
#             if found:
#                 return True
#             nums.pop()
#             l2.pop()
#             types.pop()
#             used[i] = 0
#     return False

# ## Populate the quad numbers
# for t in range(3,9):
#     for n in range(1,200):
#         get_quad_number(t,n)

# for o in quad_nums[8]:
#     if o<1000 or o>9999:
#         continue
#     nums = [o]
#     l2 = [o % 100]
#     types = [8]
#     used = [0 if i<5 else 1 for i in range(6)]
#     found = find_next_quad(nums, l2, used, types)
#     if found:
#         for num in nums:
#             if num < 1000 or num > 9999:
#                 found = False
#                 break
#     if found:
#         print(nums, types, sum(nums))