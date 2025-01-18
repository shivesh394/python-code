from collections import OrderedDict

my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move key 'a' to the end
my_dict.move_to_end('a')

print(my_dict)

# Move key 'b' to the beginning
my_dict.move_to_end('c', last=False)

print(my_dict)
