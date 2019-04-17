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


truncatable_primes = []
num = 11

while len(truncatable_primes) < 11:

	num_list = int_to_list(num)
	num_digits = len(num_list)
	num_result = True

	for i in range(num_digits):
		num_check_f = list_to_int(num_list[i:])
		num_check_b = list_to_int(num_list[:num_digits-i])
		if not (is_prime(num_check_f) and is_prime(num_check_b)):
			num_result = False
			break

	if num_result == True:
		print(str(num))
		truncatable_primes.append(num)
	num += 2

print("The sum of all 11 truncatable primes from left or right is: " + str(sum(truncatable_primes)))

# Answer is: 748,317