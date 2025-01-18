import collections

d = collections.deque([6, 1, 2, 3, 4])
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.insert(4,3)  # using insert() to insert the value 3 at 4th index
print(d)

print (d.count(3))

d.remove(3)
print(d)

d.extend([4,5,6])
print(d)

d.extendleft([7,8,9])
print(d)

d.rotate(3)  # using rotate() to rotate the deque rotates by 3 to left
print(d)

d.rotate(-3)
print(d)

d.reverse()
print(d)