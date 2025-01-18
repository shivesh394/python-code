l1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
l2 = [2, 1, 8, 3]
k = 0

# for l in l2 :
#     for j in range(len(l1)):
#         if l1[j]  == l:
#             l1[k], l1[j] = l1[j], l1[k]
#             k += 1

# l1[:] = l1[:k] + sorted(l1[k:])
# print(l1)


m = {}


for l in l1:
    if l not in m:
        m[l] = 1
    else:
        m[l] += 1


for l in l2:
    for i in range(m[l]):
        l1[k] = l
        k += 1
    del m[l]

l3 = []
for i in m:
    for j in range(m[i]):
        l3.append(i)
l3.sort()

for i in range(len(l3)):
    l1[k + i] = l3[i] 
print(l1)