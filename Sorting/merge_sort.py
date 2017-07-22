def merge(nums, low, mid, high):
	aux = [num for num in nums]
	i, j = low, mid + 1

	for k in range(low, high + 1):
		if j > high:
			nums[k] = aux[i]
			i += 1
		elif i > mid:
			nums[k] = aux[j]
			j += 1
		elif aux[i] < aux[j]:
			nums[k] = aux[i]
			i += 1
		else:
			nums[k] = aux[j]
			j += 1


def merge_sort(nums, low, high):
	if low >= high:
		return
	mid = low + (high - low) // 2
	merge_sort(nums, low, mid)
	merge_sort(nums, mid + 1, high)
	merge(nums, low, mid, high)


def main():
	nums = [456, 788, 409, 3, 123, 40, 150, 147]
	merge_sort(nums, 0, len(nums) - 1)
	print(nums)


if __name__ == '__main__':
	main()
