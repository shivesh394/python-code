d1={}
print(type(d1))

d2={1:"shivesh","bae":"shaku","child":"infi"}
print(d2)
print(d2[1])
print(d2['child'])

d2["son"]="maxibelly"
print(d2)


d3=d2.copy()
print(d3)

d4=dict(d2)
print(d4)

print(d2.get("bae"))

d2.update({2:"maxi"})
print(d2)

print(d2.keys())
print(d2.items())
print(d2.values())


del d2["son"]
print(d2)

d2.pop(1)
print(d2)

d2.popitem()
print(d2)

d2.clear()
print(d2)

del d2
print(d2)