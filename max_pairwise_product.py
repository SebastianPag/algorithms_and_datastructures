# python3
import random

def max_pairwise_product_quadratic(numbers):
	n = len(numbers)
	max_product = 0
	if len(numbers)==1 : return numbers[0]
	for first in range(n):
		for second in range(first + 1, n):
			max_product = max(max_product,
				numbers[first] * numbers[second])
	return max_product


def max_pairwise_product_linear(numbers):
	max1, max2 = 0, 0
	if len(numbers)==1 : return numbers[0]
	for i in numbers:
		if i > max1: max1, max2 = i, max1
		elif i > max2: max2 = i
	return max1*max2	
		
def max_pairwise_product_recursive(numbers, compared=[]):
	largest = []
	comp = compared
	if len(numbers)==1 : return numbers, comp
	elif len(numbers)==0: return [1], comp
	for i in range(0, len(numbers), 2):
		try:
			x = numbers[i+1]
		except:
			x = 0
		comp.append(min(numbers[i], x))
		largest.extend([max(numbers[i], x)])
	return max_pairwise_product_recursive(largest, comp)

	
def list_generator():
	min_len, max_len = 1, 10
	min_val, max_val = 0, 1000
	max_two_list = [random.randint(min_val, max_val) for i in range(random.randint(min_len, max_len))]
	return max_two_list
		
if __name__ == '__main__':
	input_numbers = list_generator()
	print(input_numbers)
	print(max_pairwise_product_quadratic(input_numbers))
	max1, compare = max_pairwise_product_recursive(input_numbers)
	max2, _ = max_pairwise_product_recursive(compare)
	print(max1[0] * max2[0])
	print(max_pairwise_product_linear(input_numbers))