from collections import namedtuple

from DisjointSet.union_find import UnionFind
from Graphs.graph_builder import build_undirected_edge_weighted_graph


def build_sorted_edge_list_by_weight(graph):
	edge = namedtuple('Edge', 'source to weight')
	sorted_edge_list = sorted(
		[edge(vertex, nbr, vertex.get_weight(nbr)) for vertex in graph for nbr in vertex.connections()],
		key=lambda e: e.weight
	)
	return sorted_edge_list


def mst_kruskal(graph):
	mst_edges = set([])
	uf = UnionFind(graph)
	sorted_edge_list = build_sorted_edge_list_by_weight(graph)
	for edge in sorted_edge_list:
		if uf.find(edge.source) != uf.find(edge.to):
			uf.union(edge.source, edge.to)
			mst_edges.add(edge)
	return mst_edges


def main():
	graph, _ = build_undirected_edge_weighted_graph()
	assert sum(edge.weight for edge in mst_kruskal(graph)) is 37
	print('All test cases passed !')


if __name__ == '__main__':
    main()
