def fun(a, n):
    if a == 0: return 0
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res*a
        a = a*a
        n //= 2
    return res


def aTn(a, n):
    if n == 1:
        return a
    if n % 2:
        return a * fun(a, n - 1)
    else:
        return fun(a * a, n // 2)
    



def helper(a, n):
    if a == 0 : return 0
    if n == 0 : return 1
    res = helper(a, n//2)
    res = res*res
    return a*res if n % 2 == 1 else res


    
print(fun(2, 10))
print(helper(2, 10))
print(aTn(2, 15))