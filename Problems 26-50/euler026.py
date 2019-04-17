def cycleLength(divisor, dividend):

	dividend_list = []
	quotient_list = []

	while not dividend in dividend_list:
		if dividend // divisor == 0:
			dividend = dividend*10
		else:
			dividend_list.append(dividend)
			quotient_list.append(dividend // divisor)
			remainder = dividend % divisor

			if remainder == 0:
				return 0

			dividend = remainder

	cycle_start = dividend_list.index(dividend)
	cycle_length = len(dividend_list) - cycle_start

	return cycle_length


d_longest_cycle = 0

for d in range(6, 1000):
	d_cycle_length = cycleLength(d, 1)
	if d_cycle_length > d_longest_cycle:
		d_longest_cycle = d_cycle_length
		print(str(d) + " has cycle length " + str(d_cycle_length))

# Answer is: 983