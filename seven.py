#10,001st Prime

def primeTest(n):
	#Returns true if a number is prime
	if n == 1:
		return False
	for i in range(2, n):
		if n%i == 0:
			return False
	return True

def nthPrime(nQ):
	# Returns the nth prime number beginning with 1
	count = 1
	number = 1
	while count <= nQ:
		if primeTest(number) == True:
			# print(str(number)+ " is the " + str(count) +" prime number.")
			count +=1
		if count <= nQ:
			number+=1
	return number

print(nthPrime(10001))
