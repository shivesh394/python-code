import copy
l1 = [ 'a', 'b',[ 'c', 'd' ], 'e' , 'f' , 'g' , ['h','i']]
l2 = copy.copy(l1)
l1.append(["a","b"])

print(l1)
print(l2)


l1[0] = 'z'
print(l1)
print(l2)

l1[2][1] = "c"

print(l1)
print(l2)

# Here we can see that the result is changed in both lists, this is because shallow copy shares the same reference In nested values.