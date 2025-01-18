class Graph:
	def __init__(self,V):
		self.V = V
		self.adj = [[] for i in range(V)]

	def addEdge(self, u,  v):
		self.adj[u].append(v)

	def DFS(self,s):		 
		visited = [False for i in range(self.V)]
		stack = []
		stack.append(s)
		visited[s] = True
		while stack:
			s = stack.pop()
			print(s, end=' ')
			for node in self.adj[s]:
				if (not visited[node]):
					stack.append(node)
					visited[node] = True




g = Graph(5);
g.addEdge(1, 0);
g.addEdge(0, 2);
g.addEdge(2, 1);
g.addEdge(0, 3);
g.addEdge(1, 4);

print("Following is Depth First Traversal")
g.DFS(0)
