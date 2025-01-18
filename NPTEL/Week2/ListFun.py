def Update(l,i,v):
    if i>=0 and i<len(l):
        l[i]=v
        return l
    else:
        v=v+1
        return v

ns=[3,11,12]  #mutable
z=69          #immutable

print(Update(ns,2,z))
print(Update(ns,4,z))
print(ns)
print(z)