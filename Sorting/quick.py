arr = [34, 3, 78, 12, 23, 11, 2, 89, 7, 6, 96, 32]

# def Partition(arr, low, high):
#     pivot = arr[low]
#     i, j = low, high
#     while i < j:
#         while i <= high and arr[i] <= pivot:
#             i += 1
#         while j >= low and arr[j] > pivot:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[j], arr[low] = arr[low], arr[j]
#     return j



def Partition(arr, low, high):
    pInd, pivot = low, arr[high]
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[pInd] = arr[pInd], arr[i]
            pInd += 1
    arr[pInd], arr[high] = arr[high], arr[pInd]
    return pInd


def quickSort(arr, low, high):
    if(low < high):
        partition = Partition(arr, low, high)
        quickSort(arr, low, partition - 1)
        quickSort(arr, partition + 1, high)

quickSort(arr, 0, len(arr) - 1)
print(arr)