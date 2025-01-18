l=[1,5,3,4,3,5,6]
for i in l:
    if l.count(i) > 1:
        print(l.index(i)+1)
        break
