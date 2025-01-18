class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def createTree(arr):
    q = []
    i = 1
    root = Node(arr[0])
    q.append(root)
    while i < len(arr):
        temp = q.pop(0)
        newNode = Node(arr[i])
        temp.left = newNode
        q.append(newNode)
        i += 1
        newNode = Node(arr[i])
        temp.right = newNode
        q.append(newNode)
        i += 1
    return root


def levelOrder(root):
    ans = []
    if not root:
        return ans
    q = []
    q.append(root)
    while(q):
        level = []
        # size = len(q)
        for i in range(len(q)):
            front = q.pop(0)
            level.append(front.data)
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
        ans.append(level)
    return ans

# from collections import deque
# def levelOrder(root):
#     ans = []
#     if not root:
#         return ans
#     queue = deque()
#     queue.append(root)
#     while queue:
#         node = queue.popleft()
#         ans.append(node.data)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     return ans




l = [1,2,3,4,5,6,7]
root = createTree(l)
ans = levelOrder(root)
print(ans)