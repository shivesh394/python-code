import dis

def add(x,y):
    return x+y

a=lambda x,y:x+y

print(dis.dis(add))
print(dis.dis(a))