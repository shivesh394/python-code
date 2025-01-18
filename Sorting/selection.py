l = [3, 6, 9, 4, 1, 10, 34, 2, 5, 8]

for i in range(len(l)): 
    m = i
    for j in range(i+1,len(l)):
        if l[m] > l[j]:
            m = j
    l[m], l[i] = l[i], l[m]
print(l)
    