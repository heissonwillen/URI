x = int(input())

for i in range(x):
	n = int(input())

	soma = 0
	perfeito = False

	for j in range(1, n):
		if (n % j == 0):
			soma += j

	if (soma == n):
		print('{} eh perfeito'.format(n))
	else:
		print('{} nao eh perfeito'.format(n))