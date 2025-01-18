nums = [4, 10, 5, 8, 20, 15, 3, 12]  # decresing stack

ans = []
stack = []
for i in range(len(nums) - 1, -1, -1):
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(nums[i])
ans.reverse()
print(ans) 