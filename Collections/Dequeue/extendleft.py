# extendleft(iterable): This function is used to add multiple values at the left end of the deque. The argument passed is iterable. Order is reversed as a result of left appends.
import collections

de = collections.deque([1, 2, 3,])

de.extendleft([7,8,9])
print (de)