"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
shows the first 11 ugly numbers. By convention, 1 is included.
Given a number n, the task is to find n’th Ugly number.

https://www.geeksforgeeks.org/ugly-numbers/
"""


def get_nth_ugly(n):
	ugly_numbers = [1 for _ in range(n)]
	two_index, three_index, five_index, = 0, 0, 0

	for i in range(1, n):
		ugly_numbers[i] = min(ugly_numbers[two_index] * 2, ugly_numbers[three_index] * 3, ugly_numbers[five_index] * 5)
		two_index += ugly_numbers[i] == ugly_numbers[two_index] * 2
		three_index += ugly_numbers[i] == ugly_numbers[three_index] * 3
		five_index += ugly_numbers[i] == ugly_numbers[five_index] * 5

	return ugly_numbers[n - 1]


def main():
	print(get_nth_ugly(7))
	print(get_nth_ugly(10))
	print(get_nth_ugly(15))
	print(get_nth_ugly(150))


if __name__ == '__main__':
	main()
