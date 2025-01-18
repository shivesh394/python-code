n = 17
i = 4
mask = 1<<(i-1)
print(bin(n))
res = (n & mask)>>(i-1)
print(res)