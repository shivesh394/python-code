nums = [3, 6, 9, 4, 1, 10, 34, 2, 5, 8]

for i in range(1, len(nums)):
    cur = nums[i]
    j = i - 1
    while j >= 0 and cur < num[j]:
        num[j+1] = num[j]
        j -= 1
        
    nums[j+1] = cur

print(nums)