sum=0
i=1
n=int(input("enter a number="))
while i<n:
    if n%i==0:
        sum=sum+i
    i+=1
if sum==n:
    print(n,"is a perfect number")
else:
    print(n," is not a perfect number")