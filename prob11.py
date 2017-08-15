import numpy as np
import functools
import re

#read in long number
ofile = open("grid.txt","r")
num = ofile.read()
#remove non-numeric characters
num = re.sub('\\[a-z]','',num)

#turn num to 20x20 grid using numpy array
grid = list(map(int,num.split()))
grid = np.array(grid).reshape((20,20))

#list of lines of numbers to check for products
lines = []

#add rows to lines
for i in range(grid.shape[0]):
	lines.append(list(grid[i,]))

#add cols to lines
for i in range(grid.shape[1]):
	lines.append(list(grid[:,i]))

#add diagonals to lines
for i in range(-grid.shape[0]+1,grid.shape[0]):
	#only append diagonals if have more than 4 elements
	diag = list(np.diag(grid,k=i))
	if(len(diag) >= 4):
		lines.append(diag)

#add diagonals to lines
for i in range(-grid.shape[0]+1,grid.shape[0]):
	#only append diagonals if have more than 4 elements
	diag = list(np.diag(np.fliplr(grid),k=i))
	if(len(diag) >= 4):
		lines.append(diag)

products = []

#calculate 4 number adjacent products among all lines
for line in lines:
	start = 0
	stop = 4
	while(stop <= len(line)):
		#calculate product
		products.append(functools.reduce(lambda x,y: x*y,line[start:stop]))
		start += 1
		stop += 1

print(max(products))

