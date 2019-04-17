# What is the sum of the digits of the number 2^1000 ?

bignum = 2**1000

string = str(bignum)

length = len(string)

sum = 0

for i in range(length):
	addto = int(string[i])
	sum = addto + sum

print sum

# The answer is 1,366