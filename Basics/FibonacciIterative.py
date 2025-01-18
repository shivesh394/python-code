def fib(n):
    f1=-1
    f2=1
    for i in range(1,n+1):
        f3=f1+f2
        f1=f2
        f2=f3
    return f3

n=int(input("Enter a number : "))
x=fib(n)
print(x)
sum=0
z=x
while z!=0:
    z=z//10
    sum+=1
print("Number of digit is :",sum)
