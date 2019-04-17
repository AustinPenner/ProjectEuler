decimals = ""

a = 1

while a <= 1000000:
	decimals = decimals + str(a)
	a += 1

product = int(decimals[0]) * int(decimals[9]) * int(decimals[99]) * int(decimals[999]) * int(decimals[9999]) * int(decimals[99999]) * int(decimals[999999])
print product

# The answer is 210