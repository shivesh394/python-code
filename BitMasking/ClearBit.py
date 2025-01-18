n = 145
i = 5
mask = ~(1<<(i-1))

print(bin(n)[2:], mask)
n = n & mask
print(n)
print(bin(n)[2:])