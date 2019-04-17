# Find the first four consecutive integers to have four distinct prime factors

import math

def four_primes(n):
	primes = []
	for b in range(2,int(n**.5) + 1):
		if n % b == 0:
			primes.append(b)
			n = n / b
			while n % b == 0:
				n = n / b
	if n != 1:
		primes.append(1)
	if len(primes) == 4:
		return True
	return False

i = 10

the_answer = 0

while True:
	if four_primes(i) and four_primes(i + 1) and four_primes(i + 2) and four_primes(i + 3):
		the_answer = i
		break
	i = i + 1
	if i % 1000 == 0:
		print i

print the_answer

# The answer is 134,043