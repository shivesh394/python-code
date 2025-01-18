from collections import defaultdict
d = defaultdict(int)

d[5] += 1
print(d[5])

print(d[9])

if d[2]:
    print("YES")
else:
    print('NO')


d1 = {}


# print(d1[2])
# print(d1.get(2))
print(d1.get(2, 0))

# d1[2] += 1
# print(d1[2])


