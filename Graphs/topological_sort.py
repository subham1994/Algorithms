from Graphs.graph_builder import build_directed_graph


def dfs(source, postorder):
	source.color = 'gray'
	for neighbour in source.connections():
		if neighbour.color == 'white':
			dfs(neighbour, postorder)
	source.color = 'black'
	postorder.append(source)


def topological_sort(graph):
	postorder = []
	for vertex in graph:
		if vertex.color == 'white':
			dfs(vertex, postorder)
	return iter(reversed(postorder))


def main():
	graph, _ = build_directed_graph()
	print(list(topological_sort(graph)))

if __name__ == '__main__':
    main()
