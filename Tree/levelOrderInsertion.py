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


def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)


l = [1,2,3,4,5,6,7]
root = createTree(l)
inOrder(root)