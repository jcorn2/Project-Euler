def findSum(n):
	Sum = 0
	for i in range(1,n):
		if(i % 3 == 0 or i % 5 == 0):
			Sum += i

	return Sum

print(findSum(1000))








