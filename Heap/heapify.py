a = [10,23,90,1,45,27,12,88]

def heapify(i , n):
    lar = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and a[l] > a[lar]:
        lar = l
    if r < n and a[r] > a[lar]:
        lar = r
    if lar != i:
        a[i], a[lar] = a[lar], a[i]
        heapify(lar, n)
n = len(a)
for i in range(n//2 -1, -1, -1):
    heapify(i, n)
print(a)