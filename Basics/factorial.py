x=int(input("Enter a number : "))
y=x
for i in range(x,1,-1):
    y=y*(i-1)
print("Factorial of",x,"is : ",y)


sum=0
z=y
while z!=0:
    z=z//10
    sum+=1
print("Number of digit in",x,"! is :",sum)


import math
  
print ("The factorial of 23 is : ", end="")
print (math.factorial(23))