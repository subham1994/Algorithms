__author__ = 'subham_1994'


# noinspection PyTypeChecker
def counting_sort(nums, bit):
	counts = [0 for _ in range(10)]
	den = pow(10, bit)
	aux = [0 for _ in nums]

	for num in nums:
		digit = (num // den) % 10
		counts[digit] += 1
	for index, _ in enumerate(counts[1:]):
		counts[index + 1] += counts[index]
	for num in reversed(nums):
		digit = (num // den) % 10
		aux[counts[digit] - 1] = num
		counts[digit] -= 1
	for index, num in enumerate(aux):
		nums[index] = num


def radix_sort(nums, bits):
	"""Least significant digit radix sort"""
	for bit in range(bits):
		counting_sort(nums, bit)


def main():
	nums = [456, 788, 409, 3, 123, 40, 150, 147]
	radix_sort(nums, 3)
	print(nums)


if __name__ == '__main__': main()
