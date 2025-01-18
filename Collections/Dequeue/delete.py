# Example 2: Popping Items Efficiently
# pop(): This function is used to delete an argument from the right end of the deque.
# popleft(): This function is used to delete an argument from the left end of the deque.


import collections

de = collections.deque([0, 1, 2, 3, 4])
print(de)

de.pop()
print(de)

de.popleft()
print(de)
