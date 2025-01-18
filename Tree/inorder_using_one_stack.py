def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
    # stack = []
    # ans = []
    # if not root:
    #     return ans
    # node = root
    # while True:
    #     if node:
    #         stack.append(node)
    #         node = node.left
    #     else:
    #         if not stack:
    #             break
    #         node = stack.pop()
    #         ans.append(node.val)
    #         node = node.right
    # return ans




    stack, ans = [], []
    if not root:
        return []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break
        root = stack.pop()
        ans.append(root.val)
        root = root.right
    return ans