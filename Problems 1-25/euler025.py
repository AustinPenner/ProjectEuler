length = 1

i = 1
a = 1
b = 1
c = 1

while length < 1000:
	c = b
	b = b + a
	a = c
	i += 1
	length = len(str(b))

print i

# The answer is 4,782