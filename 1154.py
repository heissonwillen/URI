cont = 0
soma = 0

while True:
	n = int(input())
	
	if n >= 0:
		soma += n
		cont += 1
	else:
		break

print('{:.2f}'.format(soma / cont))