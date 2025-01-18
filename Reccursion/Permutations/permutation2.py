nums = [1,2,3]
ans = []
sol = []
vis = set()

def dfs():
    if len(sol) == len(nums):
        ans.append(sol.copy())
        return
    for num in nums:
        if num not in vis:
            vis.add(num)
            sol.append(num)
            dfs()
            sol.pop()
            vis.remove(num)

dfs()
print(ans)