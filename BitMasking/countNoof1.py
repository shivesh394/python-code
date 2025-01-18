import math
n = -16


c = 0
print(bin(n))
for i in range(int(math.log(abs(n),2))+1):
    if (n>>i) & 1:
        c += 1
print(c)




# c = 0
# while(n):
#     c += 1
#     n = n & (n-1)
# print(c)