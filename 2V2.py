# 2V2.py
# https://projecteuler.net/problem=2
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def Fibonacci(n):
	# Returns the nth term in the Fibonacci sequence
	if n <= 2:
		return n
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

def maxFibonacci():
	n = 1

	while Fibonacci(n) <= 4000000:
		n += 1

	return n


def main():
	summation = 0
	maxValue = maxFibonacci()

	for i in range(1, maxValue + 1):
		if Fibonacci(i) % 2 == 0:
			summation += Fibonacci(i)

	print(summation)



if __name__ == '__main__':
	main()
