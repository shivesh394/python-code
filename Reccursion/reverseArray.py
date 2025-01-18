arr = [1, 2, 3, 4, 5, 6, 7, 8]

def fun(l, r):
    if l < r:
        arr[l], arr[r] = arr[r], arr[l]
        fun(l + 1, r - 1)

fun(0, len(arr)-1)
print(arr)