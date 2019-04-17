import string

f = open("p022_names.txt", "r")
names_one_line = f.read()
names_one_line = names_one_line.replace("\"","")
names = names_one_line.split(",")
names.sort()

def alph_value(name):
	# Get alphabetical value of name
	letters = len(name)
	name.upper()

	nameval = 0
	for letter in name:
		nameval += string.uppercase.index(letter) + 1
	return nameval

# Loop through names and sum alph_value * index for each
total = 0
for i in range(len(names)):
	nameval = alph_value(names[i])
	total += nameval*(i+1)

print total

# The answer is 871,198,282