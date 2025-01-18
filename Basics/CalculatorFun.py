def calculator(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return (sum,sub,mul,div)

t=calculator(10, 2)  #python virtual machine always consider these multiple values only one object that is tuple
print(t)
print(type(t))

print("Sum of x and y :",t[0])
print("Subtraction of x and y :",t[1])
print("Multiplication of x and y :",t[2])
print("Division of x and y :",t[3])