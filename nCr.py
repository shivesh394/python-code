n, r = 100, 3
num = 1
den = 1
while r:
    num *= n
    den *= r
    n -= 1
    r -= 1
res = num // den
print(res)