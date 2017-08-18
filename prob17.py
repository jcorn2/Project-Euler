import inflect

letters = 0
inflectEngine = inflect.engine()

for i in range(1,1001):
	#use inflect to get word form of number
	numAsWord = inflectEngine.number_to_words(i)
	#remove spaces and hyphens
	numAsWord = numAsWord.replace(' ','').replace('-','')
	#add word length to total
	letters += len(numAsWord)

print(letters)


