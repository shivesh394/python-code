# importing libraries 
from sortedcontainers import SortedList, SortedSet, SortedDict 

# initializing a sorted set with parameters 
# it takes an iterable as an argument 
# sorted_set = SortedSet([1, 1, 2, 3, 4]) 
# print(sorted_set.pop(0))
s = SortedSet()
s.add((1, 2))
s.add((1, 2))
print(s)
s.remove((1, 2))
s.add((90, 2))
s.add((3, 2))
s.add((4, 2))
s.add((5, 2))
print(s)
a, b  = s.pop(0)
print(a, b)