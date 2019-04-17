sum = 0

for i in range(1,1001):
	number = i**i
	sum = sum + number

string_sum = str(sum)

print "The last 10 digits of the sum are: " + string_sum[-10:]

# The answer is 9,110,846,700