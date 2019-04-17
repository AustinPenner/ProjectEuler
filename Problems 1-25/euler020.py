# Find the sum of the digits in the number 100!

i = 100

number = 1

while i > 1:
	number = number * i
	i -= 1

string = str(number)

total = 0

for j in range(len(string)):
	total = total + int(string[j])

print total

# The answer is 648