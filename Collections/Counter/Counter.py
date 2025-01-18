from collections import Counter

x = Counter("geeksforgeeks")
print(x)

for i in x.elements():
	print ( i, end = " ")