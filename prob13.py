import numpy as np
import functools
import re

#read in long number
ofile = open("numbers.txt","r")
num = ofile.read()
#remove non-numeric characters
num = re.sub('[^0-9]','',num)

#store numbers as 2d arrays  
grid = list(map(int,list(num)))
grid = np.array(grid).reshape(100,50)

Sum = [] 
carry = 0

#do addition one columns at a time, storing sum in Sum list
for i in range(50):
	Sum.append(sum(grid[:,grid.shape[1] - i - 1],carry) % 10)
	#number to carry over 
	carry = sum(grid[:,grid.shape[1] - i - 1],carry) // 10 

#add final carry if not zero
if(carry != 0):
	Sum.append(carry)

#have sum right way
Sum = list(reversed(Sum))

print(Sum)

