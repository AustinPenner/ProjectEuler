nonrepeats = '.'
total = 0

for a in range(2,101):
	for b in range(2,101):
		numb = str(a**b)
		if nonrepeats.find('.' + numb + '.') == -1:
			nonrepeats = '.' + numb + nonrepeats
			total = total + 1

print total


# The answer is 9,183