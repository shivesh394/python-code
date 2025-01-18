x = int(input())
c = int(input())
n = int(input())

b = bin(c)[2:]
z = 1
for i in range(len(b)):
    z = z**2 % n
    if b[i] == '1':
        z = z*x % n
print(z)
