a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
n =len(a)

rmax=[a[-1]]
j=0
for i in range(n-2,-1,-1):
    if a[i]>=rmax[j]:
        rmax.append(a[i])
        j+=1
    else:
        rmax.append(rmax[j])
        j+=1
rmax.reverse()
print(rmax)