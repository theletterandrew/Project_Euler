# 16.py
# https://projecteuler.net/problem=16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000?

largeNumber = 2**1000

digits = [int(d) for d in str(largeNumber)]

summation = sum(digits)
print(summation)

# 10/20/2017 11:38 AM
# Answer received = 1366