x, y = 20, 30
print(bin(x)[2:], bin(y)[2:])
while y:
    tmp = x & y
    x = x ^ y
    y = tmp << 1
    print(bin(tmp)[2:], bin(x)[2:], bin(y)[2:])
print(x)