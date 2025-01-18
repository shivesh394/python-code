def fun(n):
    if n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    elif n % 4 == 3:
        return 0
    else:
        return n
print(fun(5))