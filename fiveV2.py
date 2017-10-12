# Smallest Multiple
# After deciding my first approach was too slow (296.2 S!) I decided to come up with a faster way to
# return the answer rather than brute force it.

import math

def divisibilityTest(n, x):
	for i in range(1, x+1):
		if n % i == 0:
			if i == x:
				return True
		else:
			return False

def smallestMultiple(nQ):
	sm = math.factorial(nQ)
	for i in range(nQ, 1, -1):
		if divisibilityTest(sm/i, nQ) == True:
			sm /= i
			i+=1
	return sm

print(smallestMultiple(20))