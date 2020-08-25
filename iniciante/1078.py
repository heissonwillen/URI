x, y = 1, 2

while (x != y):
	x, y = input().split()
	
	x = int(x)
	y = int(y)

	if (x > y):
		print('Crescente')
	else: 
		print('Decrescente')