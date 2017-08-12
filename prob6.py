from functools import reduce

nums = list(range(1,100+ 1))

numsSq = [i*i for i in nums]
sumOfSq = reduce(lambda x,y: x + y,numsSq)
sqOfSum = reduce(lambda x,y: x + y,nums) ** 2

print(sqOfSum - sumOfSq)




