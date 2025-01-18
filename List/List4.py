l=[1,1,1,1,1]
x=list(set(l)) #set data type which do not duplicate the value ,insertion order is not reserved
print(type(x),x)
x={1,1,1,2,3,4,5}
print(x)
s={1,2,3,1,1,1,1,1,1}
x=frozenset(s)
print(x)
# x.add(5)
# print(x)  #frozenset can't add
