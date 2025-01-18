import copy
x = [[1,2],[3,4]]
y = x[:]
z = x.copy()
a = copy.deepcopy(x)
x[0][0] = 9
print(x)
print(y)
print(z)
print(a)

y[1][1] = 6
print(x)
print(y)
print(z)
print(a)

z[0][1] = 8
print(x)
print(y)
print(z)
print(a)


a[1][0] = 7
print(x)
print(y)
print(z)
print(a)

x.append([11, 11])
print(x)
print(y)
print(z)
print(a)