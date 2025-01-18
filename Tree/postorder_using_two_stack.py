stack = []
ans = []
if not root:
    return ans
stack.append(root)
while stack:
    node = stack.pop()
    ans.append(node.data)
    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)
ans.reverse()
print(ans)