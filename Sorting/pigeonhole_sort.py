def pigeonhole_sort(nums):
	min_num = min(nums)
	pigeonhole_size = max(nums) - min_num + 1
	pigeonholes = [0] * pigeonhole_size

	for num in nums:
		pigeonholes[num - min_num] += 1

	i = 0
	for index in range(pigeonhole_size):
		while pigeonholes[index]:
			nums[i] = index + min_num
			pigeonholes[index] -= 1
			i += 1


def main():
	nums = [456, 788, 409, 3, 123, 40, 150, 147]
	pigeonhole_sort(nums)
	print(nums)


if __name__ == '__main__':
	main()
