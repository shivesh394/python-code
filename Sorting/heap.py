a = [3, 6, 9, 4, 1, 10, 34, 2, 5, 8]


def heapify(i, n):
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

def maxHeap():
    n = len(a)
    for i in range(n//2 -1, -1, -1):
        heapify(i, n)

def heapSort():
    n = len(a)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(0, i)

maxHeap()
print(a)
heapSort()
print(a)