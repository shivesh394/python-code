from itertools import chain 

# Single iterable containing iterable elements(strings) is passed as input 
from_iterable = chain.from_iterable(['geeks', 'for', 'geeks']) 

# printing the flattened iterable 
print(from_iterable) 
print(list(from_iterable)) 
