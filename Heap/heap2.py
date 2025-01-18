heap = []

def insert(num):
    i = len(heap)
    heap.append(num)
    while i > 0:
        p = (i - 1)//2
        if heap[i] > heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            return

def delete():
    if heap:
        ans = heap[0]
        heap[0] = heap[len(heap) - 1]
        heap.pop()
        i = 0

        while i <= (len(heap) - 1)//2:
            left = 2*i + 1 if 2*i + 1 < len(heap) else i
            right = 2*i + 2 if 2*i + 2 < len(heap) else i
            lar = left if heap[left] > heap[right] else right
            if heap[lar] > heap[i]:
                heap[lar], heap[i] = heap[i], heap[lar]
                i = lar
            else:
                break
        return ans
    else:
        return -1



insert(50)
insert(30)
insert(40)
insert(10)
insert(5)
insert(20)
# insert(100)
# insert(60)
# insert(52)
# insert(8)
# insert(4)
# insert(4)
# insert(3)
# insert(2)
insert(1)

while heap:
    print(delete())