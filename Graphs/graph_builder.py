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


def build_undirected_edge_weighted_graph():
	graph = Graph()
	graph.add_edge('a', 'b', cost=4, edge_type='undirected')
	graph.add_edge('b', 'c', cost=8, edge_type='undirected')
	graph.add_edge('c', 'd', cost=7, edge_type='undirected')
	graph.add_edge('d', 'e', cost=9, edge_type='undirected')
	graph.add_edge('e', 'f', cost=10, edge_type='undirected')
	graph.add_edge('f', 'g', cost=2, edge_type='undirected')
	graph.add_edge('g', 'h', cost=1, edge_type='undirected')
	graph.add_edge('a', 'h', cost=8, edge_type='undirected')
	graph.add_edge('b', 'h', cost=11, edge_type='undirected')
	graph.add_edge('h', 'i', cost=7, edge_type='undirected')
	graph.add_edge('i', 'c', cost=2, edge_type='undirected')
	graph.add_edge('i', 'g', cost=6, edge_type='undirected')
	graph.add_edge('c', 'f', cost=4, edge_type='undirected')
	graph.add_edge('d', 'f', cost=14, edge_type='undirected')
	return graph, graph.get_vertex('a')
