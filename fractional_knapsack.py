#python3
import sys

def get_optimal_value(capacity, weights, values, number_items):
	total_value = 0
	rel_val = {values[i]/weights[i]:[values[i],weights[i]] for i in range(len(weights))}
	check = 0
	
	while check < number_items:
		n = max(rel_val.keys())
		
		if rel_val[n][1] <= capacity:
			capacity -= rel_val[n][1]	#index 1 weight
			total_value += rel_val[n][0]#index 0 value
		elif rel_val[n][1] > capacity:
			for i in reversed(range(rel_val[n][1])):
				if rel_val[n][1] <= capacity:
					capacity -= rel_val[n][1]	#index 1 weight
					total_value += rel_val[n][0]#index 0 value
		
		rel_val.pop(n)
		check += 1
	print(total_value, capacity, rel_val)

	
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values, n)
    #print("{:.10f}".format(opt_value))
