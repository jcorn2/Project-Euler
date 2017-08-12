def fib(n):
	num1 = 1
	num2 = 2
	fibNums = [num1]

	while(num2 < n):
		fibNums.append(num2)
		temp = num2
		num2 += num1
		num1 = temp

	return fibNums

def sumEven(fibNums):
	return sum([i for i in fibNums if i % 2 == 0])

print(sumEven(fib(4000000)))




