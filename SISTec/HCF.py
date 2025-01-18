def gcd (a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

a=int(input("Enter a : "))
b=int(input("Enter b : "))
x=gcd(a, b)
y=(a*b)/x
print("HCF of",a," ",b," is",x)
print("LCM of",a," ",b," is",y)