#Find no. of bit to change to convert a into b

import math
a = 45
b = 34

print(bin(a)[2:], bin(b)[2:])

n = a ^ b
c = 0
print(bin(n)[2:])
for i in range(int(math.log(n,2))+1):
    if (n>>i) & 1:
        c += 1
print(c)

c = 0
while(n):
    c += 1
    n = n & (n-1)
print(c)