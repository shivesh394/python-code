from functools import reduce
s=lambda *x:list(filter(lambda y:(y%2==0),x))
res=reduce(lambda x,y:x+y,s(1,2,3,4,5,6,7,8,9))
print(res)