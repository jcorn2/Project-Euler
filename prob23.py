import math

UPPERLIMIT = 28123

def findProperDivisors(n):
	#always have 1 as proper divisior
	factors = set([1])

	#loop to find possible factors
	for i in range(2,int(math.sqrt(float(n)) + 1)):
		#check if i divides n evenly
		if(n % i == 0):
			#found 2 proper divisors 
			factors.add(i)
			factors.add(n // i)

	return factors


abundantNums = []

for i in range(2,UPPERLIMIT + 1):
	#find sum of proper divisors of i 
	sumDivisors = sum(findProperDivisors(i))
	#check if sum is > i 
	if(sumDivisors > i):
		abundantNums.append(i)

print(len(abundantNums))

#nums = list(range(1,UPPERLIMIT)
nums = set()

#create all possible sums of abundant numbers below UPPPERLIMIT
for anum1 in abundantNums:
	for anum2 in abundantNums:
		if(anum1 + anum2 <= UPPERLIMIT):
			nums.add(anum1 + anum2)

#print sum of numbers not in nums
print(sum([i for i in range(1,UPPERLIMIT+1) if(i not in nums)]))
 
