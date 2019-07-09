x, y = 1, 2

while True:
	x, y = input().split()
	
	x = int(x)
	y = int(y)

	if (x == y):
		break

	if (x < y):
		print('Crescente')
	else: 
		print('Decrescente')