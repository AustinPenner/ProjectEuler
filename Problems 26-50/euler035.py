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


def list_to_int(num):
	num_string = ''.join([str(digit) for digit in num])
	return int(num_string)


def int_to_list(num):
	num_string = str(num)
	num_list = []
	for digit in num_string:
		num_list.append(int(digit))
	return num_list


circular_prime_count = 1

# Checking odd numbers only. We start the count at 1 to include 2.
for num in range(3, 1000000, 2):
	num_list = int_to_list(num)
	num_digits = len(num_list)
	num_result = True

	# Rotate once for each digit. If not prime, False.
	for d in range(num_digits):
		num_check = list_to_int(num_list)

		if is_prime(num_check):
			num_list.insert(0, num_list.pop())
		else:
			num_result = False
			break

	if num_result == True:
		print num
		circular_prime_count += 1

print circular_prime_count

# The answer is 55