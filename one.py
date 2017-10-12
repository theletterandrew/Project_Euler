# summation = 0
# for x in range(1000):
# 	div3 = x/3
# 	div5 = x/5

# 	if div3.is_integer() == True or div5.is_integer():
# 		summation += x
# print(summation)

summation = 0

for x in range(1000):

	if x%3 == 0 or x%5 ==0:
		summation += x
print(summation)