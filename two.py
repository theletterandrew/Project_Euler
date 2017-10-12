# Project Euler Problem #2
# Even Fibonacci Numbers

def Fibonacci(x):
	if x <= 2:
		return x
	else:
		return Fibonacci(x-1) + Fibonacci(x-2)

def maxF():
	n = 1
	while True:
		if Fibonacci(n) >= 4000000:
			return n-1
		n+=1


maxValue = maxF()
print(maxValue)

summation = 0
for n in range(1, maxValue):
	if (Fibonacci(n)/2).is_integer() == True:
		summation += Fibonacci(n)
		print(Fibonacci(n))



print('the sum is: ' + str(summation))
