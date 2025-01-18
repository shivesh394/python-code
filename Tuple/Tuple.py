tup=(1,'a',"shivesh",6.9,True,6+9j)   #tuple is immutable
print(tup)
print(tup[0])
print(tup[-1])
print(tup[2:5])
print(len(tup))


t1=(1,2,3,9.8)
t2=("maxi",7+5j)
print(t1,t2)
print(t1+t2)
print(t2+t1)

print((t2*3))
print((t1*2+t2))
print(min(t1))
print(max(t1))

t3=(1,8.4,9,2+3j)
#print(max(t3))   #Error because of int and complex type