#Sum Square Difference

def SumOfSquares(x):
	answer = 0
	for i in range(1, x+1):
		answer+= i*i

	return answer

def SquareOfSum(x):
	summation = 0
	for i in range(1, x+1):
		summation += i

	return summation * summation

# print(SquareOfSum(10)-SumOfSquares(10))
print(SquareOfSum(100)-SumOfSquares(100))