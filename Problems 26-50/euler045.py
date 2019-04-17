def is_triangle(n):
	# n = x*(x+1)/2
	# 2*n = x^2+x
	# 0 = x^2+x-2*n
	x = (-1+(1+4*2*n)**.5)/2
	return x.is_integer()


def is_pentagonal(n):
	# n = x(3x-1)/2
	# 2n = 3x^2-x
	# 0 = 3x^2-x-2n
	x = (1+(1+4*3*2*n)**.5)/(2*3)
	return x.is_integer()

def is_hexagonal(n):
	# n = x(2x-1)
	# n = 2x^2-x
	# 0 = 2x^2-x-n
	x = (1+(1+4*2*n)**.5)/(2*2)
	return x.is_integer()

hex_index = 144
hex_result = 0
while True:
	hex_result = hex_index*(2*hex_index-1)
	
	if is_pentagonal(hex_result) and is_triangle(hex_result):
		print("The next tri/pent/hex number is: " + str(hex_result))
		break
	
	hex_index += 1

# Answer is 1,533,776,805