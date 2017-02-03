from Graphs.graph_builder import build_undirected_graph

'''
	connectivity in undirected graphs
		- Vertices V and W are connected if there is a path between them.
		- Preprocess graph to answer queries of the form `is V connected to w` in constant.
		- `is connected to` relation is an Equivalence relation(Reflexive, Symmetric, Transitive).
'''

ids = {}


def connected(u, v):
	return ids.get(u) == ids.get(v)


def dfs(source, count):
	source.color = 'gray'
	ids[source] = count
	for neighbour in source.connections():
		if neighbour.color == 'white':
			neighbour.parent = source
			dfs(neighbour, count)
	neighbour.color = 'black'


def main():
	graph, _ = build_undirected_graph()

	for index, vertex in enumerate(graph):
		if vertex.color == 'white':
		    dfs(vertex, index)

	assert connected(graph.get_vertex('u'), graph.get_vertex('x'))
	assert connected(graph.get_vertex('u'), graph.get_vertex('v'))
	assert connected(graph.get_vertex('v'), graph.get_vertex('u'))
	assert connected(graph.get_vertex('w'), graph.get_vertex('z'))
	assert not connected(graph.get_vertex('u'), graph.get_vertex('w'))
	print('all test cases passed')


if __name__ == '__main__':
    main()
