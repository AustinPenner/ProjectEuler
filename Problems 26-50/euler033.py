numerators = []
denominators = []

# Separate digits out, check if top has same digits as bottom
# If so, remove digits and divide. If division equal to original,
# add to list
for den in range(10,100):
	for num in range(10, den):
		quotient = num*1.0/den

		den_str = str(den)
		num_str = str(num)

		if den_str[1] == '0' or num_str[1] == '0':
			quotient_check = 0
		elif den_str[0] == num_str[0]:
			quotient_check = int(num_str[1])*1.0/int(den_str[1])
		elif den_str[0] == num_str[1]:
			quotient_check = int(num_str[0])*1.0/int(den_str[1])
		elif den_str[1] == num_str[0]:
			quotient_check = int(num_str[1])*1.0/int(den_str[0])
		elif den_str[1] == num_str[1]:
			quotient_check = int(num_str[0])*1.0/int(den_str[0])
		else:
			quotient_check = 0

		if quotient == quotient_check:
			numerators.append(num)
			denominators.append(den)

print numerators
print denominators

# Output is 16/64, 26/65, 19/95, 49/98
# Reduced is 1/4, 2/5, 1/5, 1/2
#
# Multiplied is 2/200
# Reduced is 1/100
#
# Answer is: 100