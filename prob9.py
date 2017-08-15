#bool to know when have found a,b,c
flag = False

for a in range(1,1001):
	#check if a,b,c have been found
	if(flag):
		break
	for b in range(a + 1,1001):
		#check if a,b,c have been found
		if(flag):
			break
		for c in range(b + 1,1001):
			#check if a,b,c meet criteria 
			if(a + b + c == 1000 and (a**2 + b**2 == c**2)):
				print(a*b*c)
				flag = True
			elif(a + b + c > 1000):
				#a,b,c violate criteria
				break
