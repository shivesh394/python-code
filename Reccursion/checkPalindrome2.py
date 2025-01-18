s = 'asdfdsa'
n = len(s)

def fun(i):
    if i >= n//2:
        return True

    if s[i] != s[n - i -1]:
        return False
    else:
        return fun(i + 1)

print(fun(0))