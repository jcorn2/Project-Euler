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

prime = 2
numPrime = 1

while(numPrime < 10001):
	prime = nextPrime(prime)
	numPrime += 1
	if(numPrime % 1000 == 0):
		print(numPrime)
	
print(prime)

