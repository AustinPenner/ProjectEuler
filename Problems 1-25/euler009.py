# Find the only Pythagorean triplet, {a, b, c}, for which
# a + b + c = 1000
# a^2 + b^2 = c^2


def int_check(integer):
	decimal = integer - int(integer)
	if decimal == 0.0:
		return True
	else:
		return False

a = 333

while a < 501:
	for b in range(160,a):
		c_squared = a**2.0 + b**2.0
		c = c_squared**.5
		if int_check(c):
			if a + b + c == 1000:
				print "a is " + str(a)
				print "b is " + str(b)
				print "c is " + str(c)
	a += 1


# The answer is 31875000