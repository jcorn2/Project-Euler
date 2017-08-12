from functools import reduce

def isPrime(n):
	#all even numbers except 2 aren't prime
	if(n != 2 and n % 2 == 0):
		return False
	#checks if an odd number is a factor and thus n is not prime
	for i in range(3,n // 2 + 1):
		if(n % i == 0):
			return False
	return True

def primeFactorization(n):
	#if n is prime, then only return n
	if(isPrime(n)):
		return [n]

	factors = []
	#get all potential prime factors of n
	primes = [i for i in range(2,n // 2 + 1) if(isPrime(i))]

	for prime in primes:
		value = n
		#determine if prime divides value
		while(value % prime == 0):
			factors.append(prime)
			#update value to value / prime
			value /= prime	
	return factors 

def findSmallestNumber(n):
	#number to find smallest multiple of
	nums = list(range(2,n+1))
	largestMultiples = []
	while(len(nums) > 0):
		num = nums[0]
		largest = num
		#find largest num^n in nums
		while(largest*num in nums):
			largest *= num
		largestMultiples.append(largest)
		#remove all numbers from nums that num divides evenly 
		nums = [i for i in nums if i % num != 0]

	#reduce numbers in largestMultiples to its prime factorization and concats it to one list
	primeFactorizationList = []
	for mult in largestMultiples:
		primeFactorizationList += primeFactorization(mult)

	#smallest number is product of primeFactorizationList numbers	
	return reduce(lambda x,y: x*y,primeFactorizationList)

print(findSmallestNumber(20))

