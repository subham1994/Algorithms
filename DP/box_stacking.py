class Box:
	def __init__(self, h, w, d):
		self.h = h
		self.w = w
		self.d = d

	def get_area(self):
		return self.d * self.w

	def __lt__(self, other):
		return self.get_area() < other.get_area()

	def __repr__(self):
		return f"Box<h={self.h}, w={self.w}, d={self.d}>"


def get_max_stack(boxes, stacks, max_stack_heights, max_stack_height):
	index_of_topmost_box = max_stack_heights.index(max_stack_height)

	boxes_in_max_stack = []

	while stacks[index_of_topmost_box] != -1:
		boxes_in_max_stack.append(boxes[index_of_topmost_box])
		index_of_topmost_box = stacks[index_of_topmost_box]
	boxes_in_max_stack.append(boxes[index_of_topmost_box])

	return list(reversed(boxes_in_max_stack))


def stack_boxes(dimensions):
	boxes = []

	for h, d, w in dimensions:
		boxes.append(Box(h, max(d, w), min(d, w)))
		boxes.append(Box(d, max(h, w), min(h, w)))
		boxes.append(Box(w, max(d, h), min(d, h)))

	boxes.sort(reverse=True)

	max_stack_heights = [box.h for box in boxes]
	stacks = [-1 for _ in boxes]

	for i, curr_box in enumerate(boxes):
		for j, prev_box in enumerate(boxes[:i]):
			if curr_box.w < prev_box.w and curr_box.d < prev_box.d:
				if max_stack_heights[j] + curr_box.h > max_stack_heights[i]:
					max_stack_heights[i] = max_stack_heights[j] + curr_box.h
					stacks[i] = j

	max_stack_height = max(max_stack_heights)
	boxes_in_max_stack = get_max_stack(boxes, stacks, max_stack_heights, max_stack_height)

	return max_stack_height, boxes_in_max_stack


def main():
	dimensions = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
	max_height, boxes_in_max_stack = stack_boxes(dimensions)
	print(max_height, boxes_in_max_stack)

	dimensions = [[1, 2, 4], [3, 2, 5]]
	max_height, boxes_in_max_stack = stack_boxes(dimensions)
	print(max_height, boxes_in_max_stack)


if __name__ == '__main__':
	main()
