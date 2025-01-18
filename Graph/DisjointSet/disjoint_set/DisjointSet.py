from disjoint_set import DisjointSet
ds = DisjointSet({1: 1})
print(ds)

ds2 = DisjointSet.from_iterable([1,2,3])
print(ds2)

print(ds.find(1))
print(ds.find(5))
print(ds.find(15))


ds3 = DisjointSet({1: 2, 2: 2, 3: 3})
print(list(ds3))
print(list(ds3.itersets()))
print(ds3.connected(1,2))
print(ds3.connected(1,3))
print(ds3.connected(11,2))