#python3

def least_common_mult_stupid(a,b):
	for i in range(1,a):
		for j in range(1,b):
			if a*i == b*j: return b*i

			
def least_common_mult(a,b):
	#using (a/gcd)*b; gcd implemented using iterative euclidean algo
	gcd = euclidean_gcd(a,b)
	return (a/gcd)*b


def euclidean_gcd(a,b):
	if a == 0: return b
	else:
		while(b != 0):
			if a > b: a -= b
			else: b -= a
		return a
	
if __name__ == "__main__":
	a, b = int(input()), int(input())
	print(least_common_mult(a,b))