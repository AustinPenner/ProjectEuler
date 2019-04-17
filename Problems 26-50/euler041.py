import math

# Check if number is prime
def is_prime(n):
	if n < 2:
		return False
	# if integer is 2 or 3, then True
	elif n == 2:
		return True
	elif n == 3:
		return True
	# if integer is even, then False
	elif n % 2 == 0:
		return False
	# only check integers 3 through sqrt(n) + 1, skipping even numbers
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True

# Calculates the next permutation using lexicographical ordering
def next_permutation(num):
	size = len(num)

	for idx in reversed(range(1, size)):

		if num[idx-1] < num[idx]:
			# 1. Get the next biggest number after index(idx-1)
			next_largest = max(num)
			for i in range(idx, size):
				if num[i] > num[idx-1] and num[i] <= next_largest:
					next_largest = num[i]

			# 2. Move this number before idx-1
			next_largest_idx = num.index(next_largest)
			num.insert(idx-1, num.pop(next_largest_idx))

			# 3. Sort the sublist after idx-1
			num[idx:] = sorted(num[idx:])

			return num

	return num


nine = [1,2,3,4,5,6,7,8,9]
eight = [1,2,3,4,5,6,7,8]
seven = [1,2,3,4,5,6,7]
# Tried for all 9-digit and 8-digit pandigital numbers which yielded
# no primes. 7-digit pandigitals did.


counter = 1
perm = seven


# Loop through all n-digit pandigital numbers and print if prime.
while counter < math.factorial(len(perm)):
	perm = next_permutation(perm)

	perm_string = ''.join([str(digit) for digit in perm])
	perm_number = int(perm_string)

	if is_prime(perm_number):
		print perm_number

	counter += 1

# Answer is: 7,652,413