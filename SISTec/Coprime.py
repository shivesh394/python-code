def gcd (a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a=int(input("Enter a : "))
b=int(input("Enter b : "))
x=gcd(a,b)
if x==1:
    print("Numbers are coprime")
else:
    print("Numbers are not coprime")