# Uses python3
def fib_re(n):
	if n <= 1: return n
	return fib_re(n-1) + fib_re(n-2)


n = int(input())
print(fib_re(n))
