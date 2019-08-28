def cut_rod(prices):
	if not prices:
		return 0

	n = len(prices)
	max_price = -1

	for index, _ in enumerate(prices):
		if prices[index] + cut_rod(prices[:n - index - 1]) > max_price:
			max_price = prices[index] + cut_rod(prices[:n - index - 1])

	return max_price


def cut_rod_dp(prices):
	n = len(prices) + 1
	costs = [0] * n

	for i in range(1, n):
		for j in range(i):
			costs[i] = max(costs[i], prices[j] + costs[i - j - 1])

	return costs[-1]


def main():
	prices = [1, 5, 8, 9, 10, 17, 17, 20]

	max_price = cut_rod(prices)
	print(max_price)

	max_price = cut_rod_dp(prices)
	print(max_price)


if __name__ == '__main__':
	main()
