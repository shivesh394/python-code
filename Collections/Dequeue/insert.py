# Example 1: Appending Items Efficiently
# append(): This function is used to insert the value in its argument to the right end of the deque.
# appendleft(): This function is used to insert the value in its argument to the left end of the deque.
# insert(i, a) : This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.



import collections

de = collections.deque([1, 2, 3])
print("deque: ", de)

de.append(4)
print(de)

de.appendleft(0)
print(de)

# using insert() to insert the value 300 at index 1
de.insert(1,300)
print(de)