sum1 = 0
sum2 = 0

for i in range(1,101):
	mult = i * i
	sum1 = mult + sum1

for i in range(1,101):
	sum2 = i + sum2

print (sum2 * sum2) - sum1

# answer is 25164150