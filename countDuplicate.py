l=[1,2,3,4,1,2]

for i in range(len(l)):
    count = 0
    for j in range(i+1,len(l)):
        if(l[i] == l[j]):
            count=1
    if count == 1:
        print(l[i])