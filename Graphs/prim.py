import heapq

from Graphs.graph_builder import build_undirected_edge_weighted_graph


def mst_prim(graph, source):
	source.distance = 0
	vertex_list = [vertex for vertex in graph]
	heapq.heapify(vertex_list)
	while vertex_list:
		vertex = heapq.heappop(vertex_list)
		vertex.color = 'black'
		for neighbour in vertex.connections():
			if neighbour.color == 'white' and neighbour.distance > vertex.get_weight(neighbour):
				neighbour.parent = vertex
				neighbour.distance = vertex.get_weight(neighbour)
		while vertex_list:
			vertex_list.pop()
		vertex_list = [vertex for vertex in graph if vertex.color == 'white']
		heapq.heapify(vertex_list)


def main():
	graph, source = build_undirected_edge_weighted_graph()
	mst_prim(graph, source)
	assert sum(vertex.distance for vertex in graph) is 37
	print('All test cases passed')


if __name__ == '__main__':
    main()
