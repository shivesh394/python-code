import time
x=int(input("Enter x : "))
y=int(input("Enter y : "))

s1=time.time_ns()
x,y=y,x
s2=time.time_ns()

print("x : ",x)
print("y : ",y)
print("time : ",s2-s1)