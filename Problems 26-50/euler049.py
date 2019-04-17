def is_prime(n):
	if n < 2:
		return False
	elif n == 2 or n == 3:
		return True
	elif (n + 1) % 6 != 0 and (n - 1) % 6 != 0:
		return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True

def prime_list(start, finish):
	primes = []
	for potential_prime in range(start,finish):
		if is_prime(potential_prime):
			primes.append(potential_prime)
	return primes

def is_permutation(num1, num2):
	numba1 = str(num1)
	numba2 = str(num2)
	return sorted(numba1) == sorted(numba2)

prime_list = prime_list(1000,10000)

for difference in range(1,3401):
	for index_a in range(len(prime_list) - 1):
		first = prime_list[index_a]
		second = first + difference
		third = second + difference
		if (third > 10000):
			break
		elif (is_prime(second) and is_prime(third)):
			if (is_permutation(first, second) and is_permutation(first, third)):
				print "first prime: %d, second prime: %d, third prime: %d" % (first, second, third)

# The answer is 296,962,999,629