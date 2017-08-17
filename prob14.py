def collatz(n):
	seq = [n]
	while(n != 1):
		#even number: divide by 2
		if(n % 2 == 0):
			n = n // 2
		#odd number: times 3 + 1
		else:
			n = 3 * n + 1
		#add new n to sequence
		seq.append(n)

	return seq

maxSeqLength = 0
startingNum = 0

#calculates collatz sequence length of all natural numbers below 1 million
for i in range(1,1000000):
	seqLength = len(collatz(i))
	#check if found bigger seq length
	if(seqLength > maxSeqLength):
		maxSeqLength = seqLength
		startingNum = i

print("Starting Num: ",startingNum)
print("Sequence Length: ",maxSeqLength)




