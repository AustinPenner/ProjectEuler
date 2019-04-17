p_solutions = []

for i in range(0, 1001):
	p_solutions.append(0)


for a in range(1,500):
	for b in range(a,500):
		a_squared = a**2
		b_squared = b**2

		c_squared = a_squared + b_squared
		c = c_squared**.5

		if a + b + c > 1000:
			break
		elif c.is_integer():
			p = a + b + int(c)
			p_solutions[p] += 1

max_p = max(p_solutions)
p = p_solutions.index(max_p)

print max_p
print p

# Answer is: 840