from Graphs.graph import Graph


def build_directed_graph():
	graph = Graph()
	graph.add_edge('u', 'v')
	graph.add_edge('v', 'y')
	graph.add_edge('y', 'x')
	graph.add_edge('x', 'v')
	graph.add_edge('u', 'x')
	graph.add_edge('w', 'y')
	graph.add_edge('w', 'z')
	graph.add_edge('z', 'z')
	return graph, graph.get_vertex('u')


def build_undirected_graph():
	graph = Graph()
	graph.add_edge('u', 'v', 'undirected')
	graph.add_edge('v', 'y', 'undirected')
	graph.add_edge('y', 'x', 'undirected')
	graph.add_edge('x', 'v', 'undirected')
	graph.add_edge('u', 'x', 'undirected')
	graph.add_edge('w', 'z', 'undirected')
	graph.add_edge('z', 'z', 'undirected')
	return graph, graph.get_vertex('u')
