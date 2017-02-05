from Graphs.graph_builder import build_directed_cyclic_graph


class DirectedGraphCycleDetector:
	def __init__(self, graph):
		self.cycle = []

		for vertex in graph:
			self.dfs(vertex)

	def detected_cycle(self):
		return self.cycle != []

	def dfs(self, source):
		source.color = 'gray'
		for neighbour in source.connections():
			if self.detected_cycle():
				return
			elif neighbour.color == 'white':
				neighbour.parent = source
				self.dfs(neighbour)
			elif neighbour.color == 'gray':
				vertex = source
				while vertex != neighbour:
					self.cycle.append(vertex)
					vertex = vertex.parent
				self.cycle.append(neighbour)
				self.cycle.append(source)
		source.color = 'black'

	def __iter__(self):
		return iter(reversed(self.cycle))


def main():
	graph, _ = build_directed_cyclic_graph()
	directed_graph_cycle_detector = DirectedGraphCycleDetector(graph)
	assert directed_graph_cycle_detector.detected_cycle()
	print('All test cases passed')


if __name__ == '__main__':
    main()
