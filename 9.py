# 9.py
# https://projecteuler.net/problem=9
#
# A Pythagorean triplet is a set of three natural numbers a<b<c, for which a^2 +b^2 = c ^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a+b+c = 1000.
# Find the product abc.

def checkSum(a, b, c):
	# Function returns True if a, b, and c add together to get 1000.
	if a+b+c == 1000:
		return True
	else:
		return False

def checkTriplet(a, b, c):
	# Function returns True if a, b, and c are a Pythagorean triplet (a^2 +b^2 = c^2)
	if a**2+b**2 == c**2:
		return True
	else:
		return False

print(checkTriplet(3,4,5))