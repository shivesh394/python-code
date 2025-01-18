from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print(od)

od.pop('c')

print(od)

od['c'] = 3

print(od)

for key in od:
    print(key)