#python 3
import sys
sys.setrecursionlimit(10000)

def greatest_common_divisor(a,b):
	#assumes that neither a nor b are zero

	if a == 0:
		return b
	elif b == 0:
		return a
	else:
		return greatest_common_divisor(a-b, b) if a > b else greatest_common_divisor(a, b - a)

if __name__ == "__main__":
	a = int(input())
	b = int(input())
	
	print(greatest_common_divisor(a,b))
