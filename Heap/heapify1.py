a = [0,10,23,90,1,45,27,12,88]


def heapify(i, n):
    lar = i
    l = 2*i 
    r = 2*i + 1
    if l <= n and a[l] > a[lar]:
        lar = l
    if r <= n and a[r] > a[lar]:
        lar = r
    if lar != i:
        a[i], a[lar] = a[lar], a[i]
        heapify(lar, n)
n = len(a) - 1
for i in range(n//2, 0, -1):
    heapify(i, n)
print(a[1:])