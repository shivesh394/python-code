nums = [1, 2, 3]
ans, sol = [], []
def backtrack():
    if len(sol) == len(nums):
        ans.append(sol[:])
        return
    for num in nums:
        if num not in sol:
            sol.append(num)
            backtrack()
            sol.pop()
backtrack()
print(ans)