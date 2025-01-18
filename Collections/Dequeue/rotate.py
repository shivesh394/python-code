# rotate(): This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to the left. Else rotation is to right.

import collections

de = collections.deque([1, 2, 3,])

# using rotate() to rotate the deque rotates by 3 to left
de.rotate(-3)
print (de)