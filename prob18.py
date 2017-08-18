
with open("triangleNumbers.txt","r") as tri:
	#store triangle as list with each row another list 
	nums = [list(map(int,line.split())) for line in tri.readlines()]
	row = len(nums) - 2

	while(row >= 0):
		#go through each number in row
		for i in range(len(nums[row])):
			#add max child below number 
			nums[row][i] += nums[row + 1][i] if nums[row + 1][i] >= nums[row + 1][i + 1] else nums[row + 1][i + 1]
		#go to row above 
		row -= 1

	print(nums[0][0])	
