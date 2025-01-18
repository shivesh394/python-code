greatest = lambda x,y : x if x > y else y
print(greatest(2, 7))

l2 = lambda *x : list(filter(lambda y: (y % 2 == 0), x))
print(l2(1,2,3,34,55,67,8))

s = lambda **x : print(x.keys(), x.values())
s(name="Maxi", age=12)