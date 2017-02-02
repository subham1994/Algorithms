def partition(nums, low, high):
	x = nums[low]
	i = low
	for j in range(low + 1, high):
		if nums[j] <= x:
			i += 1
			nums[i], nums[j] = nums[j], nums[i]
	nums[low], nums[i] = nums[i], nums[low]
	return i


def quick_sort(nums, low, high):
	if low < high:
		pivot = partition(nums, low, high)
		quick_sort(nums, low, pivot)
		quick_sort(nums, pivot + 1, high)


def main():
	nums = [456, 788, 409, 3, 123, 40, 150, 147]
	quick_sort(nums, 0, len(nums))
	print(nums)


if __name__ == '__main__': main()
