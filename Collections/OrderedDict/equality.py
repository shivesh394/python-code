from collections import OrderedDict

# Create two ordered dictionaries with different orderings
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# Compare the ordered dictionaries for equality
print(od1 == od2) 
