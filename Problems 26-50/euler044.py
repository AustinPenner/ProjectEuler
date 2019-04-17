# Return true iff a number n is pentagonal
def is_pentagonal(n):
	# n = x(3x-1)/2
	# 2n = 3x^2-x
	# 0 = 3x^2-x-2n
	x = (1+(1+4*3*2*n)**.5)/(2*3)
	return x.is_integer()

# Calculate the nth pentagonal number
def get_pentagonal(n):
	return n*(3*n-1)/2

# 1. Enumerate pentagonal numbers one at a time
# 2. Using the largest pentagonal number so far, iterate
#    through all smaller pentagonal numbers. 
# 3. Find the difference and sum of these numbers.
# 4. If both are pentagonal, return the difference.
def pentagonal_range(upper):
	pentagonal_nums = [0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145]


	for n in range(10, upper):
		for m in range(1, n):
			pent_n = pentagonal_nums[n]
			pent_m = pentagonal_nums[m]

			pent_sum = pent_n + pent_m
			pent_diff = pent_n - pent_m

			if is_pentagonal(pent_diff):
				if is_pentagonal(pent_sum):
					print("Pj is: " + str(pent_n))
					print("Pk is: " + str(pent_m))
					print("Difference is: " + str(pent_diff))

		pentagonal_nums.append(get_pentagonal(n+1))


pentagonal_range(100000)


# Answer is: 5,482,660