# Smallest Multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallestMultiple(n):
	increment = 1
	while True:
		for i in range(1, n+1):
			if increment % i == 0:
				if i == n:
					return increment
			else:
				break
		increment +=1


# print(smallestMultiple(20))
# 232792560
# [Finished in 296.2s]