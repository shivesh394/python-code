class getNode:
	def __init__(self, data):
		self.data = data 
		self.left = self.right = None
ans = []
def hasPath(root, res, x):
    if root.data == x:
        t = (root.data,)
        res += t
        ans.append(res)
        return 
    t = (root.data,)
    res += t
    if root.left:
        hasPath(root.left, res, x)
    if root.right:
        hasPath(root.right, res, x)

def printPath(root, x):
    t = ()
    hasPath(root, t, x)
    print(list(ans[0]))




root = getNode(1) 
root.left = getNode(2) 
root.right = getNode(3) 
root.left.left = getNode(4) 
root.left.right = getNode(5) 
root.right.left = getNode(6) 
root.right.right = getNode(7) 
    
x = 5
printPath(root, x)
