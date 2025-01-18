arr = [1,2,3,4,5,6]
n = len(arr)

def fun(i):
    if i < n//2: 
        arr[i], arr[n - i - 1] = arr[n - i -1], arr[i]
        fun(i + 1)

fun(0)
print(arr)