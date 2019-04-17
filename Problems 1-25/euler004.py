def is_pal(number):
	number = int(number)
	string = str(number)
	length = len(string)

#	If number has even number of digits, it should be checked if
#	the first half is equal to the reverse of the second half
	if length % 2 == 0:
		i = 0
		word1 = ""
		word2 = ""
		half = length / 2
		while i < half:
			word1 = word1 + string[i]
			i = i + 1
		
		while (length - 1) > (half - 1):
			word2 = word2 + string[length - 1]
			length = length - 1
		
		if int(word1) == int(word2):
			return True
		else:
			return False
#	This takes odd digit numbers and runs them as even digit
#	numbers, removing the middle number.
	else:
		odd = length / 2
		string = string[:odd] + string[odd + 1:]
		length = length - 1
		
		i = 0
		word1 = ""
		word2 = ""
		half = length / 2
		while i < half:
			word1 = word1 + string[i]
			i = i + 1
		
		while (length - 1) > (half - 1):
			word2 = word2 + string[length - 1]
			length = length - 1
		
		if word1 == word2:
			return True
		else:
			return False

# If two numbers make a palindrome when multiplied
# their product replaces product1
product1 = 1

j = 999

while j > 900:
	for k in range(900,j + 1):
		product2 = j * k
		if is_pal(product2):
			if product2 > product1:
				product1 = product2
	j -= 1

print product1

# The answer is 906609