class UnionFind:
	def __init__(self, graph):
		self._id = {}
		self._size = {}

		for vertex in graph:
			self._id[vertex] = vertex
			self._size[vertex] = 1

	def _root(self, u):
		while self._id[u] != u:
			self._id[u] = self._id[self._id[u]]
			u = self._id[u]
		return u

	def find(self, u):
		return self._root(u)

	def union(self, u, v):
		root_u = self._root(u)
		root_v = self._root(v)

		if self._size[root_u] < self._size[root_v]:
			self._id[root_u] = root_v
			self._size[root_v] += self._size[root_u]
		else:
			self._id[root_v] = root_u
			self._size[root_u] += self._size[root_v]
