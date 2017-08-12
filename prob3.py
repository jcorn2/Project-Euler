def isPrime(n):
	#all even numbers except 2 aren't prime
	if(n != 2 and n % 2 == 0):
		return False
	#checks if an odd number is a factor and thus n is not prime
	for i in range(3,n // 2 + 1):
		if(n % i == 0):
			return False
	return True

def nextPrime(n):
	#special case for 2, only need to add 1
	if(n == 2):
		return 3
	newPrime = n + 2

	#checks each successive odd number until next prime is found	
	while(not isPrime(newPrime)):
		newPrime += 2

	return newPrime

def findFactors(n):
	val = n
	i = 2

	#if val == i, then found largest prime divisor
	while(val != i):
		#prime number i is no longer a factor of val, try next prime
		if(val % i != 0):
			i = nextPrime(i)
		#val is still divisible by i
		else:
			val /= i
	return i 
	
print(findFactors(600851475143))
