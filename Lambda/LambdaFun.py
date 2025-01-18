fun=lambda x:x*x*x
print(fun(12))

#lambda with filter
l1=[1,2,3,4,5,6,7,8,9,10]
l2=list(filter(lambda x: (x%2==0),l1))
print(l2)

#lambda with map
l3=[23,45,12,56,765,69]
l4=list(map(lambda x:x*2,l3))
print(l4)

R = lambda a: print(a%2==0)
print(R(4))