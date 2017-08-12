def isPalindrome(n):
	nStr = str(n)
	#make use of string slicing to reverse number
	return (nStr == nStr[::-1])

threeDigitNums = range(100,1000)
#list of all multiplications of 3 digit numbers
products = [i * j for i in threeDigitNums for j in threeDigitNums]
products.sort()

#find first palindrome amoung multiplication list
for i in reversed(products):
	if(isPalindrome(i)):
		print(i)
		break

