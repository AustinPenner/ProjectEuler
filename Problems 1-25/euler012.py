biggest = 0

def triangle(z):
	global biggest
	list = []
	
	for c in range(1,int(z**.5) + 1):
		if z % c == 0:
			list.append(c)
			if c**2 != z:
				list.append((z / c))
	length = len(list)
	if length >= biggest:
		biggest = length
		print "%r is the triangle with the most divisors (at %r) so far" % (z, length)

a = 2001000
b = 2001

while a < 100000000:
	triangle(a)
	a = a + b
	b = b + 1


# The answer is 76,576,500