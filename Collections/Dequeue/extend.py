# extend(iterable): This function is used to add multiple values at the right end of the deque. The argument passed is iterable.

import collections

de = collections.deque([1, 2, 3,])

de.extend([4,5,6])
print(de)
