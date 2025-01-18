l=list(map(int,input().split()))
l.sort()
for i in range(l[-1]+1):
    if i not in l:
        print(i)
        break