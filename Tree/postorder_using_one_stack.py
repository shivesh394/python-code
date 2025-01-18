stack = []
ans = []
if not root:
    return ans
cur = root
while cur or stack:
    if cur:
        stack.append(cur)
        cur = cur.left
    else:
        temp = stack[-1].right
        if not temp:
            temp = stack.pop()
            ans.append(temp.data)
            while stack and temp == stack[-1].right:
                temp = stack.pop()
                ans.append(temp.data)
        else:
            cur = temp
print(ans)