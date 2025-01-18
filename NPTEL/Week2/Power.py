def Power(m,n):
    ans=1
    for i in range(0,n):
        ans=ans*m
    return ans
m=int(input("Enter a number :"))
n=int(input("Enter power :"))
print(m,"to the power of",n,"is",Power(m,n))