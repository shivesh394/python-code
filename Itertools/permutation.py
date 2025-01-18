from itertools import permutations
# perm = permutations([1, 1, 2, 3, 4])

# for i in list(perm):
#     print("".join(str(list(i))))



# Get all permutations of length 2
perm = permutations([[1, 2], [2, 3], [2, 8]], 2)
# print(list(perm))
for p in list(perm):
	print (p[0], p[1])

