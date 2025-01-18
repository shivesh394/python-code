# Problem Statement:
# There’s an array ‘A’ of size ‘N’ with positive and negative elements (not necessarily equal). Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values. The leftover elements should be placed at the very end in the same order as in array A.

# Note: Start the array with positive elements.


# def alternateNumbers(nums):
#     pos = []
#     neg = []
#     for n in nums:
#         if n > 0:
#             pos.append(n)
#         elif n < 0:
#             neg.append(n)
#     c = 0
#     for i in range(min(len(pos),len(neg))):
#         nums[2*i] = pos.pop(0)
#         nums[2*i+1] = neg.pop(0)
#         c += 1
#     i = 2*c
#     while pos:
#         nums[i] = pos.pop(0)

#     while neg:
#         nums[i] = neg.pop(0) 
#     return nums



def alternateNumbers(nums):
    posInd = 0
    negInd = 1
    pos = 0
    neg = 0
    ans = [0]*len(nums)
    for n in nums:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1

    l = min(pos, neg)

    for i in range(2*l):
        if nums[i] > 0:
            ans[posInd] = nums[i]
            posInd += 2
        elif nums[i] < 0:
            ans[negInd] = nums[i]
            negInd += 2
    c = 2*l
    if pos > neg:
        for i in range(pos-neg):
            ans[l+i] = nums[i]
    elif neg > pos:
        for i in range(neg - pos):
            ans[l+i] = nums[i]
    return nums
    

nums = [1,2,-4,-5]
nums = [1,2,-3,-1,-2,-3]

print(alternateNumbers(nums))