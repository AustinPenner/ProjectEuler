import math

def is_pandigital(n):
	# Check if number is pandigital
	n_string = str(n)
	n_list = []
	for digit in n_string:
		n_list.append(int(digit))

	ten = range(10)
	if sorted(nine) == sorted(n_list):
		return True
	else:
		return False

def list_to_str(num):
	num_string = ''.join([str(digit) for digit in num])
	return num_string


def int_to_list(num):
	num_string = str(num)
	num_list = []
	for digit in num_string:
		num_list.append(int(digit))
	return num_list


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


current_perm = range(10)
counter = 0
pandigital_sum = 0

while counter < math.factorial(10):

	current_str = list_to_str(current_perm)
	current_num = int(current_str)

	digit_groups = []
	for i in range(1, 8):
		digit_groups.append(int(current_str[i] + current_str[i+1] + current_str[i+2]))

	divisors = [2, 3, 5, 7, 11, 13, 17]

	sub_s_divisible = True
	for i in range(7):
		if digit_groups[i] % divisors[i] != 0:
			sub_s_divisible = False
			break

	if counter % 100000 == 0:
		print current_num

	if sub_s_divisible == True:
		print current_num
		pandigital_sum += current_num

	current_perm = next_permutation(current_perm)
	counter += 1

print("The sum of all valid nums is:  " + str(pandigital_sum))

# Answer is: 16,695,334,890