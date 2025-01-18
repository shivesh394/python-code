a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
n =len(a)

lmin=[a[0]]

for i in range(1,n):
    if a[i] <= lmin[i-1]:
        lmin.append(a[i])
    else:
        lmin.append(lmin[i-1])

print(lmin)