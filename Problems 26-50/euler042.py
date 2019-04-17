def is_triangle(word):
	alphabet = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	letter_sum = 0
	
	for letter in word:
		letter_sum += alphabet.index(letter)

	# Triangle numbers:
	# n = x*(x+1)/2
	# 2*n = x^2+x
	# 0 = x^2+x-2*n
	# Quadratic formula:
	x = (-1+(1+4*2*letter_sum)**.5)/2
	return x.is_integer()


with open("euler042_words.txt", "r") as file:
	line = file.readline()
	
line = line.replace("\"","")
line = line.split(",")

# Loop through each word, add 1 if it's a triangle number
count = 0
for word in line:
	if is_triangle(word):
		count += 1

print count

# Answer is: 162