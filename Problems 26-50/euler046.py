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


def golbach_other(num):
	# check if number is sum of prime and twice a square
	for i in range(2, num):
		for j in range(1, num):
			numcheck = i + 2*(j**2)

			if numcheck > num:
				break
			elif not is_prime(i):
				pass
			elif numcheck == num:
				return True
	return False


# Loop through odd composite numbers. Try writing this as the sum of 
# a prime and two times a square. If no valid sum, return the value. 
this_num = 9
while True:
	if ((this_num - 1) % 100 == 0):
		print this_num

	if is_prime(this_num):
		this_num += 2
	elif golbach_other(this_num):
		this_num += 2
	else:
		print("The first odd composite that violates Golbachs other conjecture is " + str(this_num))
		break

# Answer is 5777