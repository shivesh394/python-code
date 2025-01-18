list1=[1,2,3,4]
list2=list1

list1[2:]=[7,8]
print(list1)
print(list2)

list1[2:]=[8,9,7,45]
print(list1)
print(list2)

list1[0:3]=[69]
print(list1)
print(list2)


print(69 in list1)
print(6 in list1)


l=[1,1,1,1,8,9,56,4,5,6]
if 1 in l:
    l.remove(1)
print(l)

while 1 in l:
    l.remove(1)
print(l)

l.reverse()
print(l)

l.sort()
print(l)

print(l.index(6))
# print(l.rindex(6))
