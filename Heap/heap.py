class Heap:
	"""min heap implementation"""

	def __init__(self):
		self._heap = []

	def size(self):
		return len(self._heap)

	def _swap(self, i, j):
		self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

	@staticmethod
	def _parent(i):
		return (i - 1) // 2

	@staticmethod
	def _left_child(i):
		return 2 * i + 1

	@staticmethod
	def _right_child(i):
		return 2 * (i + 1)

	def peek(self):
		if self.size() == 0:
			return -1

		return self._heap[0]

	def _percolate_up(self, i):
		p = self._parent(i)

		if p < 0:
			return

		if self._heap[p] > self._heap[i]:
			self._swap(p, i)

		self._percolate_up(p)

	def _percolate_down(self, i):
		l, r, smallest = self._left_child(i), self._right_child(i), i

		if l < self.size() and self._heap[l] < self._heap[smallest]:
			smallest = l
		if r < self.size() and self._heap[r] < self._heap[smallest]:
			smallest = r

		if smallest == i:
			return

		self._swap(i, smallest)
		self._percolate_down(smallest)

	def push(self, el):
		self._heap.append(el)
		self._percolate_up(self.size() - 1)

	def poll(self):
		if self.size() == 0:
			return -1

		self._swap(0, self.size() - 1)
		val = self._heap.pop()
		self._percolate_down(0)
		return val


def main():
	h = Heap()
	h.push(7)
	h.push(5)

	assert h.size() == 2
	assert h.peek() == 5
	assert h.poll() == 5
	assert h.size() == 1
	assert h.peek() == 7

	h.push(6)
	h.push(3)
	h.push(8)

	assert h.peek() == 3
	assert h.size() == 4
	assert h.poll() == 3
	assert h.peek() == 6
	assert h.size() == 3

	print("all test cases passed")


if __name__ == '__main__':
	main()
