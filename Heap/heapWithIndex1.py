l = [0]

def insert(num):
    i = len(l)
    l.append(num)
    while i > 1:
        p = i//2
        if l[i] > l[p]:
            l[i], l[p] = l[p], l[i]
            i = p
        else:
            return

def delete():
    print(l[1])
    l[1] = l[len(l)-1]
    l.pop()
    i = 1
    if len(l) == 3:
        if l[1] < l[2]:
            l[1], l[2] = l[2], l[1]
    while i < len(l)//2:
        left = l[2*i]
        right= l[2*i + 1]
        larger = 2*i if left > right else 2*i + 1
        if l[i] < l[larger]:
            l[i], l[larger] = l[larger], l[i]
            i = larger
        else:
            return

insert(50)
insert(30)
insert(40)
insert(10)
insert(5)
insert(20)
insert(100)
insert(60)
insert(52)
insert(8)
insert(4)
insert(14)

while len(l) > 1:
    delete()