import math
n = 15
a = 2
for i in range(2, 100):
    a = a**i % n
    d = math.gcd(a - 1, n)
    print(d)
    if 1 < d and d < n:
        print(d)