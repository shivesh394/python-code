def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    while(m%n)!=0:
        (m,n)=(n,m%n)
    return(n)

a=int(input("Enter a : "))
b=int(input("Enter b : "))
print("GCD of",a," ",b," is",gcd(a,b))