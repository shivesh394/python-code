n=int(input())
l=list(map(int,input().split()))

def gcd(x,y):
    if y==0:
        return x
    elif x>y:
        return gcd(y,x%y)
    elif y>x:
        return gcd(x,y%x)

lcm=l[0]
for i in range(len(l)-1):
    lcm=int(lcm*l[i+1]/gcd(lcm,l[i+1]))

print(lcm)