l = [3, 6, 9, 4, 1, 10, 34, 2, 5, 8]

for i in range(len(l)):
    for j in range(1,len(l)-i): 
        if l[j-1] > l[j] :
            l[j-1], l[j] = l[j], l[j-1]

print(l)