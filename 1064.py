soma = 0
pos = 0

for i in range (6):
	n = float(input())
	if (n > 0):
		soma += n
		pos += 1

media = (soma / pos)

print('{} valores positivos'.format(pos))
print('{:.1f}'.format(media))