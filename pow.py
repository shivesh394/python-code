x, n = 2, 21
ans = 1
while n:
    if n % 2:
        ans *= x
        n -= 1
    else:
        x*= x
        n //= 2
print(ans, 2**21)