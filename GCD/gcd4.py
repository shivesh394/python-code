def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if(m%i)==0 and (n%i)==0:
            cf=i
    return(cf)

a=int(input("Enter a : "))
b=int(input("Enter b : "))
print("GCD of",a," ",b," is",gcd(a,b))