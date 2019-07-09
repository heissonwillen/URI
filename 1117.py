cont = 0
soma = 0

while True:
	n = float(input())
	
	if 0 <= n <= 10:
		soma += n
		cont += 1

		if cont == 2:
			break
	else:
		print('nota invalida')

print('media = {}'.format(soma / cont))