def min_coins_needed_to_get_exact_change(denominations, amount):
	max_val = 1 << 31
	min_cost = [max_val] * (amount + 1)
	denominations_used = [max_val] * (amount + 1)

	min_cost[0] = 0

	for coin in denominations:
		for a in range(coin, amount + 1):
			if min_cost[a - coin] != max_val and min_cost[a - coin] + 1 < min_cost[a]:
				min_cost[a] = min_cost[a - coin] + 1
				denominations_used[a] = coin

	return min_cost[-1]


def num_ways_to_get_a_change(denominations, amount):
	ways = [0] * (amount + 1)
	ways[0] = 1

	for coin in denominations:
		for w in range(coin, amount + 1):
			ways[w] += ways[w - coin]

	return ways[-1]


def can_make_change(denominations, amount):
	possible = [False] * (amount + 1)
	possible[0] = True

	for coin in denominations:
		for w in range(coin, amount + 1):
			possible[w] = possible[w] or possible[w - coin]

	return possible[-1]


def main():
	denominations, amount = [1, 5, 12, 25], 16
	num_coins = min_coins_needed_to_get_exact_change(denominations, amount)
	print(num_coins)

	denominations, amount = [1, 2, 3], 4
	num_ways = num_ways_to_get_a_change(denominations, amount)
	print(num_ways)

	denominations, amount = [2, 5, 3, 6], 10
	num_ways = num_ways_to_get_a_change(denominations, amount)
	print(num_ways)


if __name__ == '__main__':
	main()
