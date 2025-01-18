def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    
    while(m%n)!=0:
        d=m-n
        (m,n)=(gcd(max(n,d),min(n,d)))
    return(n)
a=int(input("Enter a : "))
b=int(input("Enter b : "))
print("GCD of",a," ",b," is",gcd(a,b))