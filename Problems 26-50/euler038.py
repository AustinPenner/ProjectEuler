def is_pandigital(n):
	# Check if number is pandigital
	n_string = str(n)
	n_list = []
	for digit in n_string:
		n_list.append(int(digit))

	nine = range(1,10)
	if sorted(nine) == sorted(n_list):
		return True
	else:
		return False


def list_to_int(num):
	num_string = ''.join([str(digit) for digit in num])
	return int(num_string)


def int_to_list(num):
	num_string = str(num)
	num_list = []
	for digit in num_string:
		num_list.append(int(digit))
	return num_list


def concatenated_product(i, n):
	# Return the concatenated product of i and (1, 2, ..., n)
	n_tup = range(1, n+1)
	prod = []

	for d in range(n):
		prod.append(n_tup[d]*i)

	concat_prod = ''.join([str(element) for element in prod])
	return int(concat_prod)

largest_pandigital = 0

for i in range(1, 100000):
	for n in range(2,10):
		concat_prod = concatenated_product(i, n)

		if concat_prod >= 100000000 and concat_prod < 1000000000:
			if is_pandigital(concat_prod) and concat_prod > largest_pandigital:
				largest_pandigital = concat_prod
				print concat_prod

# Answer is: 932,718,654