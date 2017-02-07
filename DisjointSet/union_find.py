class UnionFind:
	def __init__(self, graph):
		self.id = {}
		self.size = {}

		for vertex in graph:
			self.id[vertex] = vertex
			self.size[vertex] = 1

	def root(self, u):
		while self.id[u] != u:
			self.id[u] = self.id[self.id[u]]
			u = self.id[u]
		return u

	def find(self, u):
		return self.find(u)

	def union(self, u, v):
		root_u = self.root(u)
		root_v = self.root(v)

		if self.size[root_u] < self.size[root_v]:
			self.id[root_u] = root_v
			self.size[root_v] += self.size[root_u]
		else:
			self.id[root_v] = root_u
			self.size[root_u] += self.size[root_v]
