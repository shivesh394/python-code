def helper(x, n):
    if x == 0 : return 0
    if n == 0 : return 1

    res = helper(x, n//2)
    res = res*res 
    return x*res if n%2 == 1 else res 
x = 8
n = 10
res = helper(x, abs(n))
print(res%6)