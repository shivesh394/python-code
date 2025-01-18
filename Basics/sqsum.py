def sqsum(n):
    if n==1:
        return 1
    return n*n+sqsum(n-1)
n=int(input('Enter a number:'))
print(sqsum(n))

#or

x=int(input("Enter a number:"))
y=x*(x+1)*(2*x+1)//6
print(y)