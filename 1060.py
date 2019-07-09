positivos = 0

for n in range (6):
	val = float(input())

	if (val > 0):
		positivos += 1

print('{} valores positivos'.format(positivos))