#python3

def cashier(n):
	change = {}
	coins = [10,5,1]
	for i in range(len(coins)):
		change[str(coins[i])] = int(n/coins[i])
		n -= int(n/coins[i])*coins[i]
		print(n)
	return change

if __name__ == "__main__":
	n = int(input())
	print(cashier(n))