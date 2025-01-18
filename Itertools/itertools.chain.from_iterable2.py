# Importing chain class from itertools 
from itertools import chain 


# Single iterable containing iterable elements(strings and list) is passed as input 
from_iterable = chain.from_iterable(['geeks', 'for', 'geeks', ['w', 'i', 'n', 's']]) 

# printing the flattened iterable 
print(list(from_iterable)) 
