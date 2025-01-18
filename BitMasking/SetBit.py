n = 145
i = 3
mask = 1<<(i-1)
print(bin(n)[2:])
n = mask | n
print(n)
print(bin(n)[2:])