from Graphs.graph import Graph


def build_directed_acyclic_graph():
	graph = Graph()
	graph.add_edge('u', 'v')
	graph.add_edge('v', 'y')
	graph.add_edge('y', 'x')
	graph.add_edge('u', 'x')
	graph.add_edge('w', 'y')
	graph.add_edge('w', 'z')
	return graph, graph.get_vertex('u')


def build_directed_cyclic_graph():
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


def build_directed_edge_weighted_graph():
	graph = Graph()
	graph.add_edge('s', 't', cost=10)
	graph.add_edge('s', 'y', cost=5)
	graph.add_edge('t', 'y', cost=2)
	graph.add_edge('y', 't', cost=3)
	graph.add_edge('t', 'x', cost=1)
	graph.add_edge('y', 'z', cost=2)
	graph.add_edge('y', 'x', cost=9)
	graph.add_edge('z', 's', cost=7)
	graph.add_edge('z', 'x', cost=6)
	graph.add_edge('x', 'z', cost=4)
	return graph, graph.get_vertex('s')


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
