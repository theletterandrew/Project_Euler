# 14.py
#
# Longest Collatz Sequence
#
#
# Which starting number, under one million, produces the longest chain?

def generateSequence(n):
	# Generates a Collatz sequence for a given number n.
	sequence = []
	sequence.append(n)
	while n != 1:
		if n % 2 == 0:
			n = n/2
			sequence.append(n)
		else:
			n = 3 * n + 1
			sequence.append(n)

	return len(sequence)


maxLength = 0
number = 0

for i in range(1, 1000001):
	length = generateSequence(i)

	if length > maxLength:
		maxLength = length
		number = i

print(number)

# 10/20/2017 11:30 AM
# Tested with n <= 100,000 and received a value of 77031 in 6.4s.

# 10/20/2017 11:30 AM
# with n <= 1,000,000 I received a value of 837799 in 75.8 s