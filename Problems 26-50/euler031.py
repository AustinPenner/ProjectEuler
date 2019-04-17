# Using the 1p, 2p, 5p, 10p, 20p, 50p, 1E, and 2E currency where 100p = 1E,
# how many different ways are there to make two dollars?

# We start with 1 because of the 1 10p piece
ways = 1

for a in range(0,201,1):
	for b in range(0,201,2):
		if a + b <= 200:
			for c in range(0,201,5):
				if a + b + c <= 200:
					for d in range(0,201,10):
						if a + b + c + d <= 200:
							for e in range(0,201,20):
								if a + b + c + d + e <= 200:
									for f in range(0,201,50):
										if a + b + c + d + e + f <= 200:
											for g in range(0,201,100):
												if (a + b + c + d + e + f + g) == 200:
													ways = ways + 1

print ways

# The answer is 73,682