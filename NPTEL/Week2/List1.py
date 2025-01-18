num=[1,2,3,4]
name=["shiv","maxi","belly"]
mixed=[2,"shivesh","yellow"]

print(len(num))
print(len(name))
print(len(mixed))
print(name)
print(name[0])
print(name[0:1])
print(name[0:2])

nested=[1,2,["hello",3,[9]]]
print(nested)
print(nested[2])
print(nested[2][0])
print(nested[2][0][4])

nested[2]=3   # lists are mutable
print(nested)