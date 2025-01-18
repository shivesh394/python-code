import copy
a = 'hello'
b = str(a)
c = a[:]
d = a + ''
e = copy.copy(a)

print(id(a),id(b),id(c),id(d),id(e))