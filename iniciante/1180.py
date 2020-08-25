x = int(input())

menor = 0

for i in range(1, x + 1):
	n = int(input())

	'''
	if (i == 1):
		menor = n
		pos = i
	'''

	if (n < menor or n == 1):
		menor = n
		pos = i

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(pos))