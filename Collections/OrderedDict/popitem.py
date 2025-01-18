from collections import OrderedDict

my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

last_item = my_dict.popitem(last = True)
print(last_item) 

first_item = my_dict.popitem(last = False)
print(first_item)
