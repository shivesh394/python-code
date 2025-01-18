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
    if len(heap) == 0:
        return -1

    ans = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    # Edge case.
    if len(heap) == 0:
        return ans
        
    pos = 0
    while True:
        left = pos * 2 + 1
        right = pos * 2 + 2
        leftvalue = 0
        rightvalue = 0

        # To avoid IndexError.
        if left < len(heap):
            leftvalue = heap[left]
        if right < len(heap):
            rightvalue = heap[right]

        # Swapping it with the larger value.
        if leftvalue <= heap[pos] and rightvalue <= heap[pos]:
            # As it is larger than both its children, it is at its correct position.
            break
        elif leftvalue >= rightvalue:
            heap[pos], heap[left] = heap[left], heap[pos]
            pos = left
        else:
            heap[pos], heap[right] = heap[right], heap[pos]
            pos = right
    return ans



insert(20)
insert(7)
insert(11)
insert(3)
insert(2)
insert(5)

while heap:
    print(delete())