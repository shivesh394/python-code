def Divides(m,n):
    if m%n==0:
        return True
    else:
        return False

def Even(m):
    return(Divides(m,2))

def Odd(m):
    return(not Divides(m,2))

print(Even(100))
print(Even(99))
print(Odd(100))
print(Odd(99))