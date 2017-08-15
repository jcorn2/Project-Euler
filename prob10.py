def isPrime(n):
	#all even numbers except 2 aren't prime
	if(n != 2 and n % 2 == 0):
		return False
	#checks if an odd number is a factor and thus n is not prime
	for i in range(3,n // 2 + 1,2):
		if(n % i == 0):
			return False
	return True

#list of primes
primes = [2]

#get primes below 2 million
for i in range(3,2000000,2):
	print(i)
	if(isPrime(i)):
		primes.append(i)

print(sum(primes))

