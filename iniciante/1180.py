x = int(input())

menor = 0

for i in range(1, x + 1):
	n = int(input())

	if (n < menor or n == 1):
		menor = n
		pos = i

print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')
