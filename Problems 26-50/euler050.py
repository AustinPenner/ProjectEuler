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

prime_list = []
for potential_prime in range(2,1000000):
	if is_prime(potential_prime):
		prime_list.append(potential_prime)

for num_primes in range(1000,21,-1):
	for index_a in range(len(prime_list) - num_primes - 1):
		if (sum(prime_list[index_a:num_primes + index_a]) > prime_list[-1]):
			break
		elif (sum(prime_list[index_a:num_primes + index_a]) in prime_list):
			print "largest prime is: " + str(sum(prime_list[index_a:num_primes + index_a]))
			print "number of primes is: " + str(num_primes)
			exit()

# Answer is 997,651