#python 3
import sys
sys.setrecursionlimit(10001)
fib = {}

def fib_last_digit(n):
	
	if n == 1: 
		fib[n] = 1
		return fib[n]
	elif n == 0:
		fib[n] = 1
		return fib[n]
	elif n in fib:
		return fib[n]
	else:
		val = fib_last_digit(n-1) + fib_last_digit(n-2)
		fib[n] = val
		return val
		
n = int(input())
print(fib_last_digit(n)%10)
#print(fib)