# Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# PrimeTest Function borrowed from my code for seven.py

def primeTest(n):
	#Returns true if a number is prime
	if n == 1:
		return False
	for i in range(2, n):
		if n%i == 0:
			return False
	return True

def lpf(x):
	for i in range(x, 2, -1):
		