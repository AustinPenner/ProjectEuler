# Find the sum of all amicable pairs under 10000

sum0 = 0

# For the numbers 3 through 10,000, add the proper divisors of each number.
for a in range(3,10000):
	sum1 = 1
	sum2 = 1
	for b in range(2,a):
		if a % b == 0:
			sum1 = sum1 + b

	# Running the same process with the sum of the proper divisors (sum1)
	# and then checking if the sum of proper divisors of sum1 are equal to a
	for c in range(2,sum1):
		if sum1 % c == 0:
			sum2 = sum2 + c
	if sum2 == a and a != sum1:
		sum0 = sum0 + a
		print a

print sum0

# The answer is 31,626