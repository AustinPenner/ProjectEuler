import math

def to_binary(number):
	binary = ""
	i = 1
	while i < number:
		i = i * 2
	length = math.log(i,2)
	
	j = 0
	while j < length:
		i = i / 2
		if max(i,number) == number:
			binary = binary + "1"
			number = number - i
		else:
			binary = binary + "0"
		j += 1
	return binary

def is_pal(number):
	string = str(number)
	length = len(string)
	
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
		
		if word1 == word2:
			return True
		else:
			return False
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

sum = 1+3+5+7+9

for a in range(10,1000001):
	if is_pal(a):
		if is_pal(to_binary(a)):
			sum = sum + a

print sum

# The answer is 872,187