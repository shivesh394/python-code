def gcd(m,n):
    i=min(m,n)
    while i>0:
        if(m%i)==0 and (n%i)==0:
            return(i)
        else:
            i=i-1

a=int(input("Enter a : "))
b=int(input("Enter b : "))
print("GCD of",a," ",b," is",gcd(a,b))