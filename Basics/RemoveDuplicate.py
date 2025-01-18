l=[1,2,3,4,1,2]

s=set(l)
l1=list(s)
print(s)
print(l1)

for i in l:
    print(i,": ",l.count(i))

dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
print(dup)