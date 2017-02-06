class Vertex:
	def __init__(self, key):
		self.id = key
		self.color = 'white'
		self._neighbours = {}
		self.parent = None
		self.distance = float('inf')

	def add_neighbour(self, neighbour, weight):
		self._neighbours[neighbour] = weight

	def get_weight(self, neighbour):
		return self._neighbours[neighbour]

	def connections(self):
		return self._neighbours.keys()

	def __lt__(self, other):
		return self.distance < other.distance

	def __repr__(self):
		return "<Vertex: (id={id}, distance={distance}, parent={parent}, color={color})>".format(
			id=self.id,
			distance=self.distance,
			parent=self.parent.id if self.parent else None,
			color=self.color
		)


class Graph:
	def __init__(self):
		self._vertices = {}
		self._num_vertices = 0

	def reset(self):
		for _, vertex in self._vertices.items():
			vertex.color = 'white'
			vertex.parent = None
			vertex.distance = float('inf')

	def add_vertex(self, key):
		self._vertices[key] = Vertex(key)
		self._num_vertices += 1

	def get_vertex(self, key):
		return self._vertices.get(key, None)

	def add_edge(self, source, to, edge_type='directed', cost=0):
		if source not in self._vertices:
			self.add_vertex(source)
		if to not in self._vertices:
			self.add_vertex(to)
		if edge_type == 'undirected':
			self._vertices[to].add_neighbour(self._vertices[source], cost)
		self._vertices[source].add_neighbour(self._vertices[to], cost)

	def reverse(self):
		graph = Graph()
		for _, vertex in self._vertices.items():
			for neighbour in vertex.connections():
				graph.add_edge(neighbour.id, vertex.id)
		return graph

	def __iter__(self):
		return iter(self._vertices.values())

	def __repr__(self):
		return '<Graph: {num_vertices} vertices>'.format(num_vertices=self._num_vertices)
