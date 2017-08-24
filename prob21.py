import math

def findProperDivisors(n):
	#always have 1 as proper divisior
	factors = [1]

	#loop to find possible factors
	for i in range(2,int(math.sqrt(float(n)) + 1)):
		#check if i divides n evenly
		if(n % i == 0):
			#found 2 proper divisors 
			factors.append(i)
			factors.append(n // i)

	return factors


nums = list(range(1,10001))
amicableNums = set()

while(len(nums) > 0):
	#get next number to check 
	a = nums.pop()
	b = sum(findProperDivisors(a))
	#check if sum of divisors of b is equal to a 
	if(a != b and a == sum(findProperDivisors(b)) and b <= 10000):
		#d(a) = b and d(b)=a => a and b are amicable numbers
		amicableNums.add(a)
		amicableNums.add(b)
		#remove b from list of numbers
		if(b in nums):
			nums.remove(b)

print(sum(amicableNums))


