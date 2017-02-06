import heapq

from Graphs.graph_builder import build_directed_edge_weighted_graph


def relax(neighbour, vertex):
	if neighbour.distance > vertex.distance + vertex.get_weight(neighbour):
		neighbour.distance = vertex.distance + vertex.get_weight(neighbour)
		neighbour.parent = vertex


def dijkstra(graph, source):
	source.distance = 0
	vertex_list = [vertex for vertex in graph]
	heapq.heapify(vertex_list)
	while vertex_list:
		min_vertex = heapq.heappop(vertex_list)
		for neighbour in min_vertex.connections():
			relax(neighbour, min_vertex)
		min_vertex.color = 'black'
		while vertex_list:
			heapq.heappop(vertex_list)
		vertex_list = [vertex for vertex in graph if vertex.color == 'white']
		heapq.heapify(vertex_list)


def main():
	graph, source = build_directed_edge_weighted_graph()
	dijkstra(graph, source)

	for vertex in graph:
		print(vertex)


if __name__ == '__main__':
    main()
