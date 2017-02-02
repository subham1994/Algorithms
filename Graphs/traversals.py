from queue import Queue

from Graphs.graph_builder import build_directed_graph


def bfs(source):
	q = Queue()
	source.distance = 0
	source.color = 'gray'
	q.put(source)

	while not q.empty():
		u = q.get()
		for neighbor in u.connections():
			if neighbor.color == 'white':
				neighbor.parent = u
				neighbor.distance = u.distance + 1
				neighbor.color = 'gray'
				q.put(neighbor)
		u.color = 'black'


def dfs(source):
	source.color = 'gray'
	for neighbour in source.connections():
		if neighbour.color == 'white':
			neighbour.parent = source
			dfs(neighbour)
	source.color = 'black'


def main():
	# build directed graph for dfs
	_, dfs_source = build_directed_graph()
	assert dfs_source
	dfs(dfs_source)

	# build directed graph for bfs
	_, bfs_source = build_directed_graph()
	assert bfs_source
	bfs(bfs_source)


if __name__ == '__main__':
    main()
