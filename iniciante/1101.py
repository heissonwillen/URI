while(True):
	m, n = input().split()
	m, n = int(m), int(n)

	if (m <= 0 or n <= 0):
		break
	else:
		soma = 0
		if (m > n):
			n, m = m, n

		for i in range (m, n +1):
			soma += i
			print(i, end=" ")
		print('Sum={}'.format(soma))