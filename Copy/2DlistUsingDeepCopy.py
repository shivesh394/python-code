import copy
l1 = [ 'a', 'b',[ 'c', 'd' ], 'e' , 'f' , 'g' , ['h','i']]
l2 = copy.deepcopy(l1)
l3 = l1.copy()
l1.append(["a"])

print(l1)
print(l2)
print(l3)

l1[2][1] = "c"

print(l1)
print(l2)
print(l3)