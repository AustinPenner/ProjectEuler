def collatz(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3*n + 1

maximum = 1

number = 1

for n in range(1000000,800000,-1):
	count = 2
	m = n

	while collatz(n) != 1:
		n = collatz(n)
		count = count + 1
		collatz(n)
	if count > maximum:
		maximum = count
		number = m
		print maximum
		print number

print "The largest amount of steps is " + str(maximum)
print "The number is " + str(number)

# The answer is 837799