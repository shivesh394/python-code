import time
x=int(input("Enter x : "))
y=int(input("Enter y : "))
 
s1=time.time_ns() 
x = x ^ y; 
y = x ^ y; 
x = x ^ y; 
s2=time.time_ns()
 
print ("After Swapping: x = ", x, " y =", y)
print(s2-s1)