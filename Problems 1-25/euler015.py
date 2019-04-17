triangle = [[],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]

for i in range(1,42):
	triangle[0].append(1)

for i in range(1,42):
	length = len(triangle[i-1])
	for j in range(1, length - 1):
		left = triangle[i-1][j]
		right = triangle[i][j-1]
		triangle[i].append(left + right)

for a in range(42):
	print len(triangle[a])

print triangle[20][20]

# The answer is 137846528820