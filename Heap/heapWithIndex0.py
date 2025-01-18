l = []

def insert(num):
    i = len(l)
    l.append(num)
    while i > 0:
        p = (i - 1)//2
        if l[i] > l[p]:
            l[i], l[p] = l[p], l[i]
            i = p
        else:
            return

def delete():
    print(l[0])
    l[0] = l[len(l)-1]
    l.pop()
    i = 0

    if len(l) == 2:
        if l[0] < l[1]:
            l[0], l[1] = l[1], l[0]
    while i < (len(l) - 1)//2:
        left = l[2*i + 1]
        right= l[2*i + 2]
        larger = 2*i + 1 if left > right else 2*i + 2
        if l[i] < l[larger]:
            l[i], l[larger] = l[larger], l[i]
            i = larger
        else:
            return

# insert(50)
# insert(30)
# insert(40)
# insert(10)
# insert(5)
# insert(20)
# insert(100)
# insert(60)
# insert(52)
# insert(8)
# insert(4)
# insert(4)
# insert(3)
# insert(2)
# insert(1)


while l:
    delete()