while (True):
	x, y = input().split()
	x, y = int(x), int(y)

	if (x == 0 or y == 0):	
		break
	else:
		if (x > 0 and y > 0):
			q = 'primeiro'
		if (x < 0 and y > 0):
			q = 'segundo'
		if (x < 0 and y < 0):
			q = 'terceiro'
		if (x > 0 and y < 0):
			q = 'quarto'
	print(q)