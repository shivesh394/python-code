n = 100
print(bin(n)[2:])
rightMost1 = (n & n - 1) ^ n
rightMost2 = n & ~ (n - 1)
print(rightMost1, bin(rightMost1)[2:])
print(rightMost2, bin(rightMost2)[2:])