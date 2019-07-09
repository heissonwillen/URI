x = int(input())

for i in range (1, x +1):
		
	n = int(input())	
	
	if n == 0:
		print('NULL')
	else:
		if n % 2 == 0:
			print('EVEN ', end="")
		if n % 2 != 0:
			print('ODD ', end="")
		if n < 0:
			print('NEGATIVE')
		if n > 0:
			print('POSITIVE')