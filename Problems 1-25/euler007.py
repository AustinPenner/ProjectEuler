elements = []

number = abs(int(raw_input("> ")))

i = 2

for prime in range(2,number):

	i = 2

	prime_num = True

	while i < prime:
		if prime % i == 0:
			prime_num = False
		i = i + 1
	if prime_num == True:
		elements.append(prime)

print elements[-1]
print len(elements)
print elements[10000]

# Answer is 104743