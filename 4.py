# 4.py
# https://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
	stringNum = str(number)
	backwards = stringNum[::-1]
	if stringNum == backwards:
		return True
	else:
		return False

def largestThreeDigitProducts():
	num1 = 999
	num2 = 999
