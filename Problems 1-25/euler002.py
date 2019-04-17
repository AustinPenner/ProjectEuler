cur = 1
sum = 1
total = 0

while sum < 4000000:
	prev = cur
	cur = sum
	sum = sum + prev

	if sum % 2 == 0:
		total = sum + total
	
print total

# answer is 4613732