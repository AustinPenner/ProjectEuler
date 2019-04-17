# Find sum of numbers that can be written as the fifth power
# of their digits (only five-digit numbers to be used)

sum0 = 0

# For all the numbers in this range
for a in range(2,1000000):
	string = str(a)

	# Take each digit in the number and take their fifth power, then add them
	sum2 = 0
	for b in range(len(str(a))):
		sum2 += (int(string[b]))**5
		
	# If this sum equals the original number, then add this number to sum0
	if sum2 == a:
		sum0 += a

print sum0

# The answer is 443,839