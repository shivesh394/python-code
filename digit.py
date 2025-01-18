import math
z=int(input("Enter a number : "))
x=z
sum=0
while z!=0:
    z=z//10
    sum+=1
print(sum)


print(math.ceil(math.log(x,10)))