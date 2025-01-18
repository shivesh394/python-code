# Example 5: Front and Back of a deque
# Deque[0] : We can access the front element of the deque using indexing with de[0].
# Deque[-1] : We can access the back element of the deque using indexing with de[-1].


from collections import deque

de = deque([1, 2, 3, 4, 5, 6])
print(de)

print("Front element of the deque:", de[0])
print("Back element of the deque:", de[-1])
