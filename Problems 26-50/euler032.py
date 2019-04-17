def is_pandigital(n_string):
	# Check if number is pandigital
	n_list = []
	for digit in n_string:
		n_list.append(int(digit))

	nine = range(1,10)
	if sorted(nine) == sorted(n_list):
		return True
	else:
		return False

prod_list = []

for i in range(1, 100):
	for j in range(i, 10000):
		prod = i*j

		concat = str(i) + str(j) + str(prod)

		if is_pandigital(concat):
			if not prod in prod_list:
				prod_list.append(prod)


print sum(prod_list)

# Anser is: 45,228