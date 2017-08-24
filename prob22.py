#construct dictionary of letter values using ascii character values
letters = {chr(letter):(letter-ord('a') + 1) for letter in range(ord('a'),ord('a')+26)}

with open("names.txt","r") as names:
	#read in names to list
	namesList = names.read().replace('\"','').split(',')
	#sort list
	namesList = sorted(namesList)
	
	total = -0

	#loop through all names and calculate name score of each name
	for i in range(0,len(namesList)):
		#compute alphabetical value for name
		alpVal = sum([letters[char] for char in namesList[i].lower()])
		#calculate name score
		total += alpVal * (i+1)

	print(total)

