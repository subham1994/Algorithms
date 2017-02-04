from Graphs.graph_builder import build_directed_graph
from Graphs.topological_sort import topological_sort


"""
	Kosaraju-Sharir Algorithm:
        Intuition
            - Strong components in graph G are same as in reverse(G).

        Method
            - compute reverse postorder in reverse(G).
            - run DFS in G, visiting unmarked vertices in reverse postorder of revrese(G).

        Time Complexity:
            - The above algorithm is linear time, two pass alogrithm. It calls DFS, finds reverse of
              the graph and again calls DFS. DFS takes O(V+E) for a graph represented using adjacency list.
              Reversing a graph also takes O(V+E) time.
"""


ids = {}


def strongly_connected(u, v):
	return ids.get(u) == ids.get(v)


def dfs(source, count):
	source.color = 'gray'
	ids[source] = count
	for neighbour in source.connections():
		if neighbour.color == 'white':
			neighbour.parent = source
			dfs(neighbour, count)
	source.color = 'black'


def strongly_cc(graph):
	reverse_postorder = map(lambda v: graph.get_vertex(v.id), topological_sort(graph.reverse()))
	for index, vertex in enumerate(reverse_postorder):
		if vertex.color == 'white':
			dfs(vertex, index)


def main():
	graph, _ = build_directed_graph()
	strongly_cc(graph)
	assert strongly_connected(graph.get_vertex('v'), graph.get_vertex('x'))
	assert strongly_connected(graph.get_vertex('v'), graph.get_vertex('y'))
	assert strongly_connected(graph.get_vertex('x'), graph.get_vertex('y'))
	assert not strongly_connected(graph.get_vertex('x'), graph.get_vertex('z'))
	print('All test cases passed')


if __name__ == '__main__':
    main()
