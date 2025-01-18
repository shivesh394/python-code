import itertools

l = ['Geeks', 'for', 'Geeks']

# defining iterator
iterators = itertools.cycle(l)

# for in loop
for i in range(6):
	print(next(iterators), end=" ")
