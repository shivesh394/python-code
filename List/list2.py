n=int(input())
l=list(map(int,input().split()))

count=0
for i in range(len(l)-1):
    if(l[i]==2):
        print(l[i+1])
        count+=1
i+=1
if(l[i]==2):
    print("-1")
    count+=1
if(count==0):
    print("-1")
