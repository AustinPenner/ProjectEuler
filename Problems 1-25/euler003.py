# What is the largest prime factor of the number 600851475143

def is_prime(n):
	n = abs(int(n))

	if n < 2:
		return False
	elif n == 2:
		return True
	elif n % 2 == 0:
		return False
	# only need to check integers 3 through sqrt(n) + 1, (skipping even numbers)
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True


# Take the number 600851475143 and divide it by the first prime,
# and then the next, until the remaining number is a prime.

i = 5

div = 600851475143

while i < 775146:
	if is_prime(i):
		if div % i == 0:
			div = div / i
			print div
	i = i + 1

# answer is 6857