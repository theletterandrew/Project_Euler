# 10.py
# https://projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2+3+5+7 = 17
# Find the sum of all the primes below two million.

def primeTest(n):
	# Returns true if a number is prime
	# Borrowed from 7.py
	if n == 1:
		return False
	for i in range(2, n):
		if n%i == 0:
			return False
	return True

def sumOfPrimesBelow(n):
	# Returns a list of all prime numbers below n.
	number = 1
	summation = 0

	for i in range(n):
		if primeTest(i) == True:
			summation += i

	return summation




belowTwoM = sumOfPrimesBelow(100000)
print(belowTwoM)

# 10/18/2017 3:30 PM
# took too long to come up with an answer. changed listOfPrimesBelow(n) to be a function that returns the sumOfPrimesBelow(n)

# 10/18/2017 3:40 PM
# Still took too long to come up with an answer. Tried again with n = 100,000 @ 3:47 PM

# 10/18/2017 3:47 PM
# with n = 100,000 an answer of 454396537 is given. Also, it takes less than a minute to arrive at this solution.