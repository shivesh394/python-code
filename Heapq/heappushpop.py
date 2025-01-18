from heapq import *
a = [2,7,4,0,8,12,14,13,10,3,4]
heapify(a)
b = a[:]
print(heappushpop(a, -1))
print(heapreplace(b, -1))