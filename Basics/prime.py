n=int(input("enter a number="))
a=0
for i in range(1,n+1):
    if n%i==0:
        a+=1
if a==2:
    print(n," is a prime number")
else:
    print(n," is not a prime number")
