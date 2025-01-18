import time
x=int(input("Enter x : "))
y=int(input("Enter y : "))

s1=time.time_ns()
z=x
x=y
y=z
s2=time.time_ns()

print("x : ",x)
print("y : ",y)
print("Time : ",s2-s1)