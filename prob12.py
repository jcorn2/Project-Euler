import math

def triangleNumber(n):
	#return nth triangle number
	return int(n * (n + 1) * 0.5)

def findNumFactors(n):
	factors = 0

	#loop to find possible factors
	for i in range(1,int(math.sqrt(float(n)))):
		#check if i divides n evenly
		if(n % i == 0):
			#found 2 factors
			factors += 2

	return factors

i = 8 

#loop until find triangle number with over 500 divisors
while(findNumFactors(triangleNumber(i)) < 500):	
	print(triangleNumber(i))
	i += 1

print("i = %d triangleNumber(i) = %d" % (i,triangleNumber(i)))

