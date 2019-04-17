sum = 2 + 3

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


i = 5

while i < 2000000:
	if is_prime(i, sum):
		sum = sum + i
	i = i + 1

print sum

# answer is 142913828922