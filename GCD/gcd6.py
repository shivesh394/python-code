def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if(m%n)==0:
        return(n)
    else:
       d=m-n
       return(gcd(max(n,d),min(n,d)))

a=int(input("Enter a : "))
b=int(input("Enter b : "))
print("GCD of",a," ",b," is",gcd(a,b))