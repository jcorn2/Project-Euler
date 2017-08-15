import functools
import re

start = 0
stop = 13

#read in long number
ofile = open("longNumber.txt","r")
num = ofile.read().strip()
#remove non-numeric characters
num = re.sub('[^0-9]','',num)

adjPermutations = []

#get all possible 13 adajecent numbers permutations	
while(stop < len(num)):
	adjPermutations.append(num[start:stop])
	start += 1
	stop += 1

products = []

#calculate product of each permutation
for number in adjPermutations:
	#split up number to individual digits and cast to int
	digits = list(map(int,list(number)))

	#append product to list of products
	products.append(functools.reduce(lambda x,y:x*y,digits))

print(max(products))



