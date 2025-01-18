l = [1,2,3,4]
for i in range(len(l)):
    l[i] = str(l[i])

print(l)

s = "".join(l)
print(s)