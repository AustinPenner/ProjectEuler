# Find the sum of all the numbers which are equal to the sum of the factorial
# of their digits. 145 = 1! + 4! + 5!

def factorial(c):
	mult = 1
	while c > 1:
		mult = mult * c
		c = c - 1
	return mult

sum0 = 0

a = 3

# All 9's is the largest possible result for a given number
# of digits.
# Factorial sum of   999,999 is 2,177,280
# Factorial sum of 9,999,999 is 2,540,160
# So we restrict our search to numbers less than 2,540,160.

while a <= 2540160:
	string = str(a)
	digits = len(str(a))
	sum1 = 0
	for b in range(digits):
		sum1 = sum1 + factorial(int(string[b]))
	if sum1 == a:
		sum0 = sum0 + a
	a += 1
	
print sum0
# The answer is 40,730