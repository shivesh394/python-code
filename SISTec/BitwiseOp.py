print(4 & 5)
print(4 | 5)
print(4 << 1)
print(4 >> 1)


#assignment operator
a=5
print(a)
a+=5
print(a)
a**=3
print(a)

a,b,c=2,3,4
print(a,b,c)

a,b,c=[1,2,3]  #list unpacking
print(a,b,c)

a,b,c=(1,2,3)  #tuple unpacking
print(a,b,c)

#there are no increment anddecrement operator in python
#no ternary opartor

a,b,c,d=20,10,50,40
x=30 if a<b else 40 if c<d else 50
print(x)