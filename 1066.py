par = imp = pos = neg = 0

for i in range (5):
	n = int(input())
	
	if (n % 2 == 0):
		par += 1
	elif (n % 2 != 0):
		imp += 1

	if (n > 0):
		pos += 1
	elif (n < 0):
		neg += 1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(imp))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))