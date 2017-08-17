import numpy as np

def makeGrid(n):
	return np.array(np.zeros((n+1)*(n+1))).reshape((n+1),(n+1))


def bootstrapSearch(grid):
	return search(grid,(0,0))

def search(grid,currentPosition):
	leftPath = 0
	rightPath = 0

	#check if found bottom right corner
	if(currentPosition == (grid.shape[0] - 1,grid.shape[1] - 1)):	
		#print("break case")
		return 1

	#go to right path first if can
	if(currentPosition[1] < grid.shape[1]):
		#print("going right ",(currentPosition[0],currentPosition[1] + 1))
		leftPath = search(grid,(currentPosition[0],currentPosition[1] + 1))

	#go to down path first if can
	if(currentPosition[0] < grid.shape[0]):
		#print("going down ",(currentPosition[0] + 1,currentPosition[1]))
		rightPath = search(grid,(currentPosition[0] + 1,currentPosition[1]))

	#add up found left and right paths
	return leftPath + rightPath

grid = makeGrid(7)

print(bootstrapSearch(grid))








